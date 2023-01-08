from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    email: str
    role: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
