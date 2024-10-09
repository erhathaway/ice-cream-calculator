from .base import (
    ingredients_manager, Ingredient, Flavor, ViscosityModifier,
    MeltingRateModifier, Colorant
)

# Fats and oils

# Vegetable Oil
ingredients_manager.add(Ingredient(
    name='Vegetable Oil',
    category=['Fat'],
    fat=100.0,
    carbs=0.0,
    protein=0.0,
    weight=0.0,
    calories=884.0,
    flavor_profiles=Flavor(flavor_notes={'Neutral': 1.0}),
    viscosity_modifier=ViscosityModifier(viscosity_effect=0.8),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.9),
    colorant=Colorant(color='Light Yellow', natural=True),
    density=0.92,  # Density in g/ml
))