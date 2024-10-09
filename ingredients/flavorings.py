from .base import ingredients_manager, Ingredient, Flavor, Colorant

# Flavorings

# Vanilla Extract
ingredients_manager.add(Ingredient(
    name='Vanilla Extract',
    category=['Flavoring'],
    fat=0.0,
    carbs=12.7,
    protein=0.1,
    weight=0.0,  # Adjust as needed
    calories=288.0,
    flavor_profiles=Flavor(flavor_notes={'Vanilla': 1.0}),
    colorant=Colorant(color='Brown', natural=True),
))

# Cocoa Powder
ingredients_manager.add(Ingredient(
    name='Cocoa Powder',
    category=['Flavoring'],
    fat=11.0,
    carbs=58.0,
    protein=19.0,
    weight=0.0,  # Adjust as needed
    calories=228.0,
    flavor_profiles=Flavor(flavor_notes={'Chocolate': 1.0, 'Bitter': 0.5}),
    colorant=Colorant(color='Dark Brown', natural=True),
))