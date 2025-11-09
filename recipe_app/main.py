import warnings

import flet as ft
from db import init_db
from ui.main_view import main_view

warnings.filterwarnings("ignore", category=DeprecationWarning)

init_db()


def main(page: ft.Page):
    page.title = "Recipes"
    main_view(page)


ft.app(
    target=main,
    host='0.0.0.0',
    )
