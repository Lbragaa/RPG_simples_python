from new_game.io.cli import prompt_name, print_player
from new_game.models.player import Player
from new_game.models.stats import Stats


def create_new_player():

    name = prompt_name()

    # Arguments: 
    stats = Stats(10, 3, 0, 10)

    return Player(name, stats, 1, 0, 8, 0)


def main():

    p1 = create_new_player()

    print_player(p1)


if __name__ == "__main__":
    main()