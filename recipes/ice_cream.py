from dataclasses import dataclass
from typing import List, Dict, Union

from recipe import Recipe
from ingredients import Ingredient, GumAgentProps, SweetenerProps, EmulsifierProps

@dataclass
class IceCreamGumAgentProps(GumAgentProps):
    ideal_usage: float = 0.15  # Example: 0.15% for ice cream

@dataclass
class IceCreamSweetenerProps(SweetenerProps):
    ideal_usage: float = 15.0  # Example: 15% for ice cream

@dataclass
class IceCreamEmulsifierProps(EmulsifierProps):
    ideal_usage: float = 0.2  # Example: 0.2% for ice cream

@dataclass
class IceCreamRecipe(Recipe):
    ideal_fat_percentage: float = 10.0
    fat_tolerance: float = 2.0
    ideal_sugar_percentage: float = 15.0
    sugar_tolerance: float = 1.0

    def calculate_totals(self):
        totals = super().calculate_totals()
        totals['total_sweetness'] = sum(
            ing.sweetness * ing.weight / 100 for ing in self.ingredients
        )
        return totals

    def recommend_amounts(self, items: List[Ingredient]) -> Dict[str, float]:
        recommended = {}
        total_weight = self.total_weight
        remaining_weight = total_weight

        for item in items:
            if item.sweetener_props:
                props = IceCreamSweetenerProps(**item.sweetener_props.__dict__)
                recommended[item.name] = props.ideal_usage * total_weight / 100
            elif item.gum_agent_props:
                props = IceCreamGumAgentProps(**item.gum_agent_props.__dict__)
                recommended[item.name] = props.ideal_usage * total_weight / 100
            elif item.emulsifier_props:
                props = IceCreamEmulsifierProps(**item.emulsifier_props.__dict__)
                recommended[item.name] = props.ideal_usage * total_weight / 100
            else:
                # For other ingredients, distribute the remaining weight equally
                recommended[item.name] = remaining_weight / (len(items) - len(recommended))

            remaining_weight -= recommended[item.name]

        return recommended

    def validate_mix(self) -> Dict[str, Union[bool, float]]:
        totals = self.calculate_totals()
        percentages = {
            nutrient: (totals[f'total_{nutrient}'] / totals['total_weight']) * 100
            for nutrient in ['fat', 'carbs', 'protein']
        }
        validations = {
            'fat_within_range': abs(percentages['fat'] - self.ideal_fat_percentage) <= self.fat_tolerance,
            'sugar_within_range': abs(percentages['carbs'] - self.ideal_sugar_percentage) <= self.sugar_tolerance,
            'protein_content': percentages['protein'],
            'total_weight_correct': abs(totals['total_weight'] - self.total_weight) <= 1
        }
        return validations