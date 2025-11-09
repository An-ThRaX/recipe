import flet as ft
from services.recipes import add_pseudo_recipe


class AddRecipe(ft.ElevatedButton):
    def __init__(self):
        super().__init__(
            text='Adauga',
            icon=ft.Icons.ADD_CIRCLE,
            width=100,
            height=40,
            on_click=add_pseudo_recipe
        )
