from .base import ingredients_manager, Ingredient, FreezingPointDepressant, Flavor, MeltingRateModifier, Colorant, SweetenerProperties

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