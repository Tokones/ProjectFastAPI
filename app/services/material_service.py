import sqlite3
from app.core.config import settings
from app.models.schemas import MaterialOut
from app.data.item_data import ammount_materials
from typing import List


db_path = settings.db_path

class MaterialRepository:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def get_quantity(self, id: int, boss: str) -> int:
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT quantity FROM materials
            WHERE id = ? AND boss = ?
        """, (id, boss))
        row = cursor.fetchone()
        conn.close()
        return row[0] if row else 0

    def add_quantity(self, id: int, boss: str) -> MaterialOut:
        current = self.get_quantity(id, boss)
        added = ammount_materials
        total = current + added

        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE materials
            SET quantity = ?
            WHERE id = ? AND boss = ?
            RETURNING id, boss, quantity
        """, (total, id, boss))
        row = cursor.fetchone()
        conn.commit()
        conn.close()

        return MaterialOut(id=row[0], boss=row[1], quantity=row[2])
    
    def get_more_materials(self, id: int, boss: str) -> List[MaterialOut]:
        atualizado = self.add_quantity(id, boss)
        return [atualizado]