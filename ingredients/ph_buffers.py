from .base import ingredients_manager, Ingredient, Flavor, PHModifier, PHBuffer, Colorant

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