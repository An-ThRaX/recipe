import flet as ft
from ui.elements.add_recipe_btn import AddRecipeButton
from ui.elements.build_catalogue_container import build_catalogue
from ui.elements.build_recipes_container import build_recipes_container
from ui.theme import MainTheme


def main_view(page: ft.Page):
    MainTheme().apply_theme(page)

    # Construct the recipes container
    recipes_container = build_recipes_container()

    # Construct the catalogue container
    catalogue = build_catalogue()

    # Reload the UI on changes
    def refresh_recipes():
        recipes_container.content = build_recipes_container().content
        catalogue.controls = build_catalogue().controls

        page.update()

    side_bar = ft.Container(
        content=ft.Column(
            controls=[
                AddRecipeButton(page, refresh_recipes),
                catalogue,
            ],
            spacing=20,
            width=250,
        ),
        padding=10
    )

    # Main layout: horizontal
    layout = ft.Row(
        # the main page with all its elements
        controls=[
            side_bar,
            # the rest of the screen, with the cards
            ft.Container(
                width=20,
                bgcolor=ft.Colors.WHITE,
                height=page.height
            ),
            recipes_container,
        ],
        expand=True,
    )

    page.add(layout)
