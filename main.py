from new_game.io.cli import prompt_name, print_player, print_enemy, print_combat_log, prompt_action
from new_game.models.player import Player
from new_game.models.enemy import Enemy
from new_game.models.stats import Stats
from new_game.systems.combat import roll_initiative, player_attack, enemy_attack
import random


def create_new_player():

    name = prompt_name()

    # Arguments: 
    stats = Stats(10, 3, 0, 10)

    return Player(name, stats, 1, 0, 8, 0)


def main():

    p1 = create_new_player()

    print_player(p1)

    enemy1 = Enemy("Goblin", kind = "goblin", stats = Stats(10, 3, 0, 10), xp_to_give= 8 )

    print_enemy(enemy1)

    rng = random.Random(42)

    turn_counter = 1

    while p1.hp_current > 0 and enemy1.hp_current > 0:

        print(f"\nTurn {turn_counter}:")

        first = roll_initiative(p1,enemy1,rng)
        
        if first == "player":

            #Player acts first
            acted = False

            while not acted:

                action = prompt_action()
                if action == 's':
                    print_player(p1)
                    continue
                elif action == 'a':
                    log = player_attack(p1, enemy1, rng)
                    print_combat_log(log)
                    acted = True
                elif action == 'd':
                    #There is no defend for now but will be implemented
                    acted = True

            #Enemy turn

            if enemy1.hp_current <= 0:
                break

            log = enemy_attack(enemy1,p1, rng)
            print_combat_log(log)

        else:
            #Enemy acts first
            log = enemy_attack(enemy1, p1, rng)
            print_combat_log(log)

            if p1.hp_current <= 0:
                break

            # Player turn
            acted = False

            while not acted:

                action = prompt_action()
                if action == 's':
                    print_player(p1)
                    continue
                elif action == 'a':
                    log = player_attack(p1, enemy1, rng)
                    print_combat_log(log)
                    acted = True
                elif action == 'd':
                    #There is no defend for now but will be implemented
                    acted = True
        
        turn_counter += 1

    if p1.hp_current > 0:
        print(f"You've defeated {enemy1.name} and gained {enemy1.xp_to_give} xp!")
    else:
        print(f"You have perished by the hands of {enemy1.name}...")




if __name__ == "__main__":
    main()