from pydantic import BaseModel
from typing import List,Type
from datetime import time


class Slot(BaseModel):
  availables: List[time] = []


class Person(BaseModel):
  id: int = None
  name: str = "No Name"
  slots: Slot


class Meeting(BaseModel):
  people: List[Person] = []


