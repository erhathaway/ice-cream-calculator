from dataclasses import dataclass, field
from typing import List, Optional, Dict
from copy import deepcopy

# Functional property classes
@dataclass
class FreezingPointDepressant:
    fpdf: float  # Freezing Point Depression Factor

@dataclass
class Flavor:
    flavor_notes: Dict[str, float] = field(default_factory=dict)  # {'sweet': 0.8, 'bitter': 0.2}

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
    hlb_value: float = 0.0
    ideal_usage: float = 0.0
    source: str = ''
    interactions: List[str] = field(default_factory=list)
    emulsification: float = 0.0  # Added emulsification field here

@dataclass
class PhysicalChemicalProperties:
    pH: Optional[float] = None
    melting_point: Optional[float] = None  # in °C
    boiling_point: Optional[float] = None  # in °C
    solubility: Optional[str] = None       # e.g., 'Water-soluble', 'Insoluble'
    hygroscopic: bool = False

@dataclass
class IngredientInteraction:
    reacting_ingredient: str
    reaction_type: str           # e.g., 'Maillard Reaction', 'Enzymatic Browning'
    effect: str                  # e.g., 'Color Change', 'Flavor Enhancement'

@dataclass
class RheologicalProperties:
    viscosity: float = None           # in Pa·s
    shear_rate_dependence: float = 0.0  # Flow behavior index n in Power-law fluid
    yield_stress: float = None        # in Pa
    thixotropic: bool = False

# Ingredient class with properties as attributes
@dataclass
class Ingredient:
    name: str
    category: List[str]
    fat: float = 0.0        # in grams per 100g
    carbs: float = 0.0      # in grams per 100g
    protein: float = 0.0    # in grams per 100g
    weight: float = 0.0     # in grams
    calories: float = 0.0   # in kcal per 100g
    fiber: float = 0.0      # in grams per 100g
    vitamins: Dict[str, float] = field(default_factory=dict)
    minerals: Dict[str, float] = field(default_factory=dict)
    sweetness: float = 0.0

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

    # Additional property
    water_activity: float = 0.0  # Value between 0 (completely dry) and 1 (pure water)

    # New property
    physical_chemical_properties: Optional[PhysicalChemicalProperties] = None

    # New property
    allergens: List[str] = field(default_factory=list)

    # New property
    interactions: List[IngredientInteraction] = field(default_factory=list)

    def add_interaction(self, interaction: IngredientInteraction):
        self.interactions.append(interaction)

    # New property
    shelf_life_days: float = 0.0
    optimal_storage_temperature: float = 25.0  # in °C

    def remaining_shelf_life(self, days_since_manufacture: float, storage_temperature: float) -> float:
        temperature_factor = max(0.1, 1 - 0.05 * (storage_temperature - self.optimal_storage_temperature))
        adjusted_shelf_life = self.shelf_life_days * temperature_factor
        return max(0.0, adjusted_shelf_life - days_since_manufacture)

    rheological_properties: Optional[RheologicalProperties] = None

    density: Optional[float] = None  # Density in g/ml, required for volume to weight conversion

