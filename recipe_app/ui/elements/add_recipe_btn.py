import flet as ft

from .add_recipe_form import open_add_recipe_modal


class AddRecipeButton(ft.ElevatedButton):
    def __init__(self, page: ft.Page, on_added_callback):
        self.page = page
        self.on_added_callback = on_added_callback

        super().__init__(
            text='New recipe',
            icon=ft.Icons.ADD_CIRCLE,
            width=150,
            height=40,
            on_click=self._handle_click
        )

    def _handle_click(self, e):
        open_add_recipe_modal(self.page, self.on_added_callback)
