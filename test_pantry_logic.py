"""Pantry Path tests.

Author: Mervyn S. Philip
Purpose: Verify recipe and pantry helper behavior.
Starter code/resources: Python Chapters 1-7 project.
Date: 2026-06-28
"""

import unittest

from src.pantry_path.app import find_missing_ingredients, get_fresh_pantry


class PantryLogicTests(unittest.TestCase):
    """Test the non-interactive logic used by the Pantry Path menu."""

    def test_fresh_pantry_can_be_changed_without_changing_original(self):
        """Changing one pantry copy should not affect a second fresh pantry."""
        first_pantry = get_fresh_pantry()
        second_pantry = get_fresh_pantry()

        first_pantry["rice"]["quantity"] = 99

        self.assertEqual(second_pantry["rice"]["quantity"], 3)

    def test_find_missing_ingredients_returns_only_unavailable_items(self):
        """A recipe should report ingredients missing from the pantry."""
        pantry = {"rice": {"quantity": 1, "category": "grain"}}
        recipe = {"name": "Simple Bowl", "ingredients": ["rice", "beans"]}

        missing_ingredients = find_missing_ingredients(recipe, pantry)

        self.assertEqual(missing_ingredients, ["beans"])


    def test_find_missing_ingredients_returns_empty_list_when_all_ingredients_are_available(self):
        """A recipe should return an empty list when all ingredients are available."""
        pantry = {"rice": {"quantity": 1, "category": "grain"}, "beans": {"quantity": 2, "category": "legume"}}
        recipe = {"name": "Simple Bowl", "ingredients": ["rice", "beans"]}

        missing_ingredients = find_missing_ingredients(recipe, pantry)

        self.assertEqual(missing_ingredients, [])


if __name__ == "__main__":
    unittest.main()