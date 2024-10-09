import streamlit as st
import pandas as pd

from recipes.ice_cream import IceCreamRecipe, Constraints
from ingredients.base import ingredients_manager
from copy import deepcopy

st.title("Ice Cream Recipe Calculator")

# Initialize session state for ingredient weights
if 'ingredient_weights' not in st.session_state:
    st.session_state.ingredient_weights = {}

# Input for total desired weight
total_weight = st.number_input("Total desired weight (g)", min_value=0.0, value=1000.0, step=1.0)

# Select recipe (placeholder for multiple recipes)
recipes = ['Ice Cream Recipe']  # Add more recipes as needed
selected_recipe_name = st.selectbox('Select a recipe', recipes)

# Initialize the selected recipe
ice_cream_recipe = IceCreamRecipe(total_weight=total_weight)

# Select ingredients with filtering options
im = ingredients_manager
all_ingredients = im.ingredients

# Get all categories for filtering
categories = set()
for ing in all_ingredients:
    categories.update(ing.category)
categories = sorted(list(categories))

st.subheader("Select Ingredients")


# Create filter header. Make it a h7
st.markdown("##### Category Filter")

# Create a container for category tags
category_container = st.container()

# Custom CSS for category tags
st.markdown("""
<style>
.stButton > button {
    color: #4F8BF9;
    border-color: #4F8BF9;
    background-color: white;
    margin: 2px;
    width: 150px !important;
    height: auto !important;
    white-space: normal !important;
    word-wrap: break-word !important;
    padding: 0.5rem !important;
}
.stButton > button:hover {
    color: white;
    border-color: #4F8BF9;
    background-color: #4F8BF9;
}
.selected {
    color: white !important;
    border-color: #4F8BF9 !important;
    background-color: black !important;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state for selected categories if not exists
if 'selected_categories' not in st.session_state:
    st.session_state.selected_categories = set()

# Create category tags
with category_container:
    cols = st.columns(4)  # Adjust the number of columns as needed
    for i, category in enumerate(categories):
        col = cols[i % 4]
        if col.button(category, key=f"cat_{category}"):
            if category in st.session_state.selected_categories:
                st.session_state.selected_categories.remove(category)
            else:
                st.session_state.selected_categories.add(category)

# Update button styles based on selection
for category in categories:
    if category in st.session_state.selected_categories:
        st.markdown(f"""
        <script>
        var button = document.querySelector('button[kind="secondary"][data-baseweb="button"]:contains("{category}")');
        if (button) button.classList.add('selected');
        </script>
        """, unsafe_allow_html=True)

# Filter ingredients based on selected categories
if st.session_state.selected_categories:
    filtered_ingredients = [ing for ing in all_ingredients if any(cat in ing.category for cat in st.session_state.selected_categories)]
else:
    filtered_ingredients = all_ingredients

filtered_ingredient_names = [ing.name for ing in filtered_ingredients]
selected_ingredient_names = st.multiselect('Choose ingredients', filtered_ingredient_names)

# Adjust weights of selected ingredients
st.subheader("Adjust Ingredient Weights")
for ing_name in selected_ingredient_names:
    if ing_name not in st.session_state.ingredient_weights:
        st.session_state.ingredient_weights[ing_name] = 0.0
    weight = st.number_input(
        f"Weight of {ing_name} (g)",
        min_value=0.0,
        max_value=10000.0,
        value=st.session_state.ingredient_weights[ing_name],
        step=1.0,
        key=f"weight_{ing_name}"
    )
    st.session_state.ingredient_weights[ing_name] = weight

# Add ingredients to the recipe
for ing_name in selected_ingredient_names:
    weight = st.session_state.ingredient_weights[ing_name]
    if weight > 0:
        ing = im.get_ingredient_with_weight(ing_name, weight, 'g')
        ice_cream_recipe.add_ingredient(ing)

# Set up constraints
st.subheader("Set Constraints")
possible_constraints = {
    'Total Fat': 'total_fat',
    'Total Carbs': 'total_carbs',
    'Total Protein': 'total_protein',
    'Total Gum Agent': 'total_gum_agent',
    'Total Sweetener': 'total_sweetener',
    # Add other possible constraints as needed
}

selected_constraints = st.multiselect('Select constraints to apply', list(possible_constraints.keys()))

constraints = Constraints()
for constraint_name in selected_constraints:
    property_name = possible_constraints[constraint_name]
    ideal_value = st.number_input(
        f"Ideal percentage for {constraint_name}",
        min_value=0.0,
        max_value=100.0,
        value=10.0,
        step=0.1,
        key=f"ideal_{property_name}"
    )
    tolerance = st.number_input(
        f"Tolerance for {constraint_name} (+/- %)",
        min_value=0.0,
        max_value=100.0,
        value=1.0,
        step=0.1,
        key=f"tolerance_{property_name}"
    )
    constraints.add_constraint(constraint_name, property_name, ideal_value, tolerance)

ice_cream_recipe.constraints = constraints

# Button to adjust weights automatically
if st.button("Adjust Weights Automatically"):
    ice_cream_recipe.adjust_ingredient_weights()
    # Update session state with new weights
    for ing in ice_cream_recipe.ingredients:
        st.session_state.ingredient_weights[ing.name] = ing.weight
    st.success("Ingredient weights adjusted automatically.")

# Calculate totals and display
totals = ice_cream_recipe.calculate_totals()
st.subheader("Totals")
totals_df = pd.DataFrame.from_dict(totals, orient='index', columns=['Value'])
st.dataframe(totals_df)

# Validate the mix and display results
validations = ice_cream_recipe.validate_mix()
st.subheader("Validation Results")
validation_df = pd.DataFrame(list(validations.items()), columns=['Validation', 'Result'])
st.dataframe(validation_df)

# Button to recommend adjustments
if st.button("Recommend Adjustments"):
    adjustments = ice_cream_recipe.recommend_adjustments()
    st.subheader("Recommended Adjustments")
    adjustments_df = pd.DataFrame(list(adjustments.items()), columns=['Ingredient', 'Adjustment (g)'])
    st.dataframe(adjustments_df)
    # Update session state with adjusted weights
    for ing in ice_cream_recipe.ingredients:
        st.session_state.ingredient_weights[ing.name] = ing.weight
    st.success("Ingredient weights adjusted based on recommendations.")

    # Recalculate totals and validations after adjustments
    totals = ice_cream_recipe.calculate_totals()
    st.subheader("Updated Totals")
    totals_df = pd.DataFrame.from_dict(totals, orient='index', columns=['Value'])
    st.dataframe(totals_df)

    validations = ice_cream_recipe.validate_mix()
    st.subheader("Updated Validation Results")
    validation_df = pd.DataFrame(list(validations.items()), columns=['Validation', 'Result'])
    st.dataframe(validation_df)

