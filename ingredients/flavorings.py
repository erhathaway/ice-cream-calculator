from .base import ingredients_manager, Ingredient, Flavor, Colorant, PHModifier, EmulsifierProps

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
    emulsifier_props=EmulsifierProps(
        emulsification=0.1,  # Moved emulsification here
    ),
))

# Tangerine Zest
ingredients_manager.add(Ingredient(
    name='Tangerine Zest',
    category=['Flavoring'],
    fat=0.0,
    carbs=28.0,         # Approximate value per 100g
    protein=1.5,
    weight=0.0,         # Adjust as needed
    calories=138.0,
    flavor_profiles=Flavor(flavor_notes={'Citrus': 1.0, 'Tangerine': 1.0}),
    colorant=Colorant(color='Orange', natural=True),
))

# Tangerine Juice
ingredients_manager.add(Ingredient(
    name='Tangerine Juice',
    category=['Flavoring', 'Liquid'],
    fat=0.0,
    carbs=10.4,         # Approximate value per 100g
    protein=0.7,
    weight=0.0,
    calories=45.0,
    flavor_profiles=Flavor(flavor_notes={'Citrus': 1.0, 'Tangerine': 1.0}),
    colorant=Colorant(color='Orange', natural=True),
))

# Mandarin Zest
ingredients_manager.add(Ingredient(
    name='Mandarin Zest',
    category=['Flavoring'],
    fat=0.0,
    carbs=28.0,
    protein=1.5,
    weight=0.0,
    calories=138.0,
    flavor_profiles=Flavor(flavor_notes={'Citrus': 1.0, 'Mandarin': 1.0}),
    colorant=Colorant(color='Orange', natural=True),
))

# Mandarin Juice
ingredients_manager.add(Ingredient(
    name='Mandarin Juice',
    category=['Flavoring', 'Liquid'],
    fat=0.0,
    carbs=10.5,
    protein=0.6,
    weight=0.0,
    calories=43.0,
    flavor_profiles=Flavor(flavor_notes={'Citrus': 1.0, 'Mandarin': 1.0}),
    colorant=Colorant(color='Orange', natural=True),
))

# Lemon Zest
ingredients_manager.add(Ingredient(
    name='Lemon Zest',
    category=['Flavoring'],
    fat=0.0,
    carbs=25.0,
    protein=1.5,
    weight=0.0,
    calories=130.0,
    flavor_profiles=Flavor(flavor_notes={'Citrus': 1.0, 'Lemon': 1.0}),
    colorant=Colorant(color='Yellow', natural=True),
))

# Lemon Juice
ingredients_manager.add(Ingredient(
    name='Lemon Juice',
    category=['Flavoring', 'Liquid'],
    fat=0.0,
    carbs=6.9,
    protein=0.4,
    weight=0.0,
    calories=22.0,
    flavor_profiles=Flavor(flavor_notes={'Citrus': 1.0, 'Lemon': 1.0}),
    colorant=Colorant(color='Yellow', natural=True),
    ph_modifier=PHModifier(ph_change=-2.0),  # Lemon juice is acidic
))

# Orange Zest
ingredients_manager.add(Ingredient(
    name='Orange Zest',
    category=['Flavoring'],
    fat=0.0,
    carbs=28.0,
    protein=1.5,
    weight=0.0,
    calories=138.0,
    flavor_profiles=Flavor(flavor_notes={'Citrus': 1.0, 'Orange': 1.0}),
    colorant=Colorant(color='Orange', natural=True),
))

# Orange Juice
ingredients_manager.add(Ingredient(
    name='Orange Juice',
    category=['Flavoring', 'Liquid'],
    fat=0.2,
    carbs=10.4,
    protein=0.7,
    weight=0.0,
    calories=45.0,
    flavor_profiles=Flavor(flavor_notes={'Citrus': 1.0, 'Orange': 1.0}),
    colorant=Colorant(color='Orange', natural=True),
))

# Cardamom
ingredients_manager.add(Ingredient(
    name='Cardamom',
    category=['Flavoring', 'Spice'],
    fat=6.7,
    carbs=68.5,
    protein=11.0,
    weight=0.0,
    calories=311.0,
    flavor_profiles=Flavor(flavor_notes={'Spicy': 1.0, 'Warm': 0.8, 'Citrus': 0.5}),
    colorant=Colorant(color='Pale Green', natural=True),
))

