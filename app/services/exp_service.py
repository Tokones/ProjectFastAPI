import sqlite3
from app.core.config import settings
from app.models.schemas import ExpLevel
from typing import List


DB_PATH = settings.db_dir / "database.db"

def _get_connection():
    return sqlite3.connect(DB_PATH)

def get_exp_table() -> List[ExpLevel]:
    conn = _get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT Level, Exp FROM exp ORDER BY Level ASC")
    rows = cursor.fetchall()
    conn.close()

    return [ExpLevel(level=row[0], exp=row[1]) for row in rows]