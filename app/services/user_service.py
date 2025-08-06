import sqlite3
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings
from app.core.security import get_password_hash, verify_password, create_access_token, decode_access_token
from app.models.schemas import UserBase, UserCreate, SelectJob
from app.data.job_start import gear_preset
from app.data.item_data import material_start


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

DB_PATH = settings.db_dir / "database.db"

def _get_connection():
    return sqlite3.connect(DB_PATH)

def create_user(payload: UserCreate, job: SelectJob) -> str:
    conn = _get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users WHERE User = ?", (payload.user,))
    if cursor.fetchone()[0] > 0:
        conn.close()
        raise HTTPException(status_code=400, detail="Username taken")

    cursor.execute("SELECT MAX(ID) FROM users")
    max_id = cursor.fetchone()[0]
    next_id = max_id + 1 if max_id is not None else 1

    hashed = get_password_hash(payload.password)
    cursor.execute(
        "INSERT INTO users (ID, User, Job, Gold, Exp, Level, Password) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (next_id, payload.user, job.job.value, 0, 0, 1, hashed)
    )

    gear = gear_preset[job.job.value]
    gear_values = [next_id]

    for slot in ["Helmet", "Armor", "Pants", "Boots", "Weapon_Main", "Weapon_Sub"]:
        item = gear[slot]
        gear_values.extend([item["name"], item["level"], item["rarity"]])

    cursor.execute("""
        INSERT INTO gear (
            ID,
            Helmet, Helmet_Level, Helmet_Rarity,
            Armor, Armor_Level, Armor_Rarity,
            Pants, Pants_Level, Pants_Rarity,
            Boots, Boots_Level, Boots_Rarity,
            Weapon_Main, Weapon_Main_Level, Weapon_Main_Rarity,
            Weapon_Sub, Weapon_Sub_Level, Weapon_Sub_Rarity
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, tuple(gear_values))

    for boss, quantity in material_start.items():
            cursor.execute(
                "INSERT INTO materials (id, boss, quantity) VALUES (?, ?, ?)",
                (next_id, boss, quantity))


    conn.commit()
    conn.close()

    token = create_access_token({"user_id": next_id})
    return token

def authenticate_user(username: str, password: str) -> str:
    conn = _get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT ID, Password FROM users WHERE User = ?", (username,))
    row = cursor.fetchone()
    conn.close()

    if not row or not verify_password(password, row[1]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    user_id = int(row[0])
    return create_access_token({"user_id": user_id})

def get_current_user(token: str = Depends(oauth2_scheme)) -> UserBase:
    try:
        payload = decode_access_token(token)
        user_id = payload.get("user_id")

        conn = _get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT ID, User, Job, Gold, Exp, Level FROM users WHERE ID = ?", (user_id,))
        row = cursor.fetchone()

        conn.close()

        if not row:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuário não encontrado"
            )


        return UserBase(id=row[0], user=row[1], job=row[2], gold=row[3], exp=row[4], level=row[5])

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )