from ingredients import Ingredient, ingredients_manager, FreezingPointDepressant, Flavor, GumAgentProps, PHModifier, PHBuffer, ViscosityModifier, MeltingRateModifier, Colorant, EmulsifierProperties, SweetenerProperties
# Adding ingredients to the manager
# Dairy Ingredients
ingredients_manager.add(Ingredient(
    name='Whole Milk',
    category='Dairy',
    fat=3.25,
    carbs=4.8,
    protein=3.15,
    sweetness=0.1,
    emulsification=0.2,
    fpdf=FreezingPointDepressant(fpdf=0.5),
    flavor_profiles=Flavor(flavor_notes=['Creamy', 'Slightly Sweet']),
    ph_modifier=PHModifier(ph_change=-0.1),
    ph_buffer=PHBuffer(buffering_capacity=0.8),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.0),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=1.0),
    colorant=Colorant(color='White', natural=True),
))

# Additional pH Buffers
ingredients_manager.add(Ingredient(
    name='Sodium Citrate',
    category='pH Buffer',
    flavor_profiles=Flavor(flavor_notes=['Slightly Salty']),
    ph_buffer=PHBuffer(buffering_capacity=1.0),
    colorant=Colorant(color='White', natural=True),
))

ingredients_manager.add(Ingredient(
    name='Citric Acid',
    category='pH Buffer',
    ph_modifier=PHModifier(ph_change=-0.5),
    ph_buffer=PHBuffer(buffering_capacity=0.8),
    flavor_profiles=Flavor(flavor_notes=['Sour']),
    colorant=Colorant(color='White', natural=True),
))

ingredients_manager.add(Ingredient(
    name='Potassium Phosphate',
    category='pH Buffer',
    ph_buffer=PHBuffer(buffering_capacity=1.0),
    flavor_profiles=Flavor(flavor_notes=['Slightly Bitter']),
    colorant=Colorant(color='White', natural=False),
))

ingredients_manager.add(Ingredient(
    name='Sodium Bicarbonate',
    category='pH Buffer',
    ph_modifier=PHModifier(ph_change=0.5),
    ph_buffer=PHBuffer(buffering_capacity=0.7),
    flavor_profiles=Flavor(flavor_notes=['Slightly Salty']),
    colorant=Colorant(color='White', natural=True),
))

ingredients_manager.add(Ingredient(
    name='Calcium Carbonate',
    category='pH Buffer',
    ph_modifier=PHModifier(ph_change=0.6),
    ph_buffer=PHBuffer(buffering_capacity=0.9),
    flavor_profiles=Flavor(flavor_notes=['Chalky']),
    colorant=Colorant(color='White', natural=True),
))

# Additional Viscosity Modifiers
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
    name='Carrageenan',
    category='Thickener',
    carbs=80.0,
    protein=2.0,
    viscosity_modifier=ViscosityModifier(viscosity_effect=10.0),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='Off-white', natural=True),
))

ingredients_manager.add(Ingredient(
    name='Locust Bean Gum',
    category='Thickener',
    fat=1.0,
    carbs=80.0,
    protein=5.0,
    viscosity_modifier=ViscosityModifier(viscosity_effect=12.0),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='Off-white', natural=True),
))

ingredients_manager.add(Ingredient(
    name='Pectin',
    category='Thickener',
    carbs=90.0,
    viscosity_modifier=ViscosityModifier(viscosity_effect=8.0),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='Off-white', natural=True),
))

ingredients_manager.add(Ingredient(
    name='Agar-Agar',
    category='Thickener',
    carbs=80.0,
    protein=6.0,
    viscosity_modifier=ViscosityModifier(viscosity_effect=15.0),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='Off-white', natural=True),
))

# Additional Melting Rate Modifiers
ingredients_manager.add(Ingredient(
    name='Propylene Glycol',
    category='Melting Rate Modifier',
    sweetness=0.6,
    fpdf=FreezingPointDepressant(fpdf=1.6),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.7),
    flavor_profiles=Flavor(flavor_notes=['Slightly Sweet']),
    colorant=Colorant(color='Colorless', natural=False),
))

ingredients_manager.add(Ingredient(
    name='Glycerol (Glycerin)',
    category='Melting Rate Modifier',
    sweetness=0.6,
    fpdf=FreezingPointDepressant(fpdf=1.92),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.8),
    flavor_profiles=Flavor(flavor_notes=['Sweet']),
    colorant=Colorant(color='Colorless', natural=False),
))

ingredients_manager.add(Ingredient(
    name='Fructose',
    category='Sugar',
    carbs=100.0,
    sweetness=1.7,
    fpdf=FreezingPointDepressant(fpdf=1.9),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.8),
    flavor_profiles=Flavor(flavor_notes=['Sweet']),
    colorant=Colorant(color='White', natural=True),
    sweetener_props=SweetenerProperties(
        glycemic_index=19.0,
        relative_sweetness=1.7,
        ideal_usage=10.0
    ),
))

ingredients_manager.add(Ingredient(
    name='Dextrose',
    category='Sugar',
    carbs=100.0,
    sweetness=0.75,
    fpdf=FreezingPointDepressant(fpdf=1.9),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.85),
    flavor_profiles=Flavor(flavor_notes=['Sweet']),
    colorant=Colorant(color='White', natural=True),
    sweetener_props=SweetenerProperties(
        glycemic_index=100.0,
        relative_sweetness=0.75,
        ideal_usage=15.0
    ),
))

