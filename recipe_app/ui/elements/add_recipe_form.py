import flet as ft
from db import engine
from db.models import Category, Recipe
from sqlmodel import Session, select


def open_add_recipe_modal(page: ft.Page, on_added_callback):

    def validate_field(e):
        field = e.control
        if field.value.strip():
            field.error_text = None
            page.update()

    title_input = ft.TextField(
        label="Title",
        width=300,
        on_change=validate_field
    )
    category_input = ft.TextField(
        label="Category",
        width=300,
        on_change=validate_field
    )
    ingredients_input = ft.TextField(
        label="Ingredients", width=300, multiline=True
    )
    instructions_input = ft.TextField(
        label="Instructions", width=300, multiline=True
    )

    # instantiate the modal
    modal = ft.AlertDialog(modal=True)
    # internal state to switch view of the form in case of cancelin with
    # fields filled in
    modal.confirming = False

    def build_form():
        # construc the recipe adding form

        modal.title = ft.Text("Add a new recipe")
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

    def build_confirmation():
        # construct the confirm cancel modal

        modal.title = ft.Text("Unsaved changes")
        modal.content = ft.Text(
            "You have unsaved recipe. Are you sure you want to cancel?"
        )

        modal.actions = [
            ft.TextButton('Cancel', on_click=lambda e: restore_form()),
            ft.TextButton('Confirm', on_click=lambda e: close_and_reset()),
        ]

    def restore_form():
        modal.confirming = False
        build_form()
        page.update()

    def close_and_reset():
        modal.open = False
        page.update()

    def close_modal():
        # If form is empty, just close
        if not any([
            title_input.value.strip(),
            category_input.value.strip(),
            ingredients_input.value.strip(),
            instructions_input.value.strip()
        ]):
            modal.open = False
            page.update()
            return

        # do nothing if confirmation is already ON
        if modal.confirming:
            return

        modal.confirming = True
        # Otherwise, ask for confirmation
        build_confirmation()
        page.update()

    def submit_recipe(e):
        has_error = False

        if not title_input.value:
            title_input.error_text = 'Required field. Please fill.'
            has_error = True
        else:
            title_input.error_text = None

        if not category_input.value:
            category_input.error_text = 'Required field. Please fill.'
            has_error = True
        else:
            category_input.error_text = None

        if has_error:
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
        close_and_reset()
        on_added_callback()

    build_form()

    if modal not in page.overlay:
        page.overlay.append(modal)

    modal.open = True
    page.update()
