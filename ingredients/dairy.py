from .base import (
    ingredients_manager, Ingredient, Flavor, PHModifier, PHBuffer,
    ViscosityModifier, MeltingRateModifier, Colorant, FreezingPointDepressant, EmulsifierProps
)

# Dairy ingredients
ingredients_manager.add(Ingredient(
    name='Whole Milk',
    category=['Dairy'],
    fat=3.25,
    carbs=4.8,
    protein=3.15,
    weight=0.0,
    calories=60.0,
    sweetness=0.1,
    fpdf=FreezingPointDepressant(fpdf=0.5),
    flavor_profiles=Flavor(flavor_notes={'Creamy': 1.0, 'Slightly Sweet': 0.5}),
    ph_modifier=PHModifier(ph_change=-0.1),
    ph_buffer=PHBuffer(buffering_capacity=0.8),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.0),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=1.0),
    colorant=Colorant(color='White', natural=True),
    emulsifier_props=EmulsifierProps(
        emulsification=0.2,
    ),
    density=1.03,  # Density in g/ml
))