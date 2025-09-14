from dataclasses import dataclass
from typing import Dict, Any
from new_game.models.stats import Stats

@dataclass(slots=False)
class Player:
    """A player. It contains a Stats object in it.
    - name: Name of the player
    - Stats: A Stats class object
    - Level: The current level of the player
    - xp: The current XP the player has
    - xp_needed: The XP necessary to reach the next level
    - hp_current: The current HP of the player
    """
    name: str
    stats: Stats
    level: int = 1
    xp: int = 0
    xp_needed: int = 8
    hp_current: int = 0 # will be set after init

    def to_dict(self) -> Dict[str, Any]:
            return {
                "name": self.name,
                "stats": self.stats.to_dict(),
                "level": self.level,
                "xp": self.xp,
                "xp_needed": self.xp_needed,
                "hp_current": self.hp_current,
            }


    def __post_init__(self) -> None:
        if self.hp_current <= 0:
            self.hp_current = self.stats.max_hp

#used to create a player from a dictionary (like when loading a save)
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Player":
        # Building the stats object from the nested dictionary, to then use it in the Player object
        stats= Stats.from_dict(data.get("stats", {}))
        return cls(
            name= str(data.get("name", "Default")),
            stats= stats,
            level=int(data.get("level", 1)),
            xp=int(data.get("xp", 0)),
            xp_needed=int(data.get("xp_needed", 8)),
            hp_current= int(data.get("hp_current", stats.max_hp)),
        )