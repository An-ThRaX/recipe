import flet as ft
from ui.elements.recipe_card import RecipeCard


def build_recipe_grid(recipes):
    rows = []
    # slice 3 recipes per row
    for i in range(0, len(recipes), 3):
        row = ft.Row(
            controls=[
                RecipeCard(r).card() for r in recipes[i:i+3]
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            spacing=20,  # gap between cards
        )
        rows.append(row)
    return ft.Column(rows, spacing=20)
