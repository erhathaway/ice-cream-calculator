from .base import (
    ingredients_manager, Ingredient, Flavor, ViscosityModifier,
    MeltingRateModifier, Colorant, EmulsifierProps, FreezingPointDepressant,
    PHBuffer
)

# Emulsifiers

# Egg Yolks
ingredients_manager.add(Ingredient(
    name='Egg Yolks',
    category=['Emulsifier'],
    fat=26.5,
    carbs=3.6,
    protein=15.9,
    weight=0.0,  # Adjust as needed
    calories=322.0,
    emulsification=1.0,
    fpdf=FreezingPointDepressant(fpdf=0.0),
    flavor_profiles=Flavor(flavor_notes={'Rich': 1.0, 'Creamy': 1.0}),
    ph_buffer=PHBuffer(buffering_capacity=0.5),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.5),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=1.2),
    colorant=Colorant(color='Yellow', natural=True),
    emulsifier_props=EmulsifierProps(
        hld_value=7.0,
        ideal_usage=0.5,
    ),
))

# Soy Lecithin
ingredients_manager.add(Ingredient(
    name='Soy Lecithin',
    category=['Emulsifier'],
    fat=100.0,
    carbs=0.0,
    protein=0.0,
    weight=0.0,  # Adjust as needed
    calories=884.0,
    emulsification=0.9,
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.2),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.95),
    flavor_profiles=Flavor(flavor_notes={'Mild': 1.0, 'Nutty': 0.5}),
    colorant=Colorant(color='Light Brown', natural=True),
    emulsifier_props=EmulsifierProps(
        hld_value=8.0,
        ideal_usage=0.3,
    ),
))

# Polysorbate 80
ingredients_manager.add(Ingredient(
    name='Polysorbate 80',
    category='Emulsifier',
    emulsification=1.0,
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.0),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.9),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='Amber', natural=False),
    emulsifier_props=EmulsifierProps(
        ideal_usage=0.02,
        source='Synthetic',
        hlb_value=15.0,
        interactions=[],
    ),
))

# Mono and Diglycerides
ingredients_manager.add(Ingredient(
    name='Mono and Diglycerides',
    category='Emulsifier',
    fat=100.0,
    emulsification=0.85,
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.1),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.9),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='Off-white', natural=False),
    emulsifier_props=EmulsifierProps(
        ideal_usage=0.2,
        source='Synthetic',
        hlb_value=3.8,
        interactions=[],
    ),
))

# Polyglycerol Polyricinoleate
ingredients_manager.add(Ingredient(
    name='Polyglycerol Polyricinoleate',
    category='Emulsifier',
    fat=100.0,
    emulsification=1.0,
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.0),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.95),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='Amber', natural=False),
    emulsifier_props=EmulsifierProps(
        ideal_usage=0.03,
        source='Synthetic',
        hlb_value=1.5,
        interactions=[],
    ),
))

# Sorbitan Monostearate
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
    emulsifier_props=EmulsifierProps(
        ideal_usage=0.5,
        source='Synthetic',
        hlb_value=4.7,
        interactions=[],
    ),
))

# Sodium Stearoyl Lactylate
ingredients_manager.add(Ingredient(
    name='Sodium Stearoyl Lactylate',
    category='Emulsifier',
    fat=100.0,
    emulsification=0.9,
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.2),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.92),
    flavor_profiles=Flavor(flavor_notes=['Slightly Creamy']),
    colorant=Colorant(color='White to Cream', natural=False),
    emulsifier_props=EmulsifierProps(
        ideal_usage=0.4,
        source='Synthetic',
        hlb_value=21.0,
        interactions=[],
    ),
))

# Sunflower Lecithin
ingredients_manager.add(Ingredient(
    name='Sunflower Lecithin',
    category='Emulsifier',
    fat=100.0,
    emulsification=0.8,
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.2),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.95),
    flavor_profiles=Flavor(flavor_notes=['Mild', 'Nutty']),
    colorant=Colorant(color='Light Brown', natural=True),
    emulsifier_props=EmulsifierProps(
        ideal_usage=0.3,
        source='Plant-based',
        hlb_value=8.0,
        interactions=[],
    ),
))

# Enzymatically Modified Lecithin
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
    emulsifier_props=EmulsifierProps(
        ideal_usage=0.3,
        source='Plant-based',
        hlb_value=11.0,
        interactions=[],
    ),
))