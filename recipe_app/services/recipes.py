from db import engine
from db.models import Recipe
from sqlmodel import Session
from flet import ControlEvent

import random
import string

def random_string(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))


# this will have to be used as the add btn on a formular
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

# this will be used as temp btn
def add_pseudo_recipe(e: ControlEvent):
    with Session(engine) as session:
        recipe= Recipe(
            title=random_string(5),
            ingredients=random_string(10),
            instructions=random_string(10)
        )
        session.add(recipe)
        print(f'recipe {recipe.title} added')
        session.commit()
