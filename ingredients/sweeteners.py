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

# Maple Syrup
ingredients_manager.add(Ingredient(
    name='Maple Syrup',
    category=['Sweetener'],
    fat=0.0,
    carbs=67.0,
    protein=0.0,
    weight=0.0,
    calories=260.0,
    sweetness=1.0,
    sweetener_props=SweetenerProps(glycemic_index=54.0, relative_sweetness=1.0, ideal_usage=10.0),
    fpdf=FreezingPointDepressant(fpdf=1.9),
    flavor_profiles=Flavor(flavor_notes={'Maple': 1.0, 'Sweet': 1.0}),
    colorant=Colorant(color='Amber', natural=True),
))

# Agave Syrup
ingredients_manager.add(Ingredient(
    name='Agave Syrup',
    category=['Sweetener'],
    fat=0.0,
    carbs=76.0,
    protein=0.0,
    weight=0.0,
    calories=310.0,
    sweetness=1.4,
    sweetener_props=SweetenerProps(glycemic_index=19.0, relative_sweetness=1.4, ideal_usage=7.0),
    fpdf=FreezingPointDepressant(fpdf=2.0),
    flavor_profiles=Flavor(flavor_notes={'Sweet': 1.0, 'Neutral': 0.5}),
    colorant=Colorant(color='Light Amber', natural=True),
))

# Dark Brown Sugar
ingredients_manager.add(Ingredient(
    name='Dark Brown Sugar',
    category=['Sweetener'],
    fat=0.0,
    carbs=97.0,
    protein=0.0,
    weight=0.0,
    calories=380.0,
    sweetness=1.0,
    sweetener_props=SweetenerProps(glycemic_index=64.0, relative_sweetness=1.0, ideal_usage=10.0),
    fpdf=FreezingPointDepressant(fpdf=1.9),
    flavor_profiles=Flavor(flavor_notes={'Sweet': 1.0, 'Molasses': 0.8}),
    colorant=Colorant(color='Dark Brown', natural=True),
))

# Light Brown Sugar
ingredients_manager.add(Ingredient(
    name='Light Brown Sugar',
    category=['Sweetener'],
    fat=0.0,
    carbs=97.0,
    protein=0.0,
    weight=0.0,
    calories=380.0,
    sweetness=1.0,
    sweetener_props=SweetenerProps(glycemic_index=64.0, relative_sweetness=1.0, ideal_usage=10.0),
    fpdf=FreezingPointDepressant(fpdf=1.9),
    flavor_profiles=Flavor(flavor_notes={'Sweet': 1.0, 'Molasses': 0.5}),
    colorant=Colorant(color='Light Brown', natural=True),
))

# Stevia
ingredients_manager.add(Ingredient(
    name='Stevia',
    category=['Sweetener'],
    fat=0.0,
    carbs=0.0,
    protein=0.0,
    weight=0.0,
    calories=0.0,
    sweetness=200.0,
    sweetener_props=SweetenerProps(glycemic_index=0.0, relative_sweetness=200.0, ideal_usage=0.05),
    flavor_profiles=Flavor(flavor_notes={'Sweet': 1.0, 'Bitter': 0.2}),
    colorant=Colorant(color='White', natural=True),
))

# White Sugar
ingredients_manager.add(Ingredient(
    name='White Sugar',
    category=['Sweetener'],
    fat=0.0,
    carbs=100.0,
    protein=0.0,
    weight=0.0,
    calories=387.0,
    sweetness=1.0,
    sweetener_props=SweetenerProps(glycemic_index=65.0, relative_sweetness=1.0, ideal_usage=10.0),
    fpdf=FreezingPointDepressant(fpdf=1.9),
    flavor_profiles=Flavor(flavor_notes={'Sweet': 1.0}),
    colorant=Colorant(color='White', natural=True),
))