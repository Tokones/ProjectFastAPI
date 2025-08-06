from pydantic import BaseModel
from app.models.enum import Job, Slot, Boss
from typing import Optional


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    user_id: Optional[int] = None

class UserBase(BaseModel):
    id: int
    user: str
    job: str
    gold: int
    exp: int
    level: int

class User(UserBase):
    pass

class UserCreate(BaseModel):
    user: str
    password: str
    
class SelectJob(BaseModel):
    job: Job

class ExpLevel(BaseModel):
    level: int
    exp: int

class ItemOut(BaseModel):
    name: str
    type: Slot
    boss: Boss
    level: int
    rarity: str
    
class MaterialOut(BaseModel):
    id: int
    boss: str
    quantity: int