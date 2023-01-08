from sqlalchemy import Integer, String, DateTime, Column, JSON
from sqlalchemy.sql import func
from .database import Base

class User(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key = True, index = True)
  email = Column(String, unique = True, index = True)
  role = Column(String)
  created_at = Column(DateTime(timezone=True), server_default=func.now())
  updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Recipe(Base):
  __tablename__ = "recipes"
  id = Column(Integer, primary_key = True, index = True)
  title = Column(String)
  slug = Column(String, unique = True, index = True)
  content = Column(String)
  ingredients = Column(JSON)
  flavorings = Column(JSON)
  created_at = Column(DateTime(timezone=True), server_default=func.now())
  updated_at = Column(DateTime(timezone=True), onupdate=func.now())
