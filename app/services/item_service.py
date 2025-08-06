from app.models.schemas import ItemOut
from app.core.config import settings
import app.data.item_data as item_data
import random
import sqlite3


db_path = settings.db_dir / "database.db"

def choose_prefix(boss_name: str) -> str:
    return random.choice(item_data.boss_prefixes.get(boss_name, [""]))

def choose_suffix(boss_name: str) -> str:
    return random.choice(item_data.boss_suffixes.get(boss_name, [""]))

def adjust_level(base_level: int, rarity: str) -> tuple[int, bool]:
    chance = item_data.level_up_chance.get(rarity, 0)
    level_up = random.random() < chance
    return (base_level + 1 if level_up else base_level, level_up)

def choose_rarity(min_rarity: str = "", force_common: bool = False) -> str:
    if force_common:
        return "Common"
    
    rarities = list(item_data.rarity_weights.keys())
    weights = list(item_data.rarity_weights.values())
    idx = rarities.index(min_rarity)
    return random.choices(rarities[idx:], weights[idx:], k=1)[0]

def generate_item(user_id: int, job: str, piece_type: str, boss_name: str, db_path) -> ItemOut:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(f"""
        SELECT {piece_type}_Level, {piece_type}_Rarity
        FROM gear
        WHERE ID = ?
    """, (user_id,))
    result = cursor.fetchone()

    base_level, base_rarity = result

    base_piece_name = item_data.gear_map[piece_type][job]
    prefix = choose_prefix(boss_name)
    suffix = choose_suffix(boss_name)
    full_name = f"{prefix} {base_piece_name} {suffix}"
    
    level_check, lv_up = adjust_level(base_level, base_rarity)
    new_level = int(level_check)

    new_rarity = choose_rarity(base_rarity, force_common=lv_up)


    cursor.execute(f"""
        UPDATE gear
        SET {piece_type} = ?, {piece_type}_Level = ?, {piece_type}_Rarity = ?
        WHERE ID = ?
    """, (full_name, new_level, new_rarity, user_id))

    conn.commit()
    conn.close()

    return ItemOut(
        name=full_name,
        type=piece_type,
        boss=boss_name,
        level=new_level,
        rarity=new_rarity
    )