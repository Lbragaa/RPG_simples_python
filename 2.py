import random
from random import randint as randint
import math
import time

battle_now = True
goblin_Names = [
    "Alymurh", "Dalys", "Sarkath", "Khmaz", "Kerin", "The Strongest Goblin", "Calothosk", "Gorgandr","Kolloth", "Gordhon", "Kykes"]

# self,hp,strength,speed,defense
def rolldie(max):
    n = randint(1, max)
    return n

class Player:
    def __init__(self):

        #Basic stats
        self.alive = True
        self.name = input("What will your name be?: ")
        self.level = 1
        self.originhp = 10
        self.hp = 10
        self.attack = 3
        self.speed = 10
        self.defense = 0

        # Equipment
        self.weaponname = "Random dagger"
        self.weaponpower = 0
        self.fullattack = self.attack + self.weaponpower

        #Crit
        self.critNeed = 20
        self.die = 20
        #Level UP
        self.currentXp = 0
        self.neededXp = 5
        if self.hp <= 0:
            self.alive = False

    def ShowStats(self):
        print("Your current stats are:")
        time.sleep(0.8)
        print(f"""
Name: {self.name}
Level: {self.level}\n
Total Health: {self.originhp}
Current Health: {self.hp}
Weapon: {self.weaponname} / Power: {self.weaponpower}
Attack: {self.fullattack} (+{self.weaponpower})
Speed: {self.speed}
Defense: {self.defense}\n""")

    def P_attack(self, Edefense):
        nA = rolldie(self.die)
        dmg = self.fullattack
        crit = self.critNeed
        print(f'You rolled a {nA}\n')
        time.sleep(1)
        if nA == 1:
            print("You missed your attack!\n")
            return 0
        elif nA in range(2, 10):
            ran = randint(1, 4)
            if ran == 4:
                dmg += 1
            print(f'You dealt {max(0, dmg - Edefense)} damage!\n')
            return max(0, dmg - Edefense)
        elif nA in range(10, 15):
            dmg += randint(0, 1)
            print(f'You dealt {max(0,dmg - Edefense)} damage!\n')
            return max(0,dmg - Edefense)
        elif nA in range(15, 18):
            ran = randint(1, 5)
            if ran in range(1, 5):
                dmg += 1
            print(f'You dealt {max(0,dmg - Edefense)} damage!\n')
            return max(0,dmg - Edefense)
        elif nA in range(18, crit):
            ran = randint(1, 5)
            if ran in range(1, 5):
                dmg += 1
            print(f'You dealt {max(0,dmg - Edefense)} damage!\n')
            return max(0,dmg - Edefense)
        elif nA >= crit:
            time.sleep(1)
            dmg += random.randint(1, 2)
            crit_dmg = math.ceil(dmg * 1.5) - Edefense
            print(f"You had a critical hit and dealt {max(0,crit_dmg)} damage!\n")
            return max(0,crit_dmg)
    def action(self):
        action = input("""What will you do, chosen one?: """)
        if action.lower() == "atk" or action.lower() == "attack":
            return self.P_attack(current_opponent.defense)
        elif action.lower() == "stats":
            return "stats"
        else:
            print("i don really kn what dat means. you doing nothing cuz of it")
            return 0

    def levelUp(self):
        accepted_words = ["hp", "atk", "def", "spd"]
        self.level += 1
        print(f"""Congrats! You have leveled up to level {self.level}!
|Choose a stat to upgrade|\n""")
        time.sleep(2.2)
        p1.lvlShowStats()
        decision = input("What stat would you like to improve?: (Hp, Atk, Def, Spd)\n").lower()
        while decision not in accepted_words:
            decision = input("What stat would you like to improve?: (Hp, Atk, Def, Spd)\n")
        if decision == "hp":
            self.originhp += 2
            print("Your HP has increased!\n")
        elif decision == "atk":
            self.attack += 1
            self.fullattack = self.attack + self.weaponpower
            print("Your Attack has increased!\n")
        elif decision == "def":
            self.defense += 1
            print("Your Defense has increased!\n")
        elif decision == "spd":
            self.speed += 1
            print("Your Speed has increased!\n")
        self.neededXp += 5
        self.currentXp = 0

    def lvlShowStats(self):
        print("Your current stats are:")
        print(f"""
Total Health: {self.originhp}
Attack: {self.fullattack} (+{self.weaponpower})
Speed: {self.speed}
Defense: {self.defense}\n""")
    def checklvlUp(self):
        if p1.currentXp >= p1.neededXp:
            p1.levelUp()

