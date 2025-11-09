import flet as ft

class MainTheme():
    def __init__(self):
        # if a variable, mode is parsed (e.g light/dark), the theme
        # can be easily changed at this level
        # base theme data
        self.title = "Retetar"
        self.scroll = 'adaptive'
        self.horizontal_alignment = ft.CrossAxisAlignment.START
        self.vertical_alignment = ft.MainAxisAlignment.START

    def apply_theme(self, page: ft.Page):
        page.title = self.title
        page.scroll = self.scroll
        page.horizontal_alignment = self.horizontal_alignment
        page.vertical_alignment = self.vertical_alignment
        page.bgcolor = self.bg_color
