import flet as ft


class RecipeCard(ft.Card):
    def __init__(self, recipe):
        self.recipe = recipe
        super().__init__()

    def _card_content(self, recipe):
        # this here defines the contents of each recipe card
        _card_content = ft.Container(
            padding=10,
            content=ft.Column(
                [
                    ft.Text(recipe["title"], size=18, weight="bold"),
                    ft.Text(recipe["description"], size=12),
                ]
            ),
        )
        return _card_content

    def card(self) -> None:
        # this here defines the aspect of each recipe card
        _card = ft.Card(
            width=300,
            content=self._card_content(self.recipe),
            color='blue',
        )
        return _card
