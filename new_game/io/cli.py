from typing import TYPE_CHECKING  # True only for type checkers/IDEs; False at runtime to avoid real imports
if TYPE_CHECKING:
    from new_game.models.player import Player
    from new_game.models.enemy import Enemy  # Type-only import for hints; prevents runtime circular imports

def prompt_name() -> str:

    while True:
        name = input("How will you be known as in this journey?: ").strip()
        if name:
            return name
        print("Please enter a name.")

def print_player(player: "Player") -> None:
    crit_percent = player.stats.crit_chance * 100

    print(f"\nName: {player.name} / Level: {player.level}")

    print(f"XP: {player.xp}/{player.xp_needed}")
    print(f"HP: {player.hp_current}/{player.stats.max_hp}")

    print(f"Atk: {player.stats.attack}")
    print(f"Def: {player.stats.defense}")
    print(f"Speed: {player.stats.speed}")
    print(f"Critical Hit Chance: {crit_percent:.2f}%")
    print(f"Crit Multiplier: {player.stats.crit_mult}")

def print_enemy(enemy: "Enemy") -> None:

    crit_percent = enemy.stats.crit_chance * 100

    print(f"\nName: {enemy.name}")

    print(f"HP: {enemy.hp_current}/{enemy.stats.max_hp}")

    print(f"Atk: {enemy.stats.attack}")
    print(f"Def: {enemy.stats.defense}")
    print(f"Speed: {enemy.stats.speed}")
    print(f"Critical Hit Chance: {crit_percent:.2f}%")
    print(f"Crit Multiplier: {enemy.stats.crit_mult}")
    
def print_combat_log(log: dict) -> None:

    # Log esperado:
    # log = {"actor" : enemy.name, "dmg" : final_dmg, "crit" : crit, "player_hp" : player.hp_current}
    # Print here
    if log["crit"]:
        print(f"\n{log['actor']} dealt {log['dmg']} damage with a critical hit!\nRemaining HP for {log["target"]}: {log["target_hp"]}")
    else:
        print(f"\n{log['actor']} dealt {log['dmg']} damage!\nRemaining HP for {log["target"]}: {log["target_hp"]}")

def prompt_action() -> str:
    accepted_moves = ['a','d','s']
    while True:
        action = input("\nWhat is your desired action?\na/attack, d/defend, s/stats: ").lower()
        if action in accepted_moves:
            return action
        print("Please input a valid action")