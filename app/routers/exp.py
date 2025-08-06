from fastapi import APIRouter
from typing import List
from app.models.schemas import ExpLevel
from app.services.exp_service import get_exp_table


router = APIRouter(prefix="/exp", tags=["exp"])

@router.get("/exp", response_model=List[ExpLevel])
def exp_needed_per_level():
    return get_exp_table()