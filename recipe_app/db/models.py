from typing import Optional

from sqlmodel import Field, SQLModel


class Recipe(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    ingredients: str
    instructions: str


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
