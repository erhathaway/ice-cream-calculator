from .base import ingredients_manager, Ingredient, Colorant

# Colorants

# Annatto
ingredients_manager.add(Ingredient(
    name='Annatto',
    category=['Colorant'],
    fat=0.0,
    carbs=0.0,
    protein=0.0,
    weight=0.0,
    colorant=Colorant(color='Orange', natural=True),
))

# Beet Juice
ingredients_manager.add(Ingredient(
    name='Beet Juice',
    category=['Colorant'],
    fat=0.0,
    carbs=9.6,
    protein=1.0,
    weight=0.0,
    colorant=Colorant(color='Red', natural=True),
))