# Pantry Path

Pantry Path is a command-line Python app that helps a user track pantry ingredients, update quantities, suggest recipes, and build a small shopping list. The project is designed for a Python Crash Course Chapters 1-7 final review, so the code intentionally stays readable and beginner-friendly while still behaving like a complete program.

## How to Run

```powershell
python main.py
```

To run the automated checks:

```powershell
python -m unittest discover -s tests
```

## Project Purpose

The app solves a small real-world planning problem: deciding what meals can be made from ingredients already on hand. A user can:

- View current pantry items by category.
- Add new ingredients or increase existing quantities.
- Use ingredients and update the saved state.
- See which recipes are ready and which ingredients are missing.
- Generate a unique shopping list from recipe gaps.

## Course Competency Map

| Requirement | Where it appears | Why it matters |
| --- | --- | --- |
| Variables and simple data types | Menu choices, quantities, recipe names, category strings | The app stores and updates text and numbers throughout the user journey. |
| Lists | `RECIPES`, recipe ingredients, missing ingredients, shopping list | Lists preserve order and support repeated recipe and shopping-list processing. |
| Tuples | `CATEGORIES` | Categories are fixed choices, so a tuple communicates that they should not change during the program. |
| Dictionaries | Pantry records and each recipe record | Dictionaries make ingredient details easy to find by meaningful keys like `quantity` and `category`. |
| Control flow | Menu choices, validation, recipe readiness checks | `if`, `elif`, and `else` statements direct the program based on user actions and pantry state. |
| Iteration | Recipe scanning, pantry grouping, shopping-list generation | `for` loops process collections, while the main menu and validation prompts use `while` loops. |
| User interaction | The main menu and ingredient prompts | `input()` lets the user control the program state during the live demo. |

## Design Justification

Pantry Path uses dictionaries for pantry items because each ingredient needs named details, not just a position in a list. Recipes are stored in a list because the app reviews each recipe in order. Categories are stored in a tuple because the valid category options are intentionally fixed.

The program includes functions even though functions are beyond Chapters 1-7 in many course schedules. They are used here to keep the project readable, avoid repeated code, and make testing practical. During the video analysis, this is worth mentioning as a code-quality improvement rather than a replacement for the required chapter concepts.

## Suggested Demo Path

1. Run `python main.py`.
2. Choose option `1` to show the starting pantry.
3. Choose option `4` to show ready recipes and missing items.
4. Choose option `2`, add `lettuce`, quantity `2`, category `vegetable`.
5. Choose option `3`, use `1` tomato.
6. Choose option `5` to build a shopping list.
7. Choose option `6` to exit cleanly.

## Presentation Checklist

- Replace the video placeholder at the top of this README with the final unlisted YouTube link.
- Keep the recording under 5 minutes.
- Show the live app first, then switch to the slide outline in `slides/presentation_outline.md`.
- Verify the YouTube link in an incognito window before submitting.

## Repository Notes

This repository was organized to support a realistic review process: source code is separated from tests, documentation explains the design choices, and commits should show incremental progress from planning through verification.
