from dataclasses import dataclass, field
from typing import List, Dict

from ingredients import Ingredient

@dataclass
class Recipe:
    total_weight: float = 1000.0
    ingredients: List[Ingredient] = field(default_factory=list)

    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)

    def calculate_totals(self) -> Dict[str, float]:
        totals = {
            'total_fat': 0.0,
            'total_carbs': 0.0,
            'total_protein': 0.0,
            'total_weight': 0.0
        }
        for ing in self.ingredients:
            for nutrient in ['fat', 'carbs', 'protein']:
                totals[f'total_{nutrient}'] += getattr(ing, nutrient) * ing.weight / 100
            totals['total_weight'] += ing.weight
        return totals

    def adjust_ingredient_weights(self):
        total_current_weight = sum(ing.weight for ing in self.ingredients)
        scaling_factor = self.total_weight / total_current_weight
        for ing in self.ingredients:
            ing.weight *= scaling_factor

    def validate_mix(self):
        raise NotImplementedError("This method should be implemented by subclasses")