class Goblin_1:
    def __init__(self):
        self.alive = True
        self.name = random.choice(goblin_Names)
        self.race = "Goblin"
        self.attack = randint(1, 3)
        self.speed = randint(7, 12)
        self.hp = randint(5, 10)
        self.defense = 0
        self.xpToGive = 0
        if self.hp >= 8:
            self.xpToGive = 5
        else:
            self.xpToGive = 4
        if self.name == "The Strongest Goblin":
            self.hp = 20
            self.attack = randint(2, 4)
            self.defense = 1
        self.critNeed = 20
        self.die = 20
        if self.hp <= 0:
            self.alive = False

    def G_attack(self):
        nA = rolldie(self.die)
        dmg = self.attack
        crit = self.critNeed
        print(f"\nYour opponent is about to attack you...")
        time.sleep(2)
        if nA <= 2:
            print("Your opponent missed its attack!\n")
            return 0
        elif nA < 17:
            if (dmg - p1.defense) <= 0:
                print(f"Your opponent did zero damage!")
                return 0
            print(f'Your opponent dealt {dmg - p1.defense} damage!\n')
            return dmg - p1.defense
        elif nA in range(17,crit):
            dmg += randint(0,1)
            if (dmg - p1.defense) <= 0:
                print(f"Your opponent did zero damage!")
                return 0
            print(f'Your opponent dealt {dmg - p1.defense} damage!\n')
            return dmg - p1.defense
        else:
            dmg += 0.5
            if math.ceil(dmg * 1.5) - p1.defense <= 0:
                print(f"Your opponent did zero damage!")
                return 0
            print(f"Your opponent landed a critical hit and dealt {(math.ceil(dmg * 1.5)) - p1.defense} damage!\n")
            return (math.ceil(dmg * 1.5)) - p1.defense


class Goblin_2:
    def __init__(self):
        self.alive = True
        self.name = random.choice(goblin_Names)
        self.race = "Goblin"
        self.attack = randint(2, 4)
        self.speed = randint(7, 12)
        self.defense = 1
        self.hp = randint(7, 13)
        self.xpToGive = 0
        if self.hp >= 10:
            self.xpToGive = 6
        else:
            self.xpToGive = 5
        if self.name == "The Strongest Goblin":
            self.hp = 20
            self.attack = randint(4, 5)
            self.defense = randint(2, 3)
            self.speed = randint(7, 11)
            self.xpToGive = 12
        self.critNeed = 20
        self.die = 20
        if self.hp <= 0:
            self.alive = False

    def G_attack(self):
        nA = rolldie(self.die)
        dmg = self.attack + randint(0, 1)
        crit = self.critNeed
        print(f"\nYour opponent is about to attack you...")
        time.sleep(2)
        if nA <= 2:
            print("Your opponent missed its attack!\n")
            return 0
        elif nA < crit:
            if (dmg - p1.defense) <= 0:
                print(f"Your opponent did zero damage!")
                return 0
            print(f'Your opponent dealt {dmg - p1.defense} damage!\n')
            return dmg - p1.defense
        else:
            dmg += 0.5
            if math.ceil(dmg * 1.5) - p1.defense <= 0:
                print(f"Your opponent did zero damage!")
                return 0
            print(f"Your opponent landed a critical hit and dealt {(math.ceil(dmg * 1.5)) - p1.defense} damage!\n")
            return (math.ceil(dmg * 1.5)) - p1.defense


p1 = Player()

time.sleep(0.7)
p1.ShowStats()
time.sleep(2)
print("\nAn adventure awaits you! Are you ready?")
input()
time.sleep(0.2)
print("\nLet's begin...")

time.sleep(2)
current_opponent = e1 = Goblin_1()