# Class to manage a collection of ingredients
class Ingredients:
    def __init__(self):
        self.ingredients: List[Ingredient] = []

    def add(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)

    def add_with_weight(self, ingredient: Ingredient, weight: float):
        ing_copy = deepcopy(ingredient)
        ing_copy.weight = weight
        self.ingredients.append(ing_copy)

    def list_all(self) -> List[str]:
        return [ingredient.name for ingredient in self.ingredients]

    def group_by_category(self) -> dict:
        groups = {}
        for ingredient in self.ingredients:
            for category in ingredient.category:
                groups.setdefault(category, []).append(ingredient)
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

    def calculate_total_nutrients(self) -> Dict[str, float]:
        total_nutrients = {
            'calories': 0.0,
            'fat': 0.0,
            'carbs': 0.0,
            'protein': 0.0,
            'fiber': 0.0
        }
        total_vitamins = {}
        total_minerals = {}

        for ingredient in self.ingredients:
            total_nutrients['calories'] += ingredient.calories
            total_nutrients['fat'] += ingredient.fat
            total_nutrients['carbs'] += ingredient.carbs
            total_nutrients['protein'] += ingredient.protein
            total_nutrients['fiber'] += ingredient.fiber

            for vitamin, amount in ingredient.vitamins.items():
                total_vitamins[vitamin] = total_vitamins.get(vitamin, 0) + amount

            for mineral, amount in ingredient.minerals.items():
                total_minerals[mineral] = total_minerals.get(mineral, 0) + amount

        total_nutrients['vitamins'] = total_vitamins
        total_nutrients['minerals'] = total_minerals
        return total_nutrients

    def calculate_pH(self) -> float:
        total_acid = 0.0
        total_base = 0.0
        total_buffer_capacity = 0.0

        for ingredient in self.ingredients:
            if ingredient.ph_modifier:
                delta_pH = ingredient.ph_modifier.ph_change
                buffer_capacity = ingredient.ph_buffer.buffering_capacity if ingredient.ph_buffer else 1.0

                if delta_pH < 0:
                    total_acid += abs(delta_pH) * buffer_capacity * ingredient.weight
                else:
                    total_base += delta_pH * buffer_capacity * ingredient.weight

                total_buffer_capacity += buffer_capacity * ingredient.weight

        if total_buffer_capacity == 0:
            return 7.0  # Neutral pH

        net_pH_change = (total_base - total_acid) / total_buffer_capacity
        return max(0, min(14, 7.0 + net_pH_change))  # Ensure pH between 0 and 14

    def calculate_viscosity(self, shear_rate: float = 1.0) -> float:
        """Calculate apparent viscosity of the mixture at a given shear rate."""
        total_viscosity = 0.0
        total_weight = 0.0

        for ingredient in self.ingredients:
            rp = ingredient.rheological_properties
            if rp and rp.viscosity:
                n = rp.shear_rate_dependence if rp.shear_rate_dependence else 1.0
                apparent_viscosity = rp.viscosity * (shear_rate ** (n - 1))
                total_viscosity += apparent_viscosity * ingredient.weight
                total_weight += ingredient.weight

        if total_weight == 0:
            return 0.0
        return total_viscosity / total_weight

    def get_ingredient_by_name(self, name: str) -> Ingredient:
        for ingredient in self.ingredients:
            if ingredient.name.lower() == name.lower():
                return ingredient
        raise ValueError(f"Ingredient '{name}' not found")


    def get_ingredient_with_weight(self, name: str, amount: float, unit: str) -> Ingredient:
        if not unit:
            print(f"Error with params {name}, {amount}, {unit}")
            print(f"Unit is required for get_ingredient_with_weight. Using default unit 'g'.")
            raise ValueError("Unit is required for get_ingredient_with_weight")
        ingredient = self.get_ingredient_by_name(name)
        weight_in_grams = convert_to_grams(amount, unit, density=ingredient.density)
        ing_copy = deepcopy(ingredient)
        ing_copy.weight = weight_in_grams
        return ing_copy
    
# Initialize Ingredients manager
ingredients_manager = Ingredients()


def convert_to_grams(amount: float, unit: str, density: Optional[float] = None) -> float:
    """
    Converts the given amount and unit to grams.
    If unit is a weight unit, converts directly.
    If unit is a volume unit, uses density to convert.
    """
    unit = unit.lower()
    weight_units = {
        'g': 1.0,
        'gram': 1.0,
        'grams': 1.0,
        'kg': 1000.0,
        'kilogram': 1000.0,
        'kilograms': 1000.0,
        'oz': 28.3495,
        'ounce': 28.3495,
        'ounces': 28.3495,
        'lb': 453.592,
        'pound': 453.592,
        'pounds': 453.592,
    }
    volume_units_ml = {
        'ml': 1.0,
        'milliliter': 1.0,
        'milliliters': 1.0,
        'l': 1000.0,
        'liter': 1000.0,
        'liters': 1000.0,
        'tsp': 4.92892,
        'teaspoon': 4.92892,
        'teaspoons': 4.92892,
        'tbsp': 14.7868,
        'tablespoon': 14.7868,
        'tablespoons': 14.7868,
        'cup': 240.0,
        'cups': 240.0,
    }

    if unit in weight_units:
        return amount * weight_units[unit]
    elif unit in volume_units_ml:
        if density is None:
            print(f"Error with params {density}, {amount}, {unit}")
            raise ValueError(f"Density is required to convert volume unit '{unit}' to grams")
        volume_in_ml = amount * volume_units_ml[unit]
        return volume_in_ml * density  # grams = volume (ml) * density (g/ml)
    else:
        raise ValueError(f"Unknown unit '{unit}'")