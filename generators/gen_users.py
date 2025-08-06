import random
import string
import sqlite3
from pathlib import Path
from app.data.item_data import char_job
from app.data.job_start import gear_preset
import pandas as pd


def generate_user():
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=random.randint(4, 8)))

def define_level(xp, exp_data):
    df = exp_data[exp_data.Exp <= xp]
    return int(df.Level.max()) if not df.empty else 1

def generate_job():
    return random.choice(list(char_job))

def generate_user_and_gear_tables_sql(path: Path):
    db_file = path / "database.db"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # 🧱 Criação das tabelas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        ID INTEGER PRIMARY KEY,
        User TEXT,
        Job TEXT,
        Gold INTEGER,
        Exp INTEGER,
        Level INTEGER,
        Password TEXT
        )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS gear (
        ID INTEGER,
        Helmet TEXT, Helmet_Level INTEGER, Helmet_Rarity TEXT,
        Armor TEXT, Armor_Level INTEGER, Armor_Rarity TEXT,
        Pants TEXT, Pants_Level INTEGER, Pants_Rarity TEXT,
        Boots TEXT, Boots_Level INTEGER, Boots_Rarity TEXT,
        Weapon_Main TEXT, Weapon_Main_Level INTEGER, Weapon_Main_Rarity TEXT,
        Weapon_Sub TEXT, Weapon_Sub_Level INTEGER, Weapon_Sub_Rarity TEXT
        )
    """)
    
    exp_df = pd.read_sql_query("SELECT * FROM exp", conn)

    users = {generate_user() for _ in range(500)}
    user_data = []
    gear_data = []

    for idx, name in enumerate(users, start=1):
        job = generate_job()
        gold = random.randint(0, 99_999_999)
        exp = random.randint(0, 99_999_999)
        level = define_level(exp, exp_df)
        password = ""

        user_data.append((idx, name, job, gold, exp, level, password))

    
        gear = gear_preset[job]

        gear_row = [idx]
        for slot in ["Helmet", "Armor", "Pants", "Boots", "Weapon_Main", "Weapon_Sub"]:
            item = gear[slot]
            gear_row += [item["name"], item["level"], item["rarity"]]

        gear_data.append(tuple(gear_row))

    # 💾 Inserção no banco
    cursor.execute("DELETE FROM users")
    cursor.execute("DELETE FROM gear")

    cursor.executemany("""INSERT INTO users (ID, User, Job, Gold, Exp, Level, Password)
                        VALUES (?, ?, ?, ?, ?, ?, ?)""", user_data)

    cursor.executemany("""
    INSERT INTO gear (
        ID,
        Helmet, Helmet_Level, Helmet_Rarity,
        Armor, Armor_Level, Armor_Rarity,
        Pants, Pants_Level, Pants_Rarity,
        Boots, Boots_Level, Boots_Rarity,
        Weapon_Main, Weapon_Main_Level, Weapon_Main_Rarity,
        Weapon_Sub, Weapon_Sub_Level, Weapon_Sub_Rarity
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, gear_data)

    conn.commit()
    conn.close()
    print(f"Tabelas users e gear geradas com sucesso em: {path / 'database.db'}")

if __name__ == "__main__":
    path = Path(__file__).parent.parent.resolve() / "app" / "models"
    path.mkdir(exist_ok=True)
    generate_user_and_gear_tables_sql(path)