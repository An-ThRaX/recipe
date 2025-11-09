from db import engine
from db.models import Category
from sqlalchemy import select
from sqlmodel import Session


def add_category(
        title: str
) -> None:
    with Session(engine) as session:
        category = Category(
            title=title,
        )
        session.add(category)
        session.commit()


def fetch_all_categories():
    with Session(engine) as session:
        categories = session.exec(
            select(Category)
        ).scalars().all()

        return categories
