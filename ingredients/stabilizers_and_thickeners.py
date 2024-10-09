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
    weight=0.0,
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
    density=0.8,
))

# Carrageenan
ingredients_manager.add(Ingredient(
    name='Carrageenan',
    category=['Stabilizer', 'Thickener'],
    fat=0.0,
    carbs=80.0,
    protein=2.0,
    weight=0.0,
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
    density=0.8,
))

# Locust Bean Gum
ingredients_manager.add(Ingredient(
    name='Locust Bean Gum',
    category=['Stabilizer', 'Thickener'],
    fat=1.0,
    carbs=80.0,
    protein=5.0,
    weight=0.0,
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
    density=0.8,
))

# Xanthan Gum
ingredients_manager.add(Ingredient(
    name='Xanthan Gum',
    category=['Stabilizer', 'Thickener'],
    fat=0.0,
    carbs=78.0,
    protein=7.0,
    weight=0.0,
    calories=200.0,
    flavor_profiles=Flavor(flavor_notes={'Neutral': 1.0}),
    viscosity_modifier=ViscosityModifier(viscosity_effect=18.0),
    colorant=Colorant(color='Off-white to cream', natural=True),
    ph_modifier=PHModifier(ph_change=0.0),
    gum_agent_props=GumAgentProps(
        ideal_usage_min=0.02,
        ideal_usage_max=0.1,
        activation_temp=25.0,
        cold_soluble=True,
        interactions=['Guar Gum', 'Locust Bean Gum'],
    ),
    density=0.8,
))

# Agar Agar
ingredients_manager.add(Ingredient(
    name='Agar Agar',
    category=['Gelling Agent', 'Thickener'],
    fat=0.0,
    carbs=80.0,
    protein=2.0,
    weight=0.0,
    calories=208.0,
    flavor_profiles=Flavor(flavor_notes={'Neutral': 1.0}),
    viscosity_modifier=ViscosityModifier(viscosity_effect=20.0),
    colorant=Colorant(color='Off-white', natural=True),
    ph_modifier=PHModifier(ph_change=0.0),
    gum_agent_props=GumAgentProps(
        ideal_usage_min=0.1,
        ideal_usage_max=1.0,
        activation_temp=85.0,
        cold_soluble=False,
        interactions=['Pectin'],
    ),
    density=0.8,
))

# Pectin
ingredients_manager.add(Ingredient(
    name='Pectin',
    category=['Stabilizer', 'Thickener', 'Gelling Agent'],
    fat=0.0,
    carbs=90.0,
    protein=0.0,
    weight=0.0,
    calories=240.0,
    flavor_profiles=Flavor(flavor_notes={'Neutral': 1.0}),
    viscosity_modifier=ViscosityModifier(viscosity_effect=15.0),
    colorant=Colorant(color='Off-white', natural=True),
    ph_modifier=PHModifier(ph_change=-0.2),
    gum_agent_props=GumAgentProps(
        ideal_usage_min=0.2,
        ideal_usage_max=1.5,
        activation_temp=85.0,
        cold_soluble=False,
        interactions=['Sugar', 'Acid'],
    ),
    density=0.8,
))

# Gelatin
ingredients_manager.add(Ingredient(
    name='Gelatin',
    category=['Gelling Agent', 'Thickener'],
    fat=0.0,
    carbs=0.0,
    protein=85.0,
    weight=0.0,
    calories=340.0,
    flavor_profiles=Flavor(flavor_notes={'Neutral': 1.0}),
    viscosity_modifier=ViscosityModifier(viscosity_effect=25.0),
    colorant=Colorant(color='Off-white', natural=True),
    ph_modifier=PHModifier(ph_change=0.0),
    gum_agent_props=GumAgentProps(
        ideal_usage_min=0.5,
        ideal_usage_max=2.0,
        activation_temp=35.0,
        cold_soluble=False,
        interactions=['Sugar'],
    ),
    density=0.8,
))

# Konjac Gum
ingredients_manager.add(Ingredient(
    name='Konjac Gum',
    category=['Stabilizer', 'Thickener'],
    fat=0.0,
    carbs=80.0,
    protein=2.0,
    weight=0.0,
    calories=200.0,
    flavor_profiles=Flavor(flavor_notes={'Neutral': 1.0}),
    viscosity_modifier=ViscosityModifier(viscosity_effect=22.0),
    colorant=Colorant(color='Off-white', natural=True),
    ph_modifier=PHModifier(ph_change=0.0),
    gum_agent_props=GumAgentProps(
        ideal_usage_min=0.05,
        ideal_usage_max=0.2,
        activation_temp=25.0,
        cold_soluble=True,
        interactions=['Carrageenan', 'Xanthan Gum'],
    ),
    density=0.8,
))

# Tara Gum
ingredients_manager.add(Ingredient(
    name='Tara Gum',
    category=['Stabilizer', 'Thickener'],
    fat=0.0,
    carbs=80.0,
    protein=5.0,
    weight=0.0,
    calories=200.0,
    flavor_profiles=Flavor(flavor_notes={'Neutral': 1.0}),
    viscosity_modifier=ViscosityModifier(viscosity_effect=17.0),
    colorant=Colorant(color='White to cream', natural=True),
    ph_modifier=PHModifier(ph_change=0.0),
    gum_agent_props=GumAgentProps(
        ideal_usage_min=0.05,
        ideal_usage_max=0.3,
        activation_temp=85.0,
        cold_soluble=False,
        interactions=['Guar Gum', 'Locust Bean Gum'],
    ),
    density=0.8,
))