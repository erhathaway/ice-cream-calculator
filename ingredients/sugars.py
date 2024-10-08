from .base import ingredients_manager, Ingredient, FreezingPointDepressant, Flavor, MeltingRateModifier, Colorant, SweetenerProperties

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

# Add Sugar (Sucrose)
ingredients_manager.add(Ingredient(
    name='Sugar',
    category='Sugar',
    carbs=100.0,
    sweetness=1.0,
    fpdf=FreezingPointDepressant(fpdf=1.0),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=1.0),
    flavor_profiles=Flavor(flavor_notes=['Sweet']),
    colorant=Colorant(color='White', natural=True),
    sweetener_props=SweetenerProperties(
        glycemic_index=65.0,
        relative_sweetness=1.0,
        ideal_usage=15.0
    ),
))