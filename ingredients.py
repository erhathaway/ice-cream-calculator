from dataclasses import dataclass, field
from typing import List, Optional

# Functional property classes
@dataclass
class FreezingPointDepressant:
    fpdf: float  # Freezing Point Depression Factor

@dataclass
class Flavor:
    flavor_notes: List[str] = field(default_factory=list)

@dataclass
class PHModifier:
    ph_change: float  # Effect on pH (negative lowers pH, positive raises pH)

@dataclass
class PHBuffer:
    buffering_capacity: float  # Numeric value representing buffering strength

@dataclass
class ViscosityModifier:
    viscosity_effect: float  # Numeric value representing impact on viscosity

@dataclass
class MeltingRateModifier:
    melting_rate_effect: float  # Numeric value representing impact on melting rate

@dataclass
class Colorant:
    color: str                # Description or color code (e.g., 'red', '#FF0000')
    natural: bool = True      # Whether the colorant is natural or synthetic

@dataclass
class IngredientAttribute:
    pass

@dataclass
class GumAgentProps(IngredientAttribute):
    ideal_usage_min: float = 0.0
    ideal_usage_max: float = 0.0
    activation_temp: float = 0.0
    cold_soluble: bool = False
    interactions: List[str] = field(default_factory=list)

@dataclass
class SweetenerProps(IngredientAttribute):
    glycemic_index: float = 0.0
    relative_sweetness: float = 0.0
    ideal_usage: float = 0.0

@dataclass
class EmulsifierProps(IngredientAttribute):
    hld_value: float = 0.0
    ideal_usage: float = 0.0

# Ingredient class with properties as attributes
@dataclass
class Ingredient:
    name: str
    fat: float
    carbs: float
    protein: float
    weight: float
    sweetness: float = 0.0
    gum_agent_props: Optional[GumAgentProps] = None
    sweetener_props: Optional[SweetenerProps] = None
    emulsifier_props: Optional[EmulsifierProps] = None

    # Functional properties
    fpdf: Optional[FreezingPointDepressant] = None
    flavor_profiles: Optional[Flavor] = None
    ph_modifier: Optional[PHModifier] = None
    ph_buffer: Optional[PHBuffer] = None
    viscosity_modifier: Optional[ViscosityModifier] = None
    melting_rate_modifier: Optional[MeltingRateModifier] = None
    colorant: Optional[Colorant] = None

    # Specific properties
    emulsifier_props: Optional[EmulsifierProps] = None
    sweetener_props: Optional[SweetenerProps] = None
    gum_agent_props: Optional[GumAgentProps] = None

# Class to manage a collection of ingredients
class Ingredients:
    def __init__(self):
        self.ingredients: List[Ingredient] = []

    def add(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)

    def list_all(self) -> List[str]:
        return [ingredient.name for ingredient in self.ingredients]

    def group_by_category(self) -> dict:
        groups = {}
        for ingredient in self.ingredients:
            groups.setdefault(ingredient.category, []).append(ingredient)
        return groups

    def sort_by_property(self, property_name: str, reverse: bool = False) -> List[Ingredient]:
        return sorted(
            self.ingredients,
            key=lambda x: getattr(x, property_name, 0),
            reverse=reverse
        )

    def filter_by_range(self, property_name: str, min_value: float, max_value: float) -> List[Ingredient]:
        return [
            ingredient for ingredient in self.ingredients
            if min_value <= getattr(ingredient, property_name, 0) <= max_value
        ]

# Initialize Ingredients manager
ingredients_manager = Ingredients()
