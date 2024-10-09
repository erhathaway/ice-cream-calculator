from .base import (
    ingredients_manager, Ingredient, FreezingPointDepressant, Flavor,
    MeltingRateModifier, Colorant, SweetenerProps
)

# Sweeteners and sugars

# Fructose
ingredients_manager.add(Ingredient(
    name='Fructose',
    category=['Sweetener'],
    fat=0.0,
    carbs=100.0,
    protein=0.0,
    weight=0.0,  # Adjust as needed
    calories=400.0,
    sweetness=1.7,
    fpdf=FreezingPointDepressant(fpdf=1.9),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.8),
    flavor_profiles=Flavor(flavor_notes={'Sweet': 1.0}),
    colorant=Colorant(color='White', natural=True),
    sweetener_props=SweetenerProps(
        glycemic_index=19.0,
        relative_sweetness=1.7,
        ideal_usage=10.0
    ),
))

# Dextrose
ingredients_manager.add(Ingredient(
    name='Dextrose',
    category=['Sweetener'],
    fat=0.0,
    carbs=100.0,
    protein=0.0,
    weight=0.0,  # Adjust as needed
    calories=400.0,
    sweetness=0.75,
    fpdf=FreezingPointDepressant(fpdf=1.9),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.85),
    flavor_profiles=Flavor(flavor_notes={'Sweet': 1.0}),
    colorant=Colorant(color='White', natural=True),
    sweetener_props=SweetenerProps(
        glycemic_index=100.0,
        relative_sweetness=0.75,
        ideal_usage=15.0
    ),
))

# Corn Syrup Solids
ingredients_manager.add(Ingredient(
    name='Corn Syrup Solids',
    category=['Sweetener'],
    fat=0.0,
    carbs=100.0,
    protein=0.0,
    weight=0.0,  # Adjust as needed
    calories=380.0,
    sweetness=0.4,
    fpdf=FreezingPointDepressant(fpdf=1.8),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.9),
    flavor_profiles=Flavor(flavor_notes={'Mildly Sweet': 1.0}),
    colorant=Colorant(color='White', natural=True),
    sweetener_props=SweetenerProps(
        glycemic_index=75.0,
        relative_sweetness=0.4,
        ideal_usage=15.0
    ),
))