from fastapi import APIRouter, Query, Depends, HTTPException
from app.models.enum import Slot, Boss
from app.models.schemas import ItemOut, User
from app.services.item_service import generate_item
from app.routers.users import get_current_user
from app.core.config import settings


router = APIRouter(prefix="/items", tags=["Items"])
DB_PATH = settings.db_dir / "database.db"
    
@router.get("/generate", response_model=ItemOut)
def generate(
    slot: Slot = Query(..., description="Escolha o tipo de equipamento"),
    boss: Boss = Query(..., description="Escolha o Boss"),
    current_user: User = Depends(get_current_user)
):
    try:
        item = generate_item(
            user_id=current_user.id,
            job=current_user.job,
            piece_type=slot.value,
            boss_name=boss.value,
            db_path=DB_PATH
        )
        return item
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))