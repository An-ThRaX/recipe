from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class Recipe(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    # foreigh key linking to Category table
    category_id: int = Field(foreign_key='category.id')
    category: Optional['Category'] = Relationship(back_populates='recipes')

    title: str
    ingredients: str
    instructions: str


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(unique=True)

    # Back reference to Recipe
    recipes: List['Recipe'] = Relationship(back_populates='category')
