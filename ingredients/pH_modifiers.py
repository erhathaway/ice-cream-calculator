from .base import (
    ingredients_manager, Ingredient, Flavor, PHModifier, PHBuffer, Colorant
)

# pH modifiers and buffers

# Sodium Citrate
ingredients_manager.add(Ingredient(
    name='Sodium Citrate',
    category=['pH Modifier'],
    fat=0.0,
    carbs=0.0,
    protein=0.0,
    weight=0.0,
    flavor_profiles=Flavor(flavor_notes={'Slightly Salty': 1.0}),
    ph_buffer=PHBuffer(buffering_capacity=1.0),
    colorant=Colorant(color='White', natural=True),
))

# Citric Acid
ingredients_manager.add(Ingredient(
    name='Citric Acid',
    category=['pH Modifier'],
    fat=0.0,
    carbs=0.0,
    protein=0.0,
    weight=0.0,
    ph_modifier=PHModifier(ph_change=-0.5),
    ph_buffer=PHBuffer(buffering_capacity=0.8),
    flavor_profiles=Flavor(flavor_notes={'Sour': 1.0}),
    colorant=Colorant(color='White', natural=True),
))

# Potassium Phosphate
ingredients_manager.add(Ingredient(
    name='Potassium Phosphate',
    category=['pH Modifier'],
    fat=0.0,
    carbs=0.0,
    protein=0.0,
    weight=0.0,
    ph_buffer=PHBuffer(buffering_capacity=1.0),
    flavor_profiles=Flavor(flavor_notes={'Slightly Bitter': 1.0}),
    colorant=Colorant(color='White', natural=False),
))

# Sodium Bicarbonate
ingredients_manager.add(Ingredient(
    name='Sodium Bicarbonate',
    category=['pH Modifier'],
    fat=0.0,
    carbs=0.0,
    protein=0.0,
    weight=0.0,
    ph_modifier=PHModifier(ph_change=0.5),
    ph_buffer=PHBuffer(buffering_capacity=0.7),
    flavor_profiles=Flavor(flavor_notes={'Slightly Salty': 1.0}),
    colorant=Colorant(color='White', natural=True),
))

# Calcium Carbonate
ingredients_manager.add(Ingredient(
    name='Calcium Carbonate',
    category=['pH Modifier'],
    fat=0.0,
    carbs=0.0,
    protein=0.0,
    weight=0.0,
    ph_modifier=PHModifier(ph_change=0.6),
    ph_buffer=PHBuffer(buffering_capacity=0.9),
    flavor_profiles=Flavor(flavor_notes={'Chalky': 1.0}),
    colorant=Colorant(color='White', natural=True),
))