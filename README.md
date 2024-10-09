# 🍦 Ice Cream Recipe Calculator

Calculate ideal ingredient ratios based on different recipes.

[Live App](https://tiny-grass-0760.ploomberapp.io/)

## Overview

Welcome to the **Ice Cream Recipe Calculator**! This application helps you create perfect ice cream recipes by calculating ideal ingredient ratios based on your preferences and constraints. Whether you're a professional chef or an ice cream enthusiast, this tool will help you craft delicious and balanced ice cream recipes with ease.

## 🚀 Features

- **Total Weight Input**: Specify your desired total weight for the ice cream batch.
- **Ingredient Selection**: Choose from a wide variety of ingredients, including emulsifiers, stabilizers, sweeteners, dairy options, flavorings, and more.
- **Filtering Options**: Filter ingredients by categories to easily find what you need.
- **Customizable Constraints**: Define constraints for your recipe, such as ideal values and tolerances for specific properties.
- **Automatic Weight Adjustment**: Automatically adjust ingredient weights to meet your specified constraints.
- **Validation and Recommendations**: Validate your mix and receive recommendations for adjustments to optimize your recipe.
- **Interactive Streamlit App**: User-friendly interface powered by Streamlit for an interactive recipe creation experience.


## 🛠️ Installation

### Prerequisites

- **Python 3.11+**
- **[Poetry](https://python-poetry.org/)** (for dependency management)

### Clone the Repository

```bash
git clone https://github.com/yourusername/ice-cream-calculator.git
cd ice-cream-calculator
```

### Install Dependencies

We use **Poetry** for dependency management.

Install dependencies:

```bash
poetry install
```

Generate `requirements.txt`:

```bash
poetry export --without-hashes --format=requirements.txt > requirements.txt
```

### Activate the Virtual Environment

Activate the Poetry shell:

```bash
poetry shell
```

### Alternatively, using Pip

If you prefer using Pip, install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

### Running the Streamlit App

Within the Poetry shell, run the Streamlit app:

```bash
streamlit run app.py
```

### Deploying with Ploomber Cloud

To deploy the app using **Ploomber Cloud**, run:

```bash
ploomber-cloud deploy
```

*Note: Ensure you have **Ploomber Cloud** installed and configured correctly.*

## 📚 Project Structure

```
ice-cream-calculator/
├── app.py
├── ingredients/
│   ├── __init__.py
│   ├── base.py
│   ├── emulsifiers.py
│   ├── stabilizers_and_thickeners.py
│   ├── sweeteners.py
│   └── ...
├── recipes/
│   ├── __init__.py
│   ├── base.py
│   └── ice_cream.py
├── pyproject.toml
├── requirements.txt
├── ploomber-cloud.json
└── README.md
```

- **`app.py`**: The main Streamlit application.
- **`ingredients/`**: Contains ingredient classes and definitions.
- **`recipes/`**: Contains recipe classes like `Recipe` and `IceCreamRecipe`.

---

*Happy ice cream making! 🍨*

---

