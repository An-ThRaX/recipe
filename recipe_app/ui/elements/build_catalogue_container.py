import flet as ft
from services.categories import fetch_all_categories


def build_catalogue():
    return ft.Column(
        controls=[
            ft.Text("Catalogue", size=28, weight='blod'),
            *[ft.Text(c.title) for c in fetch_all_categories()]
        ],
        width=200,
        spacing=10
    )
