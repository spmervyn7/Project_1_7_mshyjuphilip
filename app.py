"""Pantry Path application logic.

Author: Mervyn S. Philip
Purpose: Run the menu, manage pantry state, and suggest recipes.
Starter code/resources: Python Chapters 1-7 project.
Date: 2026-06-28
"""

from copy import deepcopy

from src.pantry_path.data import CATEGORIES, RECIPES, STARTING_PANTRY


def get_fresh_pantry():
    """Return a separate pantry dictionary so each session starts cleanly."""
    return deepcopy(STARTING_PANTRY)


def show_welcome():
    """Print the program title and a short user-facing summary."""
    print("\nWelcome to Pantry Path!")
    print("Track ingredients, find possible meals, and build a small shopping list.")


def display_menu():
    """Print the main menu choices."""
    print("\nMain Menu")
    print("1. View pantry")
    print("2. Add or update ingredient")
    print("3. Use an ingredient")
    print("4. Suggest recipes")
    print("5. Build shopping list")
    print("6. Exit")


def display_pantry(pantry):
    """Print pantry ingredients grouped by their saved category."""
    if not pantry:
        print("\nYour pantry is empty.")
        return

    print("\nCurrent Pantry")
    for category in CATEGORIES:
        category_items = []
        for item_name, details in pantry.items():
            if details["category"] == category:
                category_items.append(f"{item_name.title()} ({details['quantity']})")

        if category_items:
            print(f"{category.title()}: {', '.join(category_items)}")


def ask_for_positive_number(prompt):
    """Ask until the user enters a whole number greater than zero."""
    while True:
        response = input(prompt).strip()
        if response.isdigit():
            number = int(response)
            if number > 0:
                return number

        print("Please enter a whole number greater than zero.")


def ask_for_category():
    """Ask until the user chooses one of the supported ingredient categories."""
    print(f"Categories: {', '.join(CATEGORIES)}")
    while True:
        category = input("Category: ").strip().lower()
        if category in CATEGORIES:
            return category

        print("Please choose one of the listed categories.")


def add_or_update_ingredient(pantry):
    """Add a new ingredient or increase the quantity of an existing ingredient."""
    ingredient = input("\nIngredient name: ").strip().lower()
    if ingredient == "":
        print("Ingredient name cannot be blank.")
        return

    quantity = ask_for_positive_number("Quantity to add: ")

    if ingredient in pantry:
        pantry[ingredient]["quantity"] += quantity
        print(f"Updated {ingredient}: {pantry[ingredient]['quantity']} available.")
    else:
        category = ask_for_category()
        pantry[ingredient] = {"quantity": quantity, "category": category}
        print(f"Added {ingredient} to your pantry.")


def use_ingredient(pantry):
    """Remove a chosen quantity from the pantry without dropping below zero."""
    ingredient = input("\nIngredient to use: ").strip().lower()
    if ingredient not in pantry:
        print("That ingredient is not in your pantry.")
        return

    quantity = ask_for_positive_number("Quantity to use: ")
    current_quantity = pantry[ingredient]["quantity"]

    if quantity < current_quantity:
        pantry[ingredient]["quantity"] -= quantity
        print(f"{ingredient.title()} now has {pantry[ingredient]['quantity']} left.")
    elif quantity == current_quantity:
        del pantry[ingredient]
        print(f"You used the last of your {ingredient}.")
    else:
        print(f"You only have {current_quantity} {ingredient} available.")


def find_missing_ingredients(recipe, pantry):
    """Return a list of recipe ingredients that are not currently available."""
    missing_ingredients = []
    for ingredient in recipe["ingredients"]:
        if ingredient not in pantry or pantry[ingredient]["quantity"] <= 0:
            missing_ingredients.append(ingredient)

    return missing_ingredients


def suggest_recipes(pantry):
    """Print recipe suggestions and identify whether each one is ready or blocked."""
    print("\nRecipe Suggestions")
    ready_count = 0

    for recipe in RECIPES:
        missing_ingredients = find_missing_ingredients(recipe, pantry)
        difficulty = "*" * recipe["difficulty"]

        if not missing_ingredients:
            ready_count += 1
            print(f"Ready: {recipe['name']} | Difficulty: {difficulty}")
        else:
            missing_text = ", ".join(missing_ingredients)
            print(f"Need {missing_text}: {recipe['name']} | Difficulty: {difficulty}")

    if ready_count == 0:
        print("No full recipes are ready yet. Try building a shopping list next.")


def build_shopping_list(pantry):
    """Print a unique shopping list for all missing recipe ingredients."""
    shopping_list = []

    for recipe in RECIPES:
        missing_ingredients = find_missing_ingredients(recipe, pantry)
        for ingredient in missing_ingredients:
            if ingredient not in shopping_list:
                shopping_list.append(ingredient)

    if shopping_list:
        print("\nShopping List")
        for number, ingredient in enumerate(shopping_list, start=1):
            print(f"{number}. {ingredient.title()}")
    else:
        print("\nYou have every ingredient needed for the current recipes.")


def run_pantry_path():
    """Run the main program loop until the user chooses to exit."""
    pantry = get_fresh_pantry()
    running = True
    show_welcome()

    while running:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_pantry(pantry)
        elif choice == "2":
            add_or_update_ingredient(pantry)
        elif choice == "3":
            use_ingredient(pantry)
        elif choice == "4":
            suggest_recipes(pantry)
        elif choice == "5":
            build_shopping_list(pantry)
        elif choice == "6":
            running = False
            print("Thanks for using Pantry Path. Goodbye!")
        else:
            print("Please choose a menu option from 1 to 6.")