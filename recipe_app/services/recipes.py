from db import engine
from db.models import Recipe
from sqlmodel import Session


def add_recipe(
    title: str,
    ingredients: str,
    instructions: str,
):
    with Session(engine) as session:
        recipe = Recipe(
            title=title,
            ingredients=ingredients,
            instructions=instructions
        )
        session.add(recipe)
        session.commit()