ingredients_manager.add(Ingredient(
    name='Corn Syrup Solids',
    category='Sweetener',
    carbs=100.0,
    sweetness=0.4,
    fpdf=FreezingPointDepressant(fpdf=1.8),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.9),
    flavor_profiles=Flavor(flavor_notes=['Mildly Sweet']),
    colorant=Colorant(color='White', natural=True),
    sweetener_props=SweetenerProperties(
        glycemic_index=75.0,
        relative_sweetness=0.4,
        ideal_usage=15.0
    ),
))

ingredients_manager.add(Ingredient(
    name='Maltodextrin',
    category='Sweetener',
    carbs=95.0,
    sweetness=0.1,
    fpdf=FreezingPointDepressant(fpdf=1.5),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.95),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='White', natural=True),
    sweetener_props=SweetenerProperties(
        glycemic_index=85.0,
        relative_sweetness=0.1,
        ideal_usage=10.0
    ),
))

# Emulsifiers
ingredients_manager.add(Ingredient(
    name='Egg Yolks',
    category='Emulsifier',
    fat=26.5,
    carbs=3.6,
    protein=15.9,
    emulsification=1.0,
    fpdf=FreezingPointDepressant(fpdf=0.0),
    flavor_profiles=Flavor(flavor_notes=['Rich', 'Creamy']),
    ph_buffer=PHBuffer(buffering_capacity=0.5),
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.5),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=1.2),
    colorant=Colorant(color='Yellow', natural=True),
    emulsifier_props=EmulsifierProperties(
        ideal_usage=0.5,
        source='Animal-based',
        hlb_value=7.0,
        interactions=[],
    ),
))

ingredients_manager.add(Ingredient(
    name='Soy Lecithin',
    category='Emulsifier',
    fat=100.0,
    emulsification=0.9,
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.2),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.95),
    flavor_profiles=Flavor(flavor_notes=['Mild', 'Nutty']),
    colorant=Colorant(color='Light Brown', natural=True),
    emulsifier_props=EmulsifierProperties(
        ideal_usage=0.3,
        source='Plant-based',
        hlb_value=8.0,
        interactions=[],
    ),
))

ingredients_manager.add(Ingredient(
    name='Polysorbate 80',
    category='Emulsifier',
    emulsification=1.0,
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.0),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.9),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='Amber', natural=False),
    emulsifier_props=EmulsifierProperties(
        ideal_usage=0.02,
        source='Synthetic',
        hlb_value=15.0,
        interactions=[],
    ),
))

ingredients_manager.add(Ingredient(
    name='Mono and Diglycerides',
    category='Emulsifier',
    fat=100.0,
    emulsification=0.85,
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.1),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.9),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='Off-white', natural=False),
    emulsifier_props=EmulsifierProperties(
        ideal_usage=0.2,
        source='Synthetic',
        hlb_value=3.8,
        interactions=[],
    ),
))

ingredients_manager.add(Ingredient(
    name='Polyglycerol Polyricinoleate',
    category='Emulsifier',
    fat=100.0,
    emulsification=1.0,
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.0),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.95),
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='Amber', natural=False),
    emulsifier_props=EmulsifierProperties(
        ideal_usage=0.03,
        source='Synthetic',
        hlb_value=1.5,
        interactions=[],
    ),
))

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
    emulsifier_props=EmulsifierProperties(
        ideal_usage=0.5,
        source='Synthetic',
        hlb_value=4.7,
        interactions=[],
    ),
))

ingredients_manager.add(Ingredient(
    name='Sodium Stearoyl Lactylate',
    category='Emulsifier',
    fat=100.0,
    emulsification=0.9,
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.2),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.92),
    flavor_profiles=Flavor(flavor_notes=['Slightly Creamy']),
    colorant=Colorant(color='White to Cream', natural=False),
    emulsifier_props=EmulsifierProperties(
        ideal_usage=0.4,
        source='Synthetic',
        hlb_value=21.0,
        interactions=[],
    ),
))

ingredients_manager.add(Ingredient(
    name='Sunflower Lecithin',
    category='Emulsifier',
    fat=100.0,
    emulsification=0.8,
    viscosity_modifier=ViscosityModifier(viscosity_effect=1.2),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.95),
    flavor_profiles=Flavor(flavor_notes=['Mild', 'Nutty']),
    colorant=Colorant(color='Light Brown', natural=True),
    emulsifier_props=EmulsifierProperties(
        ideal_usage=0.3,
        source='Plant-based',
        hlb_value=8.0,
        interactions=[],
    ),
))

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
    emulsifier_props=EmulsifierProperties(
        ideal_usage=0.3,
        source='Plant-based',
        hlb_value=11.0,
        interactions=[],
    ),
))

# Gum Agents
ingredients_manager.add(Ingredient(
    name='Guar Gum',
    category='Stabilizer',
    carbs=80.0,
    protein=5.0,
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    viscosity_modifier=ViscosityModifier(viscosity_effect=10.0),
    colorant=Colorant(color='Off-white', natural=True),
    ph_modifier=PHModifier(ph_change=0.0),
    gum_agent_props=GumAgentProperties(
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
    gum_agent_props=GumAgentProperties(
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
    gum_agent_props=GumAgentProperties(
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
    gum_agent_props=GumAgentProperties(
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
    gum_agent_props=GumAgentProperties(
        ideal_usage_min=0.1,
        ideal_usage_max=0.5,
        activation_temp=85.0,
        cold_soluble=False,
        interactions=[],
    ),
))

# Update dictionaries if needed
ingredients_dict = {ingredient.name: ingredient for ingredient in ingredients_manager.ingredients}
