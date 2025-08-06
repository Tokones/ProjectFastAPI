from fastapi import APIRouter, Depends
from app.models.schemas import User, MaterialOut
from app.models.enum import Boss
from typing import List
from app.services.user_service import get_current_user
from app.services.material_service import MaterialRepository
from app.core.config import settings


DB_PATH = settings.db_path

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/char", response_model=User)
def user_info(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/mats", response_model=List[MaterialOut])
def check_materials(current_user: User = Depends(get_current_user)):
    inst = MaterialRepository(DB_PATH)

    result = []
    for boss in Boss:
        mat_quant = inst.get_quantity(current_user.id, boss.value)
        result.append(MaterialOut(id=current_user.id, boss=boss.value, quantity=mat_quant))
    return result