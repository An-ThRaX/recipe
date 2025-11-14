import flet as ft
from services.categories import fetch_all_categories
from services.recipes import add_pseudo_recipe, fetch_all_recipes
from ui.elements.add_recipe import AddRecipe
from ui.grid import build_recipe_grid
from ui.theme import MainTheme


def main_view(page: ft.Page):
    MainTheme().apply_theme(page)

    # build the grid with recipe cards
    recipe_grid = build_recipe_grid(
        fetch_all_recipes()
    )

    recipes_container = ft.Container(
        content=recipe_grid,
        expand=True,
        padding=10,
    )

    def on_add_recipe(e):
        # TODO 1: i got to change this to make use of AddRecipe() instead of add_pseudo_recipe
        # TODO remove this and call the actual AddRecipe
        add_pseudo_recipe()
        recipes_container.content = build_recipe_grid(fetch_all_recipes())
        page.update()



    # Left catalogue (categories)
    catalogue = ft.Column(
        [ft.Text("Catalogue", size=20, weight="bold")] +
        [ft.Text(c.title) for c in fetch_all_categories()],
        width=200,
        spacing=10,
    )

    page.update()
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
            recipes_container,
        ],
        expand=True,
    )

    page.add(layout)
