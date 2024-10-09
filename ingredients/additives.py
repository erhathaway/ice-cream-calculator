from .base import (
    ingredients_manager, Ingredient, Flavor, Colorant,
    FreezingPointDepressant, MeltingRateModifier, PHModifier,
    PHBuffer
)

# Additives

# Propylene Glycol
ingredients_manager.add(Ingredient(
    name='Propylene Glycol',
    category=['Additive', 'Melting Rate Modifier'],
    fat=0.0,
    carbs=0.0,
    protein=0.0,
    weight=0.0,
    sweetness=0.6,
    fpdf=FreezingPointDepressant(fpdf=1.6),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.7),
    flavor_profiles=Flavor(flavor_notes={'Slightly Sweet': 1.0}),
    colorant=Colorant(color='Colorless', natural=False),
))

# Glycerol (Glycerin)
ingredients_manager.add(Ingredient(
    name='Glycerol',
    category=['Additive', 'Melting Rate Modifier'],
    fat=0.0,
    carbs=0.0,
    protein=0.0,
    weight=0.0,
    sweetness=0.6,
    fpdf=FreezingPointDepressant(fpdf=1.92),
    melting_rate_modifier=MeltingRateModifier(melting_rate_effect=0.8),
    flavor_profiles=Flavor(flavor_notes={'Sweet': 1.0}),
    colorant=Colorant(color='Colorless', natural=False),
))

# Citric Acid
ingredients_manager.add(Ingredient(
    name='Citric Acid',
    category=['Additive', 'Acidulant'],
    fat=0.0,
    carbs=0.0,
    protein=0.0,
    weight=0.0,
    calories=0.0,
    ph_modifier=PHModifier(ph_change=-2.5),
    flavor_profiles=Flavor(flavor_notes={'Sour': 1.0}),
    colorant=Colorant(color='Colorless', natural=True),
))

# Sodium Citrate
ingredients_manager.add(Ingredient(
    name='Sodium Citrate',
    category=['Additive', 'Emulsifier', 'Buffering Agent'],
    fat=0.0,
    carbs=0.0,
    protein=0.0,
    weight=0.0,
    calories=0.0,
    ph_modifier=PHModifier(ph_change=-1.0),
    ph_buffer=PHBuffer(buffering_capacity=1.5),
    flavor_profiles=Flavor(flavor_notes={'Salty': 0.2}),
    colorant=Colorant(color='Colorless', natural=False),
))