
from db import engine
from db.models import Recipe
from sqlalchemy import select
from sqlmodel import Session


# this will have to be used as the add btn on a formular
def add_recipe(
    title: str,
    category_id: int,
    ingredients: str,
    instructions: str,
) -> None:
    with Session(engine) as session:
        recipe = Recipe(
            title=title,
            category_id=category_id,
            ingredients=ingredients,
            instructions=instructions
        )
        session.add(recipe)
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
