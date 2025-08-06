import random
import sqlite3
from pathlib import Path
from app.data.item_data import boss_names


def generate_material_table(path: Path):
    db_file = path / "database.db"

    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT ID FROM users")
        ids = [row[0] for row in cursor.fetchall()]

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS materials (
                id INTEGER,
                boss TEXT,
                quantity INTEGER
            )
        """)

        for id in ids:
            for boss in boss_names:
                quantity = random.randint(100, 30000)
                cursor.execute(
                    "INSERT INTO materials (id, boss, quantity) VALUES (?, ?, ?)",
                    (id, boss, quantity)
                )

        conn.commit()

if __name__ == "__main__":
    path = Path(__file__).parent.parent.resolve() / "app" / "models"
    path.mkdir(exist_ok=True)
    generate_material_table(path)