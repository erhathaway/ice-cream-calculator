from .base import ingredients_manager, Ingredient, Flavor, ViscosityModifier, Colorant, GumAgentProps, PHModifier

ingredients_manager.add(Ingredient(
    name='Guar Gum',
    category='Stabilizer',
    carbs=80.0,
    protein=5.0,
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
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

ingredients_manager.add(Ingredient(
    name='Carrageenan',
    category='Stabilizer',
    carbs=80.0,
    protein=2.0,
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
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

ingredients_manager.add(Ingredient(
    name='Locust Bean Gum',
    category='Stabilizer',
    fat=1.0,
    carbs=80.0,
    protein=5.0,
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    viscosity_modifier=ViscosityModifier(viscosity_effect=12.0),
    colorant=Colorant(color='White to yellowish', natural=True),
    gum_agent_props=GumAgentProps(
        ideal_usage_min=0.05,
        ideal_usage_max=0.2,
        activation_temp=85.0,
        cold_soluble=False,
        interactions=['Guar Gum', 'Carrageenan'],
    ),
))

ingredients_manager.add(Ingredient(
    name='Xanthan Gum',
    category='Stabilizer',
    carbs=77.0,
    protein=7.0,
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    viscosity_modifier=ViscosityModifier(viscosity_effect=15.0),
    colorant=Colorant(color='Creamy White', natural=True),
    gum_agent_props=GumAgentProps(
        ideal_usage_min=0.05,
        ideal_usage_max=0.3,
        activation_temp=25.0,
        cold_soluble=True,
        interactions=['Guar Gum', 'Locust Bean Gum'],
    ),
))

ingredients_manager.add(Ingredient(
    name='Agar-Agar',
    category='Stabilizer',
    carbs=80.0,
    protein=6.0,
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    viscosity_modifier=ViscosityModifier(viscosity_effect=20.0),
    colorant=Colorant(color='Off-white', natural=True),
    gum_agent_props=GumAgentProps(
        ideal_usage_min=0.1,
        ideal_usage_max=0.5,
        activation_temp=85.0,
        cold_soluble=False,
        interactions=[],
    ),
))

ingredients_manager.add(Ingredient(
    name='Corn Starch',
    category='Thickener',
    fat=0.1,
    carbs=91.3,
    protein=0.3,
    viscosity_modifier=ViscosityModifier(viscosity_effect=5.0),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='White', natural=True),
))

ingredients_manager.add(Ingredient(
    name='Pectin',
    category='Thickener',
    carbs=90.0,
    viscosity_modifier=ViscosityModifier(viscosity_effect=8.0),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='Off-white', natural=True),
))