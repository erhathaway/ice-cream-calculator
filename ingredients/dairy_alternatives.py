from .base import (
    ingredients_manager, Ingredient, Flavor, PHModifier, PHBuffer,
    ViscosityModifier, MeltingRateModifier, Colorant, FreezingPointDepressant
)

# Dairy alternative ingredients
ingredients_manager.add(Ingredient(
    name='Coconut Milk',
    category=['Dairy Alternative'],
    fat=24.0,
    carbs=6.0,
    protein=2.0,
    weight=0.0,  # Adjust as needed
    calories=230.0,  # per 100g
    sweetness=0.1,
    emulsification=0.2,
    fpdf=FreezingPointDepressant(fpdf=0.5),
    flavor_profiles=Flavor(flavor_notes={'Coconut': 1.0}),
    ph_modifier=PHModifier(ph_change=-0.1),
    ph_buffer=PHBuffer(buffering_capacity=0.8),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.5),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.9),
    colorant=Colorant(color='White', natural=True),
))