# Chili Powder
ingredients_manager.add(Ingredient(
    name='Chili Powder',
    category=['Flavoring', 'Spice'],
    fat=14.3,
    carbs=49.9,
    protein=14.1,
    weight=0.0,
    calories=282.0,
    flavor_profiles=Flavor(flavor_notes={'Spicy': 1.0, 'Smoky': 0.5}),
    colorant=Colorant(color='Red', natural=True),
))

# Cinnamon
ingredients_manager.add(Ingredient(
    name='Cinnamon',
    category=['Flavoring', 'Spice'],
    fat=1.2,
    carbs=80.6,
    protein=4.0,
    weight=0.0,
    calories=247.0,
    flavor_profiles=Flavor(flavor_notes={'Warm': 1.0, 'Sweet': 0.5}),
    colorant=Colorant(color='Brown', natural=True),
))

# Sumac
ingredients_manager.add(Ingredient(
    name='Sumac',
    category=['Flavoring', 'Spice'],
    fat=0.0,
    carbs=0.0,
    protein=0.0,
    weight=0.0,
    calories=0.0,
    flavor_profiles=Flavor(flavor_notes={'Tangy': 1.0, 'Citrus': 0.5}),
    colorant=Colorant(color='Deep Red', natural=True),
))

# Sage
ingredients_manager.add(Ingredient(
    name='Sage',
    category=['Flavoring', 'Herb'],
    fat=13.0,
    carbs=60.7,
    protein=10.6,
    weight=0.0,
    calories=315.0,
    flavor_profiles=Flavor(flavor_notes={'Herbal': 1.0, 'Earthy': 0.8, 'Pine': 0.5}),
    colorant=Colorant(color='Grayish Green', natural=True),
))

# Peppermint
ingredients_manager.add(Ingredient(
    name='Peppermint',
    category=['Flavoring', 'Herb'],
    fat=0.9,
    carbs=14.9,
    protein=3.8,
    weight=0.0,
    calories=70.0,
    flavor_profiles=Flavor(flavor_notes={'Minty': 1.0, 'Fresh': 0.8}),
    colorant=Colorant(color='Green', natural=True),
))

# Ginger
ingredients_manager.add(Ingredient(
    name='Ginger',
    category=['Flavoring', 'Spice'],
    fat=0.8,
    carbs=17.8,
    protein=1.8,
    weight=0.0,
    calories=80.0,
    flavor_profiles=Flavor(flavor_notes={'Spicy': 1.0, 'Warm': 0.8, 'Citrus': 0.3}),
    colorant=Colorant(color='Light Brown', natural=True),
))

# Lime Zest
ingredients_manager.add(Ingredient(
    name='Lime Zest',
    category=['Flavoring'],
    fat=0.0,
    carbs=25.0,
    protein=1.0,
    weight=0.0,
    calories=130.0,
    flavor_profiles=Flavor(flavor_notes={'Citrus': 1.0, 'Lime': 1.0}),
    colorant=Colorant(color='Green', natural=True),
))

# Lime Juice
ingredients_manager.add(Ingredient(
    name='Lime Juice',
    category=['Flavoring', 'Liquid'],
    fat=0.0,
    carbs=8.4,
    protein=0.4,
    weight=0.0,
    calories=25.0,
    flavor_profiles=Flavor(flavor_notes={'Citrus': 1.0, 'Lime': 1.0}),
    colorant=Colorant(color='Light Green', natural=True),
    ph_modifier=PHModifier(ph_change=-2.0),
))

# Coriander
ingredients_manager.add(Ingredient(
    name='Coriander',
    category=['Flavoring', 'Spice'],
    fat=17.8,
    carbs=54.9,
    protein=12.4,
    weight=0.0,
    calories=298.0,
    flavor_profiles=Flavor(flavor_notes={'Citrus': 0.5, 'Nutty': 1.0, 'Floral': 0.3}),
    colorant=Colorant(color='Light Brown', natural=True),
))