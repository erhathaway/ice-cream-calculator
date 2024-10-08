from recipes.ice_cream import IceCreamRecipe, Constraints
from ingredients import ingredients_manager

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

# Retrieve ingredients by name
coconut_milk = ingredients_manager.get_ingredient_by_name('Coconut Milk')
sugar = ingredients_manager.get_ingredient_by_name('Sugar')
oil = ingredients_manager.get_ingredient_by_name('Vegetable Oil')
water = ingredients_manager.get_ingredient_by_name('Water')
xanthan_gum = ingredients_manager.get_ingredient_by_name('Xanthan Gum')
locust_bean_gum = ingredients_manager.get_ingredient_by_name('Locust Bean Gum')

# Add ingredients to the recipe
for ingredient in [coconut_milk, sugar, oil, water, xanthan_gum, locust_bean_gum]:
    ice_cream_recipe.add_ingredient(ingredient)

# Adjust ingredient weights to match total desired weight
ice_cream_recipe.adjust_ingredient_weights()

# Calculate totals
totals = ice_cream_recipe.calculate_totals()
print("Totals:")
for key, value in totals.items():
    print(f"{key}: {value:.2f}")

# Validate the mix
validations = ice_cream_recipe.validate_mix()
print("\nValidation Results:")
for key, value in validations.items():
    print(f"{key}: {value}")
