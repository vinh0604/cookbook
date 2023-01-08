from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Ingredient: 
    name: str
    amount: Optional[int]
    unit: Optional[str]

class RecipeBase(BaseModel):
    title: str
    content: str
    ingredients: List[Ingredient] = []
    flavorings: List[str] = []

class Recipe(RecipeBase):
    id: int
    slug: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_model = True
