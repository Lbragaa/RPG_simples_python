# Milestone 1 blueprint: Stats model (comments only)
# Replace these commented lines with real code when you implement.

# 1) Imports
from dataclasses import dataclass
from typing import Dict, Any

# 2) Dataclass definition
@dataclass(slots=False)
class Stats:
    """Core combat stats for a character.
    - max_hp: total health capacity
    - attack: base attack power
    - defense: flat damage reduction
    - speed: turn order priority
    - crit_chance: 0.05 means 5% chance
    - crit_mult: 1.5 means +50% damage on crit
    """
    max_hp: int
    attack: int
    defense: int
    speed: int
    crit_chance: float = 0.05
    crit_mult: float = 1.5

# 3) Serialization helpers (JSON-friendly)
#     Turn the dataclass into a simple dict and back.
#     These will be used by save/load later.
#     Keep names stable to avoid migration headaches.


# Ele torna o stats de maneira mais simples como um dicionario.
    def to_dict(self) -> Dict[str, Any]:
        return {
            "max_hp": self.max_hp,
            "attack": self.attack,
            "defense": self.defense,
            "speed": self.speed,
            "crit_chance": self.crit_chance,
            "crit_mult": self.crit_mult,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Stats":
        return cls(
            max_hp=int(data.get("max_hp", 10)),
            attack=int(data.get("attack", 3)),
            defense=int(data.get("defense", 0)),
            speed=int(data.get("speed", 10)),
            crit_chance=float(data.get("crit_chance", 0.05)),
            crit_mult=float(data.get("crit_mult", 1.5)),
        )

# 4) Suggested defaults for a new Player
#     When you create a new player in main.py, you can start with:
#     Stats(max_hp=10, attack=3, defense=0, speed=10)

# 5) Example usage (replace comments with real code when implementing)
#     from models.stats import Stats
#     base_stats = Stats(max_hp=10, attack=3, defense=0, speed=10)
#     print(base_stats.to_dict())
