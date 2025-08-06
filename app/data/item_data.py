boss_names = ["Wyvern", "Golem", "Banshee", "Widowmaker", "Gigantes"]

boss_prefixes = {
    "Wyvern": ["Dragon", "Skyborn", "Scaled"],
    "Golem": ["Titan", "Obsidian", "Mechanized"],
    "Banshee": ["Ethereal", "Phantom", "Cursed"],
    "Widowmaker": ["Shadow", "Venom", "Silken"],
    "Gigantes": ["Monster", "Colossal", "Brutal"]
}

boss_suffixes = {
    "Wyvern": ["of Abyss", "of Eternal Flame", "of the Storm"],
    "Golem": ["of Stoneguard", "MK-III", "of Iron Will"],
    "Banshee": ["of the Abyss", "of Lost Souls", "of the Veil"],
    "Widowmaker": ["of Tarantula", "of the Weaver", "of Widow"],
    "Gigantes": ["of the Juggernaut", "of the Primordial", "of the Earthshaker"]
}

rarity_weights = {
    "Common": 65,
    "Rare": 20,
    "Epic": 10,
    "Legendary": 5,
}

level_up_chance = {
    "Common": 0.01,
    "Rare": 0.03,
    "Epic": 0.09,
    "Legendary": 0.18
}

rarity_order = ["Common", "Rare", "Epic", "Legendary"]

char_job = ["Warrior", "Archer", "Wizard", 
            "Scholar", "Berserker", "Assassin", 
            "Priest", "Paladin"
]

item_model = ["Helmet", "Armor", "Pants", "Boots", "Weapon_Main", "Weapon_Sub"]

weapon_main = {
    "Warrior": "Greatsword",
    "Archer": "Bow",
    "Wizard": "Staff",
    "Scholar": "Tome",
    "Berserker": "Dual-Axe",
    "Assassin": "Dual-Dagger",
    "Priest": "Wand",
    "Paladin": "Mace",
}

weapon_sub = {
    "Warrior": "Gauntlet",
    "Archer": "Hand-Grip",
    "Wizard": "Crystal",
    "Scholar": "Lantern",
    "Berserker": "Knot",
    "Assassin": "Trinket",
    "Priest": "Rosary",
    "Paladin": "Shield",
}

piece_head = {
    "Warrior": "Helm",
    "Archer": "Hood",
    "Wizard": "Circlet",
    "Scholar": "Turban",
    "Berserker": "Headguard",
    "Assassin": "Mask",
    "Priest": "Halo",
    "Paladin": "Crown",
}

piece_armor = {
    "Warrior": "Chestplate",
    "Archer": "Jerkin",
    "Wizard": "Robe",
    "Scholar": "Tunic",
    "Berserker": "Warplate",
    "Assassin": "Vest",
    "Priest": "Raiment",
    "Paladin": "Cuirass",
}

piece_pants = {
    "Warrior": "Greaves",
    "Archer": "Leggings",
    "Wizard": "Trousers",
    "Scholar": "Slacks",
    "Berserker": "Warleggings",
    "Assassin": "Striders",
    "Priest": "Vestments",
    "Paladin": "Platelegs",
}

piece_boots = {
    "Warrior": "Sabatons",
    "Archer": "Boots",
    "Wizard": "Sandals",
    "Scholar": "Slippers",
    "Berserker": "Warboots",
    "Assassin": "Footwraps",
    "Priest": "Heels",
    "Paladin": "Greaves",
}

gear_map = {
    "Weapon_Main": weapon_main,
    "Weapon_Sub": weapon_sub,
    "Helmet": piece_head,
    "Armor": piece_armor,
    "Pants": piece_pants,
    "Boots": piece_boots
}

ammount_materials = +500

material_start = {
    "Wyvern": 0,
    "Golem": 0,
    "Banshee": 0, 
    "Widowmaker": 0,
    "Gigantes": 0
}