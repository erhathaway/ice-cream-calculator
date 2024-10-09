from .base import (
    ingredients_manager, Ingredient, Flavor, PHModifier, PHBuffer,
    ViscosityModifier, MeltingRateModifier, Colorant, FreezingPointDepressant
)

# Dairy ingredients
ingredients_manager.add(Ingredient(
    name='Whole Milk',
    category=['Dairy'],
    fat=3.25,
    carbs=4.8,
    protein=3.15,
    weight=0.0,  # Adjust as needed
    calories=60.0,  # per 100g
    sweetness=0.1,
    emulsification=0.2,
    fpdf=FreezingPointDepressant(fpdf=0.5),
    flavor_profiles=Flavor(flavor_notes={'Creamy': 1.0, 'Slightly Sweet': 0.5}),
    ph_modifier=PHModifier(ph_change=-0.1),
    ph_buffer=PHBuffer(buffering_capacity=0.8),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.0),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=1.0),
    colorant=Colorant(color='White', natural=True),
))