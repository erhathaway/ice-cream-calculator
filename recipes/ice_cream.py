from dataclasses import dataclass, field
from typing import List, Dict, Union

from recipes import Recipe
from ingredients import Ingredient
from constraints import Constraints

@dataclass
class IceCreamRecipe(Recipe):
    constraints: Constraints = field(default_factory=Constraints)

    def calculate_totals(self):
        totals = super().calculate_totals()
        totals['total_sweetener'] = sum(
            ing.weight for ing in self.ingredients if hasattr(ing, 'sweetener_props')
        )
        totals['total_gum_agent'] = sum(
            ing.weight for ing in self.ingredients if hasattr(ing, 'gum_agent_props')
        )
        totals['total_emulsifier'] = sum(
            ing.weight for ing in self.ingredients if hasattr(ing, 'emulsifier_props')
        )
        totals['total_viscosity_modifier'] = sum(
            ing.weight for ing in self.ingredients if hasattr(ing, 'viscosity_modifier') and ing.viscosity_modifier is not None and ing.viscosity_modifier.viscosity_effect != 0
        )
        totals['total_melting_rate_modifier'] = sum(
            ing.weight for ing in self.ingredients if hasattr(ing, 'melting_rate_modifier') and ing.melting_rate_modifier is not None and ing.melting_rate_modifier.melting_rate_effect != 0
        )
        totals['total_ph_modifier'] = sum(
            ing.weight for ing in self.ingredients if hasattr(ing, 'ph_modifier') and ing.ph_modifier is not None and ing.ph_modifier.ph_change != 0
        )
        totals['total_ph_buffer'] = sum(
            ing.weight for ing in self.ingredients if hasattr(ing, 'ph_buffer') and ing.ph_buffer is not None and ing.ph_buffer.buffering_capacity != 0
        )
        totals['total_flavor_profiles'] = sum(
            ing.weight for ing in self.ingredients if hasattr(ing, 'flavor_profiles') and ing.flavor_profiles is not None and ing.flavor_profiles.flavor_notes != {}
        )
        totals['total_colorant'] = sum(
            ing.weight for ing in self.ingredients if hasattr(ing, 'colorant') and ing.colorant is not None and ing.colorant.color is not None
        )

        return totals

    def recommend_amounts(self, items: List[Ingredient]) -> Dict[str, float]:
        recommended = {}
        total_weight = self.total_weight
        remaining_weight = total_weight

        for item in items:
            if item.sweetener_props:
                recommended[item.name] = self.constraints.sweetener.ideal_value * total_weight / 100
            elif item.gum_agent_props:
                recommended[item.name] = self.constraints.gum_agent.ideal_value * total_weight / 100
            elif item.emulsifier_props:
                recommended[item.name] = self.constraints.emulsifier.ideal_value * total_weight / 100
            else:
                # For other ingredients, distribute the remaining weight equally
                recommended[item.name] = remaining_weight / (len(items) - len(recommended))

            remaining_weight -= recommended[item.name]

        return recommended

    def validate_mix(self) -> Dict[str, Union[bool, float]]:
        totals = self.calculate_totals()
        validations = {}

        for constraint in self.constraints.constraints:
            if constraint.property in totals:
                if totals['total_weight'] == 0:
                    # Handle the zero total weight case
                    value = 0  # or consider raising an exception
                else:
                    value = totals[constraint.property] / totals['total_weight'] * 100

                validations[f"{constraint.name}_within_range"] = constraint.min_value <= value <= constraint.max_value
                validations[f"{constraint.name}_value"] = value

        validations['total_weight_correct'] = abs(totals['total_weight'] - self.total_weight) <= 1
        return validations
    
    def recommend_adjustments(self):
        max_iterations = 10
        adjustments = {}
        for _ in range(max_iterations):
            totals = self.calculate_totals()
            validations = self.validate_mix()
            is_valid = all(
                v for k, v in validations.items() if 'within_range' in k
            )
            if is_valid:
                break

            for constraint in self.constraints.constraints:
                property_name = constraint.property
                constraint_name = constraint.name
                within_range_key = f"{constraint_name}_within_range"
                value_key = f"{constraint_name}_value"

                if within_range_key in validations and not validations[within_range_key]:
                    current_percentage = validations[value_key]
                    difference_percentage = constraint.ideal_value - current_percentage
                    weight_difference = difference_percentage * totals['total_weight'] / 100

                    # Identify ingredients that affect this property
                    applicable_ingredients = []
                    for ing in self.ingredients:
                        if property_name == 'total_fat' and getattr(ing, 'fat', 0) > 0:
                            applicable_ingredients.append(ing)
                        elif property_name == 'total_carbs' and getattr(ing, 'carbs', 0) > 0:
                            applicable_ingredients.append(ing)
                        elif property_name == 'total_protein' and getattr(ing, 'protein', 0) > 0:
                            applicable_ingredients.append(ing)
                        elif property_name == 'total_sweetener' and getattr(ing, 'sweetener_props', None):
                            applicable_ingredients.append(ing)
                        elif property_name == 'total_gum_agent' and getattr(ing, 'gum_agent_props', None):
                            applicable_ingredients.append(ing)
                        elif property_name == 'total_emulsifier' and getattr(ing, 'emulsifier_props', None):
                            applicable_ingredients.append(ing)
                        # Add other properties as needed

                    total_current_weight = sum(ing.weight for ing in applicable_ingredients)
                    if total_current_weight > 0:
                        for ing in applicable_ingredients:
                            weight_fraction = ing.weight / total_current_weight
                            ing_weight_adjustment = weight_difference * weight_fraction
                            ing.weight += ing_weight_adjustment
                            adjustments[ing.name] = adjustments.get(ing.name, 0) + ing_weight_adjustment
                    else:
                        # No ingredients to adjust for this property
                        pass

            # Recalculate total weight
            self.total_weight = sum(ing.weight for ing in self.ingredients)

        else:
            print("Unable to reach a valid mix within the maximum iterations.")

        return adjustments
