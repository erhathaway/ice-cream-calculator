from copy import deepcopy
from dataclasses import dataclass, field
from typing import List, Dict

from ingredients.base import Ingredient

@dataclass
class Recipe:
    total_weight: float = 1000.0
    ingredients: List[Ingredient] = field(default_factory=list)

    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)

    def add_ingredient_with_weight(self, ingredient: Ingredient, weight: float):
        ing_copy = deepcopy(ingredient)
        ing_copy.weight = weight
        self.ingredients.append(ing_copy)

    def calculate_totals(self) -> Dict[str, float]:
        totals = {
            'total_fat': 0.0,
            'total_carbs': 0.0,
            'total_protein': 0.0,
            'total_weight': 0.0,
            'total_calories': 0.0,
            'total_fiber': 0.0,
                    }
        for ing in self.ingredients:
            for nutrient in ['fat', 'carbs', 'protein', 'calories', 'fiber']:
                if hasattr(ing, nutrient): 
                    totals[f'total_{nutrient}'] += getattr(ing, nutrient) * ing.weight / 100
                else:
                    print(f"Warning: {nutrient} attribute not found for {ing.name}")
            totals['total_weight'] += ing.weight
        return totals

    def adjust_ingredient_weights(self):
        total_current_weight = sum(ing.weight for ing in self.ingredients)
        if total_current_weight == 0:
            return
        print(f"Total weight: {self.total_weight}") 
        print("/")
        print(f"Total current weight: {total_current_weight}")
        scaling_factor = self.total_weight / total_current_weight
        print(f"Scaling factor: {scaling_factor}")
        for ing in self.ingredients:
            ing.weight *= scaling_factor

    def validate_mix(self):
        raise NotImplementedError("This method should be implemented by subclasses")
    
    