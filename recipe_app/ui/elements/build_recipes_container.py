import flet as ft
from services.recipes import fetch_all_recipes
from ui.grid import build_recipe_grid


def build_recipes_container():
    return ft.Container(
        content=ft.ListView(
            controls=build_recipe_grid(fetch_all_recipes()).controls,
            expand=True,
            padding=10,
            spacing=10,
        ),
        expand=True,
        padding=10,
    )
