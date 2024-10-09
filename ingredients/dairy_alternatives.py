from .base import (
    ingredients_manager, Ingredient, Flavor, PHModifier, PHBuffer,
    ViscosityModifier, MeltingRateModifier, Colorant, FreezingPointDepressant, EmulsifierProps
)

# Dairy alternatives

# Almond Milk
ingredients_manager.add(Ingredient(
    name='Almond Milk',
    category=['Dairy Alternative'],
    fat=2.5,
    carbs=1.0,
    protein=0.5,
    weight=0.0,
    calories=30.0,
    sweetness=0.1,
    fpdf=FreezingPointDepressant(fpdf=0.5),
    flavor_profiles=Flavor(flavor_notes={'Nutty': 1.0, 'Slightly Sweet': 0.5}),
    ph_modifier=PHModifier(ph_change=-0.1),
    ph_buffer=PHBuffer(buffering_capacity=0.8),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.0),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=1.0),
    colorant=Colorant(color='Off-White', natural=True),
    emulsifier_props=EmulsifierProps(
        emulsification=0.1,
    ),
    density=1.01,  # Density in g/ml
))

# Soy Milk
ingredients_manager.add(Ingredient(
    name='Soy Milk',
    category=['Dairy Alternative'],
    fat=1.8,
    carbs=3.0,
    protein=3.3,
    weight=0.0,
    calories=43.0,
    sweetness=0.1,
    fpdf=FreezingPointDepressant(fpdf=0.5),
    flavor_profiles=Flavor(flavor_notes={'Bean': 0.5, 'Creamy': 0.8}),
    ph_modifier=PHModifier(ph_change=-0.1),
    ph_buffer=PHBuffer(buffering_capacity=0.8),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.2),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=1.0),
    colorant=Colorant(color='Off-White', natural=True),
    emulsifier_props=EmulsifierProps(
        emulsification=0.2,
    ),
    density=1.02,
))

# Oat Milk
ingredients_manager.add(Ingredient(
    name='Oat Milk',
    category=['Dairy Alternative'],
    fat=1.5,
    carbs=6.0,
    protein=1.0,
    weight=0.0,
    calories=50.0,
    sweetness=0.2,
    fpdf=FreezingPointDepressant(fpdf=0.5),
    flavor_profiles=Flavor(flavor_notes={'Grain': 1.0, 'Slightly Sweet': 0.5}),
    ph_modifier=PHModifier(ph_change=-0.1),
    ph_buffer=PHBuffer(buffering_capacity=0.8),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.1),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=1.0),
    colorant=Colorant(color='Cream', natural=True),
    emulsifier_props=EmulsifierProps(
        emulsification=0.15,
    ),
    density=1.03,
))

# Coconut Milk
ingredients_manager.add(Ingredient(
    name='Coconut Milk',
    category=['Dairy Alternative'],
    fat=24.0,
    carbs=6.0,
    protein=2.0,
    weight=0.0,
    calories=230.0,
    sweetness=0.1,
    fpdf=FreezingPointDepressant(fpdf=0.5),
    flavor_profiles=Flavor(flavor_notes={'Coconut': 1.0, 'Creamy': 1.0}),
    ph_modifier=PHModifier(ph_change=-0.1),
    ph_buffer=PHBuffer(buffering_capacity=0.8),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.5),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=1.2),
    colorant=Colorant(color='White', natural=True),
    emulsifier_props=EmulsifierProps(
        emulsification=0.3,
    ),
    density=0.98,
))

# Rice Milk
ingredients_manager.add(Ingredient(
    name='Rice Milk',
    category=['Dairy Alternative'],
    fat=2.5,
    carbs=10.0,
    protein=0.5,
    weight=0.0,
    calories=60.0,
    sweetness=0.3,
    fpdf=FreezingPointDepressant(fpdf=0.5),
    flavor_profiles=Flavor(flavor_notes={'Sweet': 0.5, 'Grain': 0.8}),
    ph_modifier=PHModifier(ph_change=-0.1),
    ph_buffer=PHBuffer(buffering_capacity=0.8),
    viscosity_modifier=ViscosityModifier(viscosity_effect=0.9),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=1.0),
    colorant=Colorant(color='Off-White', natural=True),
    emulsifier_props=EmulsifierProps(
        emulsification=0.1,
    ),
    density=1.00,
))

# Cashew Milk
ingredients_manager.add(Ingredient(
    name='Cashew Milk',
    category=['Dairy Alternative'],
    fat=2.0,
    carbs=1.0,
    protein=1.0,
    weight=0.0,
    calories=25.0,
    sweetness=0.1,
    fpdf=FreezingPointDepressant(fpdf=0.5),
    flavor_profiles=Flavor(flavor_notes={'Nutty': 1.0, 'Creamy': 0.8}),
    ph_modifier=PHModifier(ph_change=-0.1),
    ph_buffer=PHBuffer(buffering_capacity=0.8),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.2),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=1.0),
    colorant=Colorant(color='Off-White', natural=True),
    emulsifier_props=EmulsifierProps(
        emulsification=0.15,
    ),
    density=1.01,
))

# Hemp Milk
ingredients_manager.add(Ingredient(
    name='Hemp Milk',
    category=['Dairy Alternative'],
    fat=3.0,
    carbs=0.0,
    protein=2.0,
    weight=0.0,
    calories=30.0,
    sweetness=0.1,
    fpdf=FreezingPointDepressant(fpdf=0.5),
    flavor_profiles=Flavor(flavor_notes={'Earthy': 1.0, 'Nutty': 0.5}),
    ph_modifier=PHModifier(ph_change=-0.1),
    ph_buffer=PHBuffer(buffering_capacity=0.8),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.1),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=1.0),
    colorant=Colorant(color='Off-White', natural=True),
    emulsifier_props=EmulsifierProps(
        emulsification=0.1,
    ),
    density=1.02,
))