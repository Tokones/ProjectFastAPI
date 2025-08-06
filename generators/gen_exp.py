import numpy as np
import sqlite3
from pathlib import Path


def generate_exp_table_sql(path: Path):
    max_level = 70
    total_exp = 99_999_999
    exponent = 2

    levels = np.arange(2, max_level + 1)
    scaled_positions = np.linspace(0, 1, len(levels) + 2)[1:-1]
    weights = np.power(scaled_positions, exponent)
    weights /= weights.sum()
    exp_deltas = weights * total_exp

    exp_table = [(1, 0)]
    cumulative = 0
    for lvl, delta in zip(levels, exp_deltas):
        cumulative += delta
        exp_table.append((int(lvl), int(round(cumulative))))

    db_file = path / "database.db"
    db_file.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exp (
        Level INTEGER,
        Exp INTEGER
    )
    """)

    cursor.execute("DELETE FROM exp")
    cursor.executemany("INSERT INTO exp (Level, Exp) VALUES (?, ?)", exp_table)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    path = Path(__file__).parent.parent.resolve() / "app" / "models"
    path.mkdir(exist_ok=True)
    generate_exp_table_sql(path)