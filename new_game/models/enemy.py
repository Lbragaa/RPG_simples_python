# Milestone 2 blueprint: Enemy model (comments only)
# Replace these commented lines with real code when you implement.

# 1) Imports

from dataclasses import dataclass
from typing import Dict, Any
from new_game.models.stats import Stats  # reuse the same Stats as Player

# 2) Dataclass definition
@dataclass
class Enemy:
    """A single enemy instance in combat.
    - name: the display name (e.g., "Goblin Scout")
    - kind: archetype identifier (e.g., "goblin", "vampire")
    - stats: combat stats (hp, atk, def, spd, crit)
    - xp_to_give: XP rewarded upon defeat
    - hp_current: current HP (initialized to stats.max_hp)
    """
    name: str
    kind: str
    stats: Stats
    xp_to_give: int
    hp_current: int = 0

    def __post_init__(self) -> None:
        if self.hp_current <= 0:
            self.hp_current = self.stats.max_hp

# 3) Serialization helpers (JSON-friendly)
    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "kind": self.kind,
            "stats": self.stats.to_dict(),
            "xp_to_give": self.xp_to_give,
            "hp_current": self.hp_current,
        }

#     @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Enemy":
        stats = Stats.from_dict(data.get("stats", {}))
        return cls(
            name=str(data.get("name", "Enemy")),
            kind=str(data.get("kind", "unknown")),
            stats=stats,
            xp_to_give=int(data.get("xp_to_give", 5)),
            hp_current=int(data.get("hp_current", stats.max_hp)),
        )

# 4) Notes on design
# - Prefer one generic Enemy class plus a "kind" field and data-driven stats from JSON.
# - Only create subclasses if behavior truly differs (e.g., special AI/skills).
# - For MVP, a single Enemy class is enough and simpler to test.

