import flet as ft
from ui.elements.add_recipe import AddRecipe
from ui.grid import build_recipe_grid


def main_view(page: ft.Page):
    page.title = "Retetar"
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll = "adaptive"

    # Left catalogue (categories)
    catalogue = ft.Column(
        [
            ft.Text("Catalogue", size=20, weight="bold"),
            ft.TextButton("All Recipes"),
            ft.TextButton("Desserts"),
            ft.TextButton("Main Dishes"),
            ft.TextButton("Drinks"),
        ],
        width=200,
        spacing=10,
    )

    recipes = [{"title": f"Recipe {i+1}", "description": "Short description"} for i in range(13)]
    recipe_grid = build_recipe_grid(recipes)
    grid_container = ft.Container(
        content=recipe_grid,
        expand=True,
        padding=10,
    )

    # Main layout: horizontal
    layout = ft.Row(
        controls=[
            ft.Column(
                controls=[
                    AddRecipe(),
                    catalogue,
                ],
                spacing=20,
            ),
            ft.VerticalDivider(),
            grid_container,
        ],
        expand=True,
    )

    page.add(layout)