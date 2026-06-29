"""Pantry Path data.

Author: Mervyn S. Philip
Purpose: Provide starter pantry items, categories, and recipe data.
Starter code/resources: Python Chapters 1-7 project.
Date: 2026-06-28
"""

CATEGORIES = ("protein", "grain", "vegetable", "fruit", "dairy", "pantry")

STARTING_PANTRY = {
    "rice": {"quantity": 3, "category": "grain"},
    "black beans": {"quantity": 2, "category": "protein"},
    "chicken": {"quantity": 1, "category": "protein"},
    "tomato": {"quantity": 4, "category": "vegetable"},
    "cheddar": {"quantity": 2, "category": "dairy"},
}

RECIPES = [
    {
        "name": "Rice and Bean Bowl",
        "ingredients": ["rice", "black beans", "tomato", "cheddar"],
        "difficulty": 1,
    },
    {
        "name": "Chicken Garden Plate",
        "ingredients": ["chicken", "rice", "tomato"],
        "difficulty": 2,
    },
    {
        "name": "Cheesy Tomato Rice",
        "ingredients": ["rice", "tomato", "cheddar"],
        "difficulty": 1,
    },
    {
        "name": "Protein Power Bowl",
        "ingredients": ["black beans", "chicken", "rice"],
        "difficulty": 3,
    },
]