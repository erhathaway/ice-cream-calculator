from .base import ingredients_manager, Ingredient, Flavor, Colorant

# Proteins

# Whey Protein Isolate
ingredients_manager.add(Ingredient(
    name='Whey Protein Isolate',
    category=['Protein'],
    fat=1.0,
    carbs=3.5,
    protein=90.0,
    weight=0.0,
    calories=360.0,
    flavor_profiles=Flavor(flavor_notes={'Milky': 1.0}),
    colorant=Colorant(color='White', natural=True),
    density=0.33,
))