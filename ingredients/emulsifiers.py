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
    fpdf=FreezingPointDepressant(fpdf=0.0),
    flavor_profiles=Flavor(flavor_notes={'Rich': 1.0, 'Creamy': 1.0}),
    ph_buffer=PHBuffer(buffering_capacity=0.5),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.5),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=1.2),
    colorant=Colorant(color='Yellow', natural=True),
    emulsifier_props=EmulsifierProps(
        hlb_value=7.0,
        ideal_usage=0.5,
        emulsification=1.0,  # Moved emulsification here
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
    flavor_profiles=Flavor(flavor_notes={'Mild': 1.0, 'Nutty': 0.5}),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.2),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.95),
    colorant=Colorant(color='Light Brown', natural=True),
    emulsifier_props=EmulsifierProps(
        hlb_value=8.0,
        ideal_usage=0.3,
        emulsification=0.9,  # Added emulsification value
    ),
))

# Polysorbate 80
ingredients_manager.add(Ingredient(
    name='Polysorbate 80',
    category=['Emulsifier'],
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.0),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.9),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='Amber', natural=False),
    emulsifier_props=EmulsifierProps(
        hlb_value=15.0,
        ideal_usage=0.02,
        source='Synthetic',
        emulsification=1.0,  # Moved emulsification here
        interactions=[],
    ),
))

# Mono and Diglycerides
ingredients_manager.add(Ingredient(
    name='Mono and Diglycerides',
    category=['Emulsifier'],
    fat=100.0,
    weight=0.0,  # Adjust as needed
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.1),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.9),
    colorant=Colorant(color='Off-white', natural=False),
    emulsifier_props=EmulsifierProps(
        hlb_value=3.8,
        ideal_usage=0.2,
        emulsification=0.85,  # Moved emulsification here
        source='Synthetic',
        interactions=[],
    ),
))

# Polyglycerol Polyricinoleate
ingredients_manager.add(Ingredient(
    name='Polyglycerol Polyricinoleate',
    category=['Emulsifier'],
    fat=100.0,
    weight=0.0,  # Adjust as needed
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.0),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.95),
    colorant=Colorant(color='Amber', natural=False),
    emulsifier_props=EmulsifierProps(
        hlb_value=1.5,
        ideal_usage=0.03,
        emulsification=1.0,  # Moved emulsification here
        source='Synthetic',
        interactions=[],
    ),
))

# Sorbitan Monostearate
ingredients_manager.add(Ingredient(
    name='Sorbitan Monostearate',
    category=['Emulsifier'],
    fat=95.0,
    carbs=5.0,
    weight=0.0,  # Adjust as needed
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.1),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.9),
    colorant=Colorant(color='Yellowish', natural=False),
    emulsifier_props=EmulsifierProps(
        hlb_value=4.7,
        ideal_usage=0.5,
        emulsification=0.85,  # Moved emulsification here
        source='Synthetic',
        interactions=[],
    ),
))

# Sodium Stearoyl Lactylate
ingredients_manager.add(Ingredient(
    name='Sodium Stearoyl Lactylate',
    category=['Emulsifier'],
    fat=100.0,
    weight=0.0,  # Adjust as needed
    flavor_profiles=Flavor(flavor_notes=['Slightly Creamy']),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.2),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.92),
    colorant=Colorant(color='White to Cream', natural=False),
    emulsifier_props=EmulsifierProps(
        hlb_value=21.0,
        ideal_usage=0.4,
        emulsification=0.9,  # Moved emulsification here
        source='Synthetic',
        interactions=[],
    ),
))

# Sunflower Lecithin
ingredients_manager.add(Ingredient(
    name='Sunflower Lecithin',
    category=['Emulsifier'],
    fat=100.0,
    weight=0.0,  # Adjust as needed
    flavor_profiles=Flavor(flavor_notes=['Mild', 'Nutty']),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.2),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.95),
    colorant=Colorant(color='Light Brown', natural=True),
    emulsifier_props=EmulsifierProps(
        hlb_value=8.0,
        ideal_usage=0.3,
        emulsification=0.8,  # Added emulsification value
        source='Plant-based',
        interactions=[],
    ),
))

# Enzymatically Modified Lecithin
ingredients_manager.add(Ingredient(
    name='Enzymatically Modified Lecithin',
    category=['Emulsifier'],
    fat=99.0,
    carbs=1.0,
    weight=0.0,  # Adjust as needed
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.3),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.9),
    colorant=Colorant(color='Light Brown', natural=False),
    emulsifier_props=EmulsifierProps(
        hlb_value=11.0,
        ideal_usage=0.3,
        emulsification=0.95,  # Added emulsification value
        source='Plant-based',
        interactions=[],
    ),
))