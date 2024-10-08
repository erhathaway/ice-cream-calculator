from ingredients import Ingredient, GumAgentProps, SweetenerProps
from recipes.ice_cream import IceCreamRecipe

# Create ingredients
coconut_milk = Ingredient(name='Coconut Milk', fat=24, carbs=6, protein=2, weight=400)
sugar = Ingredient(name='Sugar', fat=0, carbs=100, protein=0, weight=150, sweetness=1.0)
sugar.sweetener_props = SweetenerProps(glycemic_index=65, relative_sweetness=1.0)
oil = Ingredient(name='Vegetable Oil', fat=100, carbs=0, protein=0, weight=100)
water = Ingredient(name='Water', fat=0, carbs=0, protein=0, weight=350)

# Create gum agents
xanthan_gum = Ingredient(name='Xanthan Gum', fat=0, carbs=77, protein=7, weight=0, sweetness=0)
xanthan_gum.gum_agent_props = GumAgentProps(
    ideal_usage_min=0.1,
    ideal_usage_max=0.2,
    activation_temp=25,
    cold_soluble=True,
    interactions=['Locust Bean Gum']
)

locust_bean_gum = Ingredient(name='Locust Bean Gum', fat=1, carbs=80, protein=5, weight=0, sweetness=0)
locust_bean_gum.gum_agent_props = GumAgentProps(
    ideal_usage_min=0.1,
    ideal_usage_max=0.25,
    activation_temp=85,
    cold_soluble=False,
    interactions=['Xanthan Gum']
)

# Initialize the ice cream recipe
ice_cream_recipe = IceCreamRecipe(total_weight=1000)

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

# Get recommended amounts
all_ingredients = [coconut_milk, sugar, oil, water, xanthan_gum, locust_bean_gum]
recommended_amounts = ice_cream_recipe.recommend_amounts(all_ingredients)
print("\nRecommended Amounts:")
for ingredient, amount in recommended_amounts.items():
    print(f"{ingredient}: {amount:.2f}g")