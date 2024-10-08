from .base import ingredients_manager, Ingredient, Flavor, ViscosityModifier, MeltingRateModifier, Colorant

# Add Vegetable Oil
ingredients_manager.add(Ingredient(
    name='Vegetable Oil',
    category='Fat',
    fat=100.0,
    carbs=0.0,
    protein=0.0,
    flavor_profiles=Flavor(flavor_notes=['Neutral']),
    viscosity_modifier=ViscosityModifier(viscosity_effect=0.8),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.9),
    colorant=Colorant(color='Light Yellow', natural=True),
))