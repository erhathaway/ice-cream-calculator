from .base import (
    ingredients_manager, Ingredient, Flavor, PHModifier, PHBuffer,
    ViscosityModifier, MeltingRateModifier, Colorant, FreezingPointDepressant,
    EmulsifierProps
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
    emulsifier_props=EmulsifierProps(
        emulsification=0.2
    ),
    fpdf=FreezingPointDepressant(fpdf=0.5),
    flavor_profiles=Flavor(flavor_notes={'Coconut': 1.0}),
    ph_modifier=PHModifier(ph_change=-0.1),
    ph_buffer=PHBuffer(buffering_capacity=0.8),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.5),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.9),
    colorant=Colorant(color='White', natural=True),
))

ingredients_manager.add(Ingredient(
    name='Cashew Milk Concentrate',
    category=['Dairy Alternative'],
    fat=26.0,  # Approximate value per 100g
    carbs=20.0,  # Approximate value per 100g
    protein=8.0,  # Approximate value per 100g
    weight=0.0,  # Adjust as needed
    calories=350.0,  # Approximate value per 100g
    sweetness=0.2,  # Adjust based on taste
    emulsifier_props=EmulsifierProps(
        emulsification=0.3
    ),
    fpdf=FreezingPointDepressant(fpdf=0.5),
    flavor_profiles=Flavor(flavor_notes={'Cashew': 1.0}),
    ph_modifier=PHModifier(ph_change=-0.1),
    ph_buffer=PHBuffer(buffering_capacity=0.7),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.3),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.9),
    colorant=Colorant(color='Off-White', natural=True),
))

ingredients_manager.add(Ingredient(
    name='Macadamia Milk Concentrate',
    category=['Dairy Alternative'],
    fat=32.0,  # Approximate value per 100g
    carbs=14.0,  # Approximate value per 100g
    protein=7.0,  # Approximate value per 100g
    weight=0.0,  # Adjust as needed
    calories=400.0,  # Approximate value per 100g
    sweetness=0.2,  # Adjust based on taste
    emulsifier_props=EmulsifierProps(
        emulsification=0.3
    ),
    fpdf=FreezingPointDepressant(fpdf=0.5),
    flavor_profiles=Flavor(flavor_notes={'Macadamia': 1.0}),
    ph_modifier=PHModifier(ph_change=-0.1),
    ph_buffer=PHBuffer(buffering_capacity=0.7),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.3),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.9),
    colorant=Colorant(color='Creamy White', natural=True),
))