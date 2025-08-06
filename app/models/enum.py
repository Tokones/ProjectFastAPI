from enum import Enum, StrEnum
from app.data.item_data import char_job, item_model, boss_names


Slot = Enum("type", {name: name for name in item_model})

Boss = Enum("boss", {name: name for name in boss_names})

Job = StrEnum("Job", {name: name for name in char_job})