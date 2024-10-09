from recipes.ice_cream import IceCreamRecipe, Constraints
from ingredients.base import ingredients_manager
# Initialize the ice cream recipe
ice_cream_recipe = IceCreamRecipe(total_weight=1000)

# Set up constraints
constraints = Constraints()
constraints.add_constraint("Fat", "total_fat", 10.0, 2.0)
constraints.add_constraint("Sugar", "total_carbs", 15.0, 1.0)
constraints.add_constraint("Protein", "total_protein", 3.0, 1.0)
constraints.add_constraint("Gum Agent", "total_gum_agent", 0.15, 0.05)
constraints.add_constraint("Sweetener", "total_sweetener", 15.0, 1.0)

ice_cream_recipe.constraints = constraints
im = ingredients_manager
# Add ingredients with specified weights and units
ice_cream_recipe.add_ingredient(im.get_ingredient_with_weight('Coconut Milk', 300, 'g'))
ice_cream_recipe.add_ingredient(im.get_ingredient_with_weight('White Sugar', 150, 'g'))
ice_cream_recipe.add_ingredient(im.get_ingredient_with_weight('Vegetable Oil', 50, 'g'))
ice_cream_recipe.add_ingredient(im.get_ingredient_with_weight('Water', 400, 'g'))
ice_cream_recipe.add_ingredient(im.get_ingredient_with_weight('Xanthan Gum', 5, 'g'))
ice_cream_recipe.add_ingredient(im.get_ingredient_with_weight('Locust Bean Gum', 5, 'g'))

# Using cups and tablespoons
ice_cream_recipe.add_ingredient(im.get_ingredient_with_weight('Coconut Milk', 1.25, 'cup'))
ice_cream_recipe.add_ingredient(im.get_ingredient_with_weight('White Sugar', 8, 'tbsp'))
ice_cream_recipe.add_ingredient(im.get_ingredient_with_weight('Vegetable Oil', 1, 'oz'))
ice_cream_recipe.add_ingredient(im.get_ingredient_with_weight('Water', 200, 'ml'))

# Adjust ingredient weights to match total desired weight
ice_cream_recipe.adjust_ingredient_weights()

# Calculate totals
totals = ice_cream_recipe.calculate_totals()
print("\nTotals:")
for key, value in totals.items():
    print(f"{key}: {value:.2f}")

# Validate the mix
validations = ice_cream_recipe.validate_mix()
print("\nValidation Results:")
for key, value in validations.items():
    print(f"{key}: {value}")
