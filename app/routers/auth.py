from fastapi import APIRouter, Depends, Query
from fastapi.security import OAuth2PasswordRequestForm
from app.models.schemas import UserCreate, Token, SelectJob
from app.services.user_service import create_user, authenticate_user


router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup", response_model=Token)
def signup(data: UserCreate, job: SelectJob = Query(..., description="Select Class")):
    token = create_user(data, job)
    return {"access_token": token}

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    token = authenticate_user(form_data.username, form_data.password)
    return {"access_token": token, "token_type": "bearer"}