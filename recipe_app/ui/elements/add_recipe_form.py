import flet as ft
from db import engine
from db.models import Category, Recipe
from sqlmodel import Session, select


def open_add_recipe_modal(page: ft.Page, on_added_callback):
    title_input = ft.TextField(label="Title", width=300)
    category_input = ft.TextField(label="Category", width=300)
    ingredients_input = ft.TextField(
        label="Ingredients", width=300, multiline=True
    )
    instructions_input = ft.TextField(
        label="Instructions", width=300, multiline=True
    )

    modal = ft.AlertDialog(modal=True)

    def close_modal():
        modal.open = False
        page.update()

    def submit_recipe(e):
        if not title_input.value or not category_input.value:
            page.snack_bar = ft.SnackBar(
                ft.Text("Title and Category are required!")
            )
            page.snack_bar.open = True
            page.update()
            return

        with Session(engine) as session:
            # Check if category exists
            category = session.exec(
                select(Category).where(Category.title == category_input.value)
            ).first()

            if not category:
                category = Category(title=category_input.value)
                session.add(category)
                session.commit()
                session.refresh(category)

            # Add recipe
            recipe = Recipe(
                title=title_input.value,
                category=category,
                ingredients=ingredients_input.value,
                instructions=instructions_input.value
            )
            session.add(recipe)
            session.commit()
        close_modal()
        on_added_callback()

    modal.title = ft.Text('Add a new recipe')
    modal.content = ft.Column(
            [
                title_input,
                category_input,
                ingredients_input,
                instructions_input
            ],
            tight=True
        )
    modal.actions = [
            ft.ElevatedButton("Submit", on_click=submit_recipe),
            ft.TextButton("Cancel", on_click=lambda e: close_modal())
        ]

    if modal not in page.overlay:
        page.overlay.append(modal)

    modal.open = True
    page.update()