def status_and_action(player_name, p_health, opponentName, o_health):
    global battle_now
    if p_health <= 0 or p1.alive == False:
        p1.alive = False
        time.sleep(1.5)
        print(f"You have perished by the hands of {opponentName}! You fought well, but... ")
        time.sleep(1.5)
        print("\nEND OF JOURNEY")
        exit()
    elif o_health <= 0 or current_opponent.alive == False:
        current_opponent.alive = False
        battle_now = False
        print(f"You have defeated your opponent, {opponentName}, the {current_opponent.race}!\n")
    else:
        time.sleep(1)
        print(f"""\n{opponentName}'s HP: {o_health}
Your current HP: {p_health}\n""")

class Swords:
    def __init__(self, power):
        self.name = f"{current_opponent.name}'s blade"
        self.power = power
        number = randint(1, 500)
        if number == 100:
            self.name = f"holy fuck that's a 0.2% chance weapon"
            self.power = 50
        elif current_opponent.name == "The Strongest Goblin":
            self.name = f"Gabiritos's the Great grand blade"
            self.power = 5

def battling():
    global battle_now
    battle_now = True
    p1.hp = p1.originhp
    if (p1.speed < current_opponent.speed) and current_opponent.alive:
        time.sleep(1.5)
        print("\nYour opponent is faster than you and will move first!")
    while battle_now:
        if p1.speed >= current_opponent.speed:
            time.sleep(1)
            status_and_action(p1.name, p1.hp, current_opponent.name, current_opponent.hp)
            action = p1.action()
            if action == "stats":
                time.sleep(1)
                p1.ShowStats()
                continue
            current_opponent.hp = current_opponent.hp - action
            time.sleep(2)
            status_and_action(p1.name, p1.hp, current_opponent.name, current_opponent.hp)
            if current_opponent.alive:
                p1.hp = p1.hp - current_opponent.G_attack()
        else:
            time.sleep(2)
            status_and_action(p1.name, p1.hp, current_opponent.name, current_opponent.hp)
            time.sleep(0.5)
            p1.hp = p1.hp - current_opponent.G_attack()
            yourturn = True
            while yourturn:
                status_and_action(p1.name, p1.hp, current_opponent.name, current_opponent.hp)
                action = p1.action()
                if action == "stats":
                    time.sleep(1)
                    p1.ShowStats()
                    continue
                current_opponent.hp = (current_opponent.hp - action)
                if current_opponent.hp <= 0 or current_opponent.alive == False:
                    status_and_action(p1.name, p1.hp, current_opponent.name, current_opponent.hp)
                yourturn = False
    else:
        print("Well done!\n")
        p1.hp = p1.originhp
        p1.currentXp = p1.currentXp + current_opponent.xpToGive
        p1.checklvlUp()


def checksword():
    time.sleep(3)
    print("You noticed that the goblin you just defeated dropped his weapon...")
    time.sleep(1)
    answer = input("Do you wish to take a look at it? (Y/N): \n")
    time.sleep(1)
    if answer.lower() == "y":
        print(f"""You observe the blade and notice the following:
Name: {sword1.name}
Attack power: {sword1.power}\n""")
        time.sleep(3)
        p1.ShowStats()
        answer = input("Would you like to take this weapon?: """)
        if answer.lower() == "y":
            print("You've got a new sword!\n")
            time.sleep(1.8)
            p1.weaponname = sword1.name
            p1.weaponpower = sword1.power
            p1.fullattack = p1.attack + p1.weaponpower
            p1.ShowStats()
    else:
        print(f"""You ignore the weapon without taking a single look. 
Interesting decision huh. """)


forest_first_battle = True
while forest_first_battle:
    current_opponent = e1 = Goblin_1()
    print(f"""As you venture through the greenery bushes, your gaze lands at a lonely boar sleeping in a nearby glade. An easy prey!
But before you can go after it...""")
    input()
    print(f"""You are surprised by your first opponent, a goblin named {current_opponent.name}! """)
    battling()
    forest_first_battle = False

second_event = True
while second_event:
    sword1 = Swords(randint(1, 2))
    checksword()
    question = input(f'Look for another goblin to fight?: (Note: these goblins will be a bit stronger :) ')
    while question.lower() == "y":
        current_opponent = Goblin_2()
        print(f"You will be fighting {current_opponent.name}!")
        battling()
        question = input(f'Look for another goblin to fight?: \n')
    if question.lower() == "n":
        print("Maybe some other time then")
    second_event = False