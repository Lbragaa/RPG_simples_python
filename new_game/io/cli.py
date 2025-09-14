from typing import TYPE_CHECKING  # True only for type checkers/IDEs; False at runtime to avoid real imports
if TYPE_CHECKING:
    from new_game.models.player import Player  # Type-only import for hints; prevents runtime circular imports

def prompt_name() -> str:

    while True:
        name = input("How will you be known as in this journey?: ").strip()
        if name:
            return name
        print("Please enter a name.")

def print_player(player: "Player") -> None:
    crit_percent = player.stats.crit_chance * 100

    print(f"Name: {player.name} / Level: {player.level}")

    print(f"XP: {player.xp}/{player.xp_needed}")
    print(f"HP: {player.hp_current}/{player.stats.max_hp}")

    print(f"Atk: {player.stats.attack}")
    print(f"Def: {player.stats.defense}")
    print(f"Speed: {player.stats.speed}")
    print(f"Critical Hit Chance: {crit_percent:.2f}%")
    print(f"Crit Multiplier: {player.stats.crit_mult}")
