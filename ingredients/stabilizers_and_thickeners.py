from .base import (
    ingredients_manager, Ingredient, Flavor, ViscosityModifier,
    Colorant, GumAgentProps, PHModifier
)

# Stabilizers and thickeners

# Guar Gum
ingredients_manager.add(Ingredient(
    name='Guar Gum',
    category=['Stabilizer', 'Thickener'],
    fat=0.0,
    carbs=80.0,
    protein=5.0,
    weight=0.0,  # Adjust as needed
    calories=200.0,
    flavor_profiles=Flavor(flavor_notes={'Neutral': 1.0}),
    viscosity_modifier=ViscosityModifier(viscosity_effect=10.0),
    colorant=Colorant(color='Off-white', natural=True),
    ph_modifier=PHModifier(ph_change=0.0),
    gum_agent_props=GumAgentProps(
        ideal_usage_min=0.1,
        ideal_usage_max=0.5,
        activation_temp=25.0,
        cold_soluble=True,
        interactions=['Locust Bean Gum', 'Xanthan Gum'],
    ),
))

# Carrageenan
ingredients_manager.add(Ingredient(
    name='Carrageenan',
    category=['Stabilizer', 'Thickener'],
    fat=0.0,
    carbs=80.0,
    protein=2.0,
    weight=0.0,  # Adjust as needed
    calories=200.0,
    flavor_profiles=Flavor(flavor_notes={'Neutral': 1.0}),
    viscosity_modifier=ViscosityModifier(viscosity_effect=10.0),
    colorant=Colorant(color='Off-white', natural=True),
    gum_agent_props=GumAgentProps(
        ideal_usage_min=0.01,
        ideal_usage_max=0.05,
        activation_temp=60.0,
        cold_soluble=False,
        interactions=['Locust Bean Gum'],
    ),
))

# Locust Bean Gum
ingredients_manager.add(Ingredient(
    name='Locust Bean Gum',
    category=['Stabilizer', 'Thickener'],
    fat=1.0,
    carbs=80.0,
    protein=5.0,
    weight=0.0,  # Adjust as needed
    calories=200.0,
    flavor_profiles=Flavor(flavor_notes={'Neutral': 1.0}),
    viscosity_modifier=ViscosityModifier(viscosity_effect=12.0),
    colorant=Colorant(color='White to Yellowish', natural=True),
    gum_agent_props=GumAgentProps(
        ideal_usage_min=0.05,
        ideal_usage_max=0.2,
        activation_temp=85.0,
        cold_soluble=False,
        interactions=['Guar Gum', 'Carrageenan'],
    ),
))