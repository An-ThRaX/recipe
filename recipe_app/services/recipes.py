import random
import string

from db import engine
from db.models import Recipe
from flet import ControlEvent
from sqlalchemy import select
from sqlmodel import Session


def random_string(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))


# this will have to be used as the add btn on a formular
def add_recipe(
    title: str,
    ingredients: str,
    instructions: str,
) -> None:
    with Session(engine) as session:
        recipe = Recipe(
            title=title,
            ingredients=ingredients,
            instructions=instructions
        )
        session.add(recipe)
        session.commit()


# this will be used as temp btn
def add_pseudo_recipe(e: ControlEvent) -> None:
    with Session(engine) as session:
        recipe = Recipe(
            title=random_string(5),
            ingredients=random_string(10),
            instructions=random_string(10)
        )
        session.add(recipe)
        print(f'recipe {recipe.title} added')
        session.commit()


def fetch_all_recipes():
    with Session(engine) as session:
        recipes = session.exec(
            select(Recipe)
        ).scalars().all()
        return [
            {
                'title': r.title,
                'description': r.ingredients,
            }
            for r in recipes
        ]
