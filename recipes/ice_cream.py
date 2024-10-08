from dataclasses import dataclass, field
from typing import List, Dict, Union

from recipe import Recipe
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
        totals['total_sweetness'] = sum(
            ing.sweetness * ing.weight / 100 for ing in self.ingredients if hasattr(ing, 'sweetness')
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
                value = totals[constraint.property] / totals['total_weight'] * 100
                validations[f"{constraint.name}_within_range"] = constraint.min_value <= value <= constraint.max_value
                validations[f"{constraint.name}_value"] = value

        validations['total_weight_correct'] = abs(totals['total_weight'] - self.total_weight) <= 1
        return validations