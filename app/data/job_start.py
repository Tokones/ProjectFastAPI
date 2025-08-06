import app.data.item_data as item_data


gear_preset = {}

for job in item_data.weapon_main:
    gear_preset[job] = {
        "Weapon_Main": {
            "name": f"Rusty {item_data.weapon_main[job]}",
            "level": 1,
            "rarity": "Common"
        },
        "Weapon_Sub": {
            "name": f"Faded {item_data.weapon_sub[job]}",
            "level": 1,
            "rarity": "Common"
        },
        "Helmet": {
            "name": f"Worn {item_data.piece_head[job]}",
            "level": 1,
            "rarity": "Common"
        },
        "Armor": {
            "name": f"Frayed {item_data.piece_armor[job]}",
            "level": 1,
            "rarity": "Common"
        },
        "Pants": {
            "name": f"Torn {item_data.piece_pants[job]}",
            "level": 1,
            "rarity": "Common"
        },
        "Boots": {
            "name": f"Scratched {item_data.piece_boots[job]}",
            "level": 1,
            "rarity": "Common"
        }
    }