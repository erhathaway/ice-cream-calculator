from .base import ingredients_manager, Ingredient, FreezingPointDepressant, Flavor, PHModifier, PHBuffer, ViscosityModifier, MeltingRateModifier, Colorant

# Existing milk ingredients
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

# Add Coconut Milk
ingredients_manager.add(Ingredient(
    name='Coconut Milk',
    category='Dairy Alternative',
    fat=24.0,
    carbs=6.0,
    protein=2.0,
    sweetness=0.1,
    emulsification=0.2,
    fpdf=FreezingPointDepressant(fpdf=0.5),
    flavor_profiles=Flavor(flavor_notes=['Coconut']),
    ph_modifier=PHModifier(ph_change=-0.1),
    ph_buffer=PHBuffer(buffering_capacity=0.8),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.5),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.9),
    colorant=Colorant(color='White', natural=True),
))

# Add other milk types here (e.g., Skim Milk, Almond Milk, etc.) when they are defined