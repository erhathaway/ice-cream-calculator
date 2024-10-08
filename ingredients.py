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
    emulsifier_props: Optional[EmulsifierProperties] = None
    sweetener_props: Optional[SweetenerProperties] = None
    gum_agent_props: Optional[GumAgentProperties] = None

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

# Adding ingredients to the manager
# Dairy Ingredients
ingredients_manager.add(Ingredient(
    name='Whole Milk',
    category='Dairy',
    fat=3.25,
    carbs=4.8,
    protein=3.15,
    sweetness=0.1,
    emulsification=0.2,
    fpdf=FreezingPointDepressant(fpdf=0.5),
    flavor_profiles=Flavor(flavor_notes=['Creamy', 'Slightly Sweet']),
    ph_modifier=PHModifier(ph_change=-0.1),
    ph_buffer=PHBuffer(buffering_capacity=0.8),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.0),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=1.0),
    colorant=Colorant(color='White', natural=True),
))

# Additional pH Buffers
ingredients_manager.add(Ingredient(
    name='Sodium Citrate',
    category='pH Buffer',
    flavor_profiles=Flavor(flavor_notes=['Slightly Salty']),
    ph_buffer=PHBuffer(buffering_capacity=1.0),
    colorant=Colorant(color='White', natural=True),
))

ingredients_manager.add(Ingredient(
    name='Citric Acid',
    category='pH Buffer',
    ph_modifier=PHModifier(ph_change=-0.5),
    ph_buffer=PHBuffer(buffering_capacity=0.8),
    flavor_profiles=Flavor(flavor_notes=['Sour']),
    colorant=Colorant(color='White', natural=True),
))

ingredients_manager.add(Ingredient(
    name='Potassium Phosphate',
    category='pH Buffer',
    ph_buffer=PHBuffer(buffering_capacity=1.0),
    flavor_profiles=Flavor(flavor_notes=['Slightly Bitter']),
    colorant=Colorant(color='White', natural=False),
))

ingredients_manager.add(Ingredient(
    name='Sodium Bicarbonate',
    category='pH Buffer',
    ph_modifier=PHModifier(ph_change=0.5),
    ph_buffer=PHBuffer(buffering_capacity=0.7),
    flavor_profiles=Flavor(flavor_notes=['Slightly Salty']),
    colorant=Colorant(color='White', natural=True),
))

ingredients_manager.add(Ingredient(
    name='Calcium Carbonate',
    category='pH Buffer',
    ph_modifier=PHModifier(ph_change=0.6),
    ph_buffer=PHBuffer(buffering_capacity=0.9),
    flavor_profiles=Flavor(flavor_notes=['Chalky']),
    colorant=Colorant(color='White', natural=True),
))

# Additional Viscosity Modifiers
ingredients_manager.add(Ingredient(
    name='Corn Starch',
    category='Thickener',
    fat=0.1,
    carbs=91.3,
    protein=0.3,
    viscosity_modifier=ViscosityModifier(viscosity_effect=5.0),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='White', natural=True),
))

ingredients_manager.add(Ingredient(
    name='Carrageenan',
    category='Thickener',
    carbs=80.0,
    protein=2.0,
    viscosity_modifier=ViscosityModifier(viscosity_effect=10.0),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='Off-white', natural=True),
))

ingredients_manager.add(Ingredient(
    name='Locust Bean Gum',
    category='Thickener',
    fat=1.0,
    carbs=80.0,
    protein=5.0,
    viscosity_modifier=ViscosityModifier(viscosity_effect=12.0),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='Off-white', natural=True),
))

ingredients_manager.add(Ingredient(
    name='Pectin',
    category='Thickener',
    carbs=90.0,
    viscosity_modifier=ViscosityModifier(viscosity_effect=8.0),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='Off-white', natural=True),
))

ingredients_manager.add(Ingredient(
    name='Agar-Agar',
    category='Thickener',
    carbs=80.0,
    protein=6.0,
    viscosity_modifier=ViscosityModifier(viscosity_effect=15.0),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='Off-white', natural=True),
))

# Additional Melting Rate Modifiers
ingredients_manager.add(Ingredient(
    name='Propylene Glycol',
    category='Melting Rate Modifier',
    sweetness=0.6,
    fpdf=FreezingPointDepressant(fpdf=1.6),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.7),
    flavor_profiles=Flavor(flavor_notes=['Slightly Sweet']),
    colorant=Colorant(color='Colorless', natural=False),
))

ingredients_manager.add(Ingredient(
    name='Glycerol (Glycerin)',
    category='Melting Rate Modifier',
    sweetness=0.6,
    fpdf=FreezingPointDepressant(fpdf=1.92),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.8),
    flavor_profiles=Flavor(flavor_notes=['Sweet']),
    colorant=Colorant(color='Colorless', natural=False),
))

ingredients_manager.add(Ingredient(
    name='Fructose',
    category='Sugar',
    carbs=100.0,
    sweetness=1.7,
    fpdf=FreezingPointDepressant(fpdf=1.9),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.8),
    flavor_profiles=Flavor(flavor_notes=['Sweet']),
    colorant=Colorant(color='White', natural=True),
    sweetener_props=SweetenerProperties(
        glycemic_index=19.0,
        relative_sweetness=1.7,
        ideal_usage=10.0
    ),
))

ingredients_manager.add(Ingredient(
    name='Dextrose',
    category='Sugar',
    carbs=100.0,
    sweetness=0.75,
    fpdf=FreezingPointDepressant(fpdf=1.9),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.85),
    flavor_profiles=Flavor(flavor_notes=['Sweet']),
    colorant=Colorant(color='White', natural=True),
    sweetener_props=SweetenerProperties(
        glycemic_index=100.0,
        relative_sweetness=0.75,
        ideal_usage=15.0
    ),
))

ingredients_manager.add(Ingredient(
    name='Corn Syrup Solids',
    category='Sweetener',
    carbs=100.0,
    sweetness=0.4,
    fpdf=FreezingPointDepressant(fpdf=1.8),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.9),
    flavor_profiles=Flavor(flavor_notes=['Mildly Sweet']),
    colorant=Colorant(color='White', natural=True),
    sweetener_props=SweetenerProperties(
        glycemic_index=75.0,
        relative_sweetness=0.4,
        ideal_usage=15.0
    ),
))

ingredients_manager.add(Ingredient(
    name='Maltodextrin',
    category='Sweetener',
    carbs=95.0,
    sweetness=0.1,
    fpdf=FreezingPointDepressant(fpdf=1.5),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.95),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='White', natural=True),
    sweetener_props=SweetenerProperties(
        glycemic_index=85.0,
        relative_sweetness=0.1,
        ideal_usage=10.0
    ),
))

# Emulsifiers
ingredients_manager.add(Ingredient(
    name='Egg Yolks',
    category='Emulsifier',
    fat=26.5,
    carbs=3.6,
    protein=15.9,
    emulsification=1.0,
    fpdf=FreezingPointDepressant(fpdf=0.0),
    flavor_profiles=Flavor(flavor_notes=['Rich', 'Creamy']),
    ph_buffer=PHBuffer(buffering_capacity=0.5),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.5),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=1.2),
    colorant=Colorant(color='Yellow', natural=True),
    emulsifier_props=EmulsifierProperties(
        ideal_usage=0.5,
        source='Animal-based',
        hlb_value=7.0,
        interactions=[],
    ),
))

ingredients_manager.add(Ingredient(
    name='Soy Lecithin',
    category='Emulsifier',
    fat=100.0,
    emulsification=0.9,
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.2),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.95),
    flavor_profiles=Flavor(flavor_notes=['Mild', 'Nutty']),
    colorant=Colorant(color='Light Brown', natural=True),
    emulsifier_props=EmulsifierProperties(
        ideal_usage=0.3,
        source='Plant-based',
        hlb_value=8.0,
        interactions=[],
    ),
))

ingredients_manager.add(Ingredient(
    name='Polysorbate 80',
    category='Emulsifier',
    emulsification=1.0,
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.0),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.9),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='Amber', natural=False),
    emulsifier_props=EmulsifierProperties(
        ideal_usage=0.02,
        source='Synthetic',
        hlb_value=15.0,
        interactions=[],
    ),
))

ingredients_manager.add(Ingredient(
    name='Mono and Diglycerides',
    category='Emulsifier',
    fat=100.0,
    emulsification=0.85,
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.1),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.9),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='Off-white', natural=False),
    emulsifier_props=EmulsifierProperties(
        ideal_usage=0.2,
        source='Synthetic',
        hlb_value=3.8,
        interactions=[],
    ),
))

ingredients_manager.add(Ingredient(
    name='Polyglycerol Polyricinoleate',
    category='Emulsifier',
    fat=100.0,
    emulsification=1.0,
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.0),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.95),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='Amber', natural=False),
    emulsifier_props=EmulsifierProperties(
        ideal_usage=0.03,
        source='Synthetic',
        hlb_value=1.5,
        interactions=[],
    ),
))

ingredients_manager.add(Ingredient(
    name='Sorbitan Monostearate',
    category='Emulsifier',
    fat=95.0,
    carbs=5.0,
    emulsification=0.85,
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.1),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.9),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='Yellowish', natural=False),
    emulsifier_props=EmulsifierProperties(
        ideal_usage=0.5,
        source='Synthetic',
        hlb_value=4.7,
        interactions=[],
    ),
))

ingredients_manager.add(Ingredient(
    name='Sodium Stearoyl Lactylate',
    category='Emulsifier',
    fat=100.0,
    emulsification=0.9,
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.2),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.92),
    flavor_profiles=Flavor(flavor_notes=['Slightly Creamy']),
    colorant=Colorant(color='White to Cream', natural=False),
    emulsifier_props=EmulsifierProperties(
        ideal_usage=0.4,
        source='Synthetic',
        hlb_value=21.0,
        interactions=[],
    ),
))

ingredients_manager.add(Ingredient(
    name='Sunflower Lecithin',
    category='Emulsifier',
    fat=100.0,
    emulsification=0.8,
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.2),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.95),
    flavor_profiles=Flavor(flavor_notes=['Mild', 'Nutty']),
    colorant=Colorant(color='Light Brown', natural=True),
    emulsifier_props=EmulsifierProperties(
        ideal_usage=0.3,
        source='Plant-based',
        hlb_value=8.0,
        interactions=[],
    ),
))

ingredients_manager.add(Ingredient(
    name='Enzymatically Modified Lecithin',
    category='Emulsifier',
    fat=99.0,
    carbs=1.0,
    emulsification=0.95,
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.3),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.9),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='Light Brown', natural=False),
    emulsifier_props=EmulsifierProperties(
        ideal_usage=0.3,
        source='Plant-based',
        hlb_value=11.0,
        interactions=[],
    ),
))

# Gum Agents
ingredients_manager.add(Ingredient(
    name='Guar Gum',
    category='Stabilizer',
    carbs=80.0,
    protein=5.0,
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    viscosity_modifier=ViscosityModifier(viscosity_effect=10.0),
    colorant=Colorant(color='Off-white', natural=True),
    ph_modifier=PHModifier(ph_change=0.0),
    gum_agent_props=GumAgentProperties(
        ideal_usage_min=0.1,
        ideal_usage_max=0.5,
        activation_temp=25.0,
        cold_soluble=True,
        interactions=['Locust Bean Gum', 'Xanthan Gum'],
    ),
))

ingredients_manager.add(Ingredient(
    name='Carrageenan',
    category='Stabilizer',
    carbs=80.0,
    protein=2.0,
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    viscosity_modifier=ViscosityModifier(viscosity_effect=10.0),
    colorant=Colorant(color='Off-white', natural=True),
    gum_agent_props=GumAgentProperties(
        ideal_usage_min=0.01,
        ideal_usage_max=0.05,
        activation_temp=60.0,
        cold_soluble=False,
        interactions=['Locust Bean Gum'],
    ),
))

ingredients_manager.add(Ingredient(
    name='Locust Bean Gum',
    category='Stabilizer',
    fat=1.0,
    carbs=80.0,
    protein=5.0,
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    viscosity_modifier=ViscosityModifier(viscosity_effect=12.0),
    colorant=Colorant(color='White to yellowish', natural=True),
    gum_agent_props=GumAgentProperties(
        ideal_usage_min=0.05,
        ideal_usage_max=0.2,
        activation_temp=85.0,
        cold_soluble=False,
        interactions=['Guar Gum', 'Carrageenan'],
    ),
))

ingredients_manager.add(Ingredient(
    name='Xanthan Gum',
    category='Stabilizer',
    carbs=77.0,
    protein=7.0,
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    viscosity_modifier=ViscosityModifier(viscosity_effect=15.0),
    colorant=Colorant(color='Creamy White', natural=True),
    gum_agent_props=GumAgentProperties(
        ideal_usage_min=0.05,
        ideal_usage_max=0.3,
        activation_temp=25.0,
        cold_soluble=True,
        interactions=['Guar Gum', 'Locust Bean Gum'],
    ),
))

ingredients_manager.add(Ingredient(
    name='Agar-Agar',
    category='Stabilizer',
    carbs=80.0,
    protein=6.0,
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    viscosity_modifier=ViscosityModifier(viscosity_effect=20.0),
    colorant=Colorant(color='Off-white', natural=True),
    gum_agent_props=GumAgentProperties(
        ideal_usage_min=0.1,
        ideal_usage_max=0.5,
        activation_temp=85.0,
        cold_soluble=False,
        interactions=[],
    ),
))

# Update dictionaries if needed
ingredients_dict = {ingredient.name: ingredient for ingredient in ingredients_manager.ingredients}

# Example operations
# List all ingredients
# print("All Ingredients:")
# for name in ingredients_manager.list_all():
#     print(name)

# Group ingredients by category
# print("\nIngredients Grouped by Category:")
# grouped = ingredients_manager.group_by_category()
# for category, ingredients in grouped.items():
#     print(f"{category}: {[ingredient.name for ingredient in ingredients]}")

# Sort ingredients by sweetness
# print("\nIngredients Sorted by Sweetness:")
# sorted_by_sweetness = ingredients_manager.sort_by_property('sweetness', reverse=True)
# for ingredient in sorted_by_sweetness:
#     print(f"{ingredient.name}: {ingredient.sweetness}")

# Filter ingredients with viscosity_effect greater than 10
# print("\nIngredients with Viscosity Effect greater than 10:")
# filtered_ingredients = [
#     ingredient for ingredient in ingredients_manager.ingredients
#     if ingredient.viscosity_modifier and ingredient.viscosity_modifier.viscosity_effect > 10
# ]
# for ingredient in filtered_ingredients:
#     print(f"{ingredient.name}: {ingredient.viscosity_modifier.viscosity_effect}")
