import flet as ft


def build_recipe_grid(recipes):
    rows = []
    for i in range(0, len(recipes), 3):
        row = ft.Row(
            controls=[
                ft.Card(
                    width=300,  # fixed width
                    content=ft.Container(
                        padding=10,
                        content=ft.Column(
                            [
                                ft.Text(r["title"], size=18, weight="bold"),
                                ft.Text(r["desc"], size=12),
                            ]
                        ),
                    ),
                )
                for r in recipes[i:i+3]  # slice 3 recipes per row
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            spacing=20,  # gap between cards
        )
        rows.append(row)
    return ft.Column(rows, spacing=20)
