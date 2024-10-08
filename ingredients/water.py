from .base import ingredients_manager, Ingredient, Flavor, Colorant

# Add Water
ingredients_manager.add(Ingredient(
    name='Water',
    category='Liquid',
    fat=0.0,
    carbs=0.0,
    protein=0.0,
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    colorant=Colorant(color='Colorless', natural=True),
))