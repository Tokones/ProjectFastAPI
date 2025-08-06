from fastapi import APIRouter, Depends, Query, HTTPException
from typing import List
from app.models.enum import Boss
from app.models.schemas import MaterialOut, User
from app.services.material_service import MaterialRepository
from app.services.user_service import get_current_user
from app.core.config import settings


DB_PATH = settings.db_path
router = APIRouter(prefix="/materials", tags=["materials"])

@router.get("/killboss", response_model=List[MaterialOut])
def kill_boss(current_user: User = Depends(get_current_user), 
              boss: Boss = Query(..., description="Select Boss")):
    try:
        inst = MaterialRepository(DB_PATH)
        item = inst.get_more_materials(
            id=current_user.id,
            boss=boss.value,
        )
        return item
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))