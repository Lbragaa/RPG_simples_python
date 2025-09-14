# Milestone 2 blueprint: Combat system (comments only)
# Replace these commented lines with real code when you implement.

# 1) Purpose
#   Pure functions that implement combat math and turn flow.
#   No input()/print() here — keep IO in io/cli.py.

# 2) Suggested imports

import random
from new_game.models.stats import Stats
from new_game.models.player import Player
from new_game.models.enemy import Enemy

# 3) RNG pattern
#   Accept a random.Random (or compatible) instance as a parameter (rng)
#   so you can seed it in tests. Avoid using random module globals directly.

# 4) Initiative
def roll_initiative(player: Player, enemy: Enemy, rng: "random.Random") -> str:
    """Return 'player' or 'enemy' based on speed (with small randomness).
    Example approach:
    - player_roll = player.stats.speed + rng.randint(0, 2)
    - enemy_roll  = enemy.stats.speed + rng.randint(0, 2)
    - tie-breaker: rng.choice(['player','enemy'])
    """

    player_roll = player.stats.speed + rng.randint(0,2)
    enemy_roll = enemy.stats.speed + rng.randint(0,2)

    if player_roll > enemy_roll:
        return "player"
    elif enemy_roll > player_roll:
        return "enemy"
    return rng.choice(['player','enemy'])

#     ...

# 5) Damage calculation
def calc_damage(attacker: Stats, defender: Stats, rng: "random.Random") -> tuple[int, bool]:
    """Compute damage and whether it crit.
    Suggested:
    - base = max(0, attacker.attack - defender.defense)
    - crit = rng.random() < attacker.crit_chance
    - dmg = int(base * attacker.crit_mult) if crit else base
    - Return (max(0, dmg), crit)
    """
    # We already expect to receive their Stats object
    base_dmg = max(0, attacker.attack - defender.defense)
    crit_bool = rng.random() < attacker.crit_chance
    dmg = int(base_dmg * attacker.crit_mult if crit_bool else base_dmg)

    #maybe use the crit bool to display a crit message?...
    return (max(0,dmg), crit_bool)

# 6) Apply damage
def apply_damage(hp_current: int, dmg: int) -> int:
    """Return new HP after applying damage (bounded at 0)."""
    return max(0, hp_current - dmg)

# 7) Turn resolution (MVP)

# These functions are useless being separate right now but I will change this later

def player_attack(player: Player, enemy: Enemy, rng: "random.Random") -> dict:
    """Resolve the player's basic attack.
    - Use calc_damage(player.stats, enemy.stats, rng)
    - Update enemy.hp_current
    - Return a dict log: {"actor":"player","dmg":X,"crit":bool,"enemy_hp":Y}
    """
    
    final_dmg, crit = calc_damage(player.stats, enemy.stats, rng)
    enemy.hp_current = apply_damage(enemy.hp_current, final_dmg)

    log = {"actor" : player.name,"target" : enemy.name, "dmg" : final_dmg, "crit" : crit, "target_hp" : enemy.hp_current}
    return log

def enemy_attack(enemy: Enemy, player: Player, rng: "random.Random") -> dict:
    """Resolve the enemy's basic attack.
    - Use calc_damage(enemy.stats, player.stats, rng)
    - Update player.hp_current
    - Return a dict log: {"actor":"enemy","dmg":X,"crit":bool,"player_hp":Y}
    """
    final_dmg, crit = calc_damage(enemy.stats, player.stats, rng)
    player.hp_current = apply_damage(player.hp_current, final_dmg)

    log = {"actor" : enemy.name, "target" : player.name, "dmg" : final_dmg, "crit" : crit, "target_hp" : player.hp_current}
    return log

# 8) Notes
# - Keep these functions small and deterministic.
# - The game loop in main.py (or a Game class later) decides what action to call.
# - For now, only implement basic attack; add defend/items later.

