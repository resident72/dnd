import os, time, random
from colorama import Fore, Style, init

init()

def clear(timer=0):
    time.sleep(timer)
    os.system("cls")

class Player:
    def __init__(self, name, health, strength, defense, dexterity):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.dexterity = dexterity

    def __str__(self):
        return f"{self.name}, {self.strength}, {self.health}, {self.defense}, {self.dexterity}"

print(f"[1] {Fore.WHITE}Vanguard: Health: {Fore.GREEN}25{Style.RESET_ALL}  Strength: {Fore.RED}15{Style.RESET_ALL}  Defense: {Fore.BLUE}25{Style.RESET_ALL}  Dexterity: {Fore.YELLOW}10{Style.RESET_ALL}\n"
      f"[2] {Fore.WHITE}Warrior: Health: {Fore.GREEN}20{Style.RESET_ALL}  Strength: {Fore.RED}20{Style.RESET_ALL}  Defense: {Fore.BLUE}15{Style.RESET_ALL}  Dexterity: {Fore.YELLOW}15{Style.RESET_ALL}\n"
      f"[3] {Fore.WHITE}Thief: Health: {Fore.GREEN}15{Style.RESET_ALL}  Strength: {Fore.RED}10{Style.RESET_ALL}  Defense: {Fore.BLUE}10{Style.RESET_ALL}  Dexterity: {Fore.YELLOW}30{Style.RESET_ALL}\n"
      f"[4] {Fore.WHITE}Slave: Health: {Fore.GREEN}10{Style.RESET_ALL}  Strength: {Fore.RED}5{Style.RESET_ALL}  Defense: {Fore.BLUE}5{Style.RESET_ALL}  Dexterity: {Fore.YELLOW}5{Style.RESET_ALL}")

class_choice = int(input("Choose a bitch:" ))
clear()

if class_choice == 1:
    player = Player("Vanguard", 25, 15, 25, 10)
elif class_choice == 2:
    player = Player("Warrior", 20, 20, 15, 15)
elif class_choice == 3:
    player = Player("Thief", 15, 10, 10, 30)
elif class_choice == 4:
    player = Player("Slave", 10, 5, 5, 5)

print(f"You chose the {player.name}!\n")
clear(2)

def print_stats():
    print(f"Health: {player.health}\nStrength: {player.strength}\nDefense: {player.defense}\nDexterity: {player.dexterity}")


def choices():
    choice = int(input("[1]\n,[2]\n,[3]\n[4]"))


while True:    
    print("You wake up in a random hole with nothing on your ass, you see some pants on the ground, do you take em or not?")
    choice = int(input("[1] Take the pants and put em on \n[2] Stay butt ass naked\n"))
    os.system("cls")
    if choice == 1:
        player.defense += 1
        print("Your ass is covered [+ 1 Defense]")
    elif choice == 2:
        player.health -= 1
        print("Your ass shivers [-1 Health]")
    else:
        print("[!]DUMBASS YOU GOT TO SAY 1 OR 2, HOW CLUELESS CAN YOU GET?[!]")
        continue
    print_stats()
    break






'''
classes = {
    1: {"name": "Vanguard", "health": 25, "strength": 15, "defense": 25, "dexterity": 10},
    2: {"name": "Warrior",  "health": 20, "strength": 20, "defense": 15, "dexterity": 15},
    3: {"name": "Thief",    "health": 15, "strength": 10, "defense": 10, "dexterity": 30},
    4: {"name": "Slave",    "health": 10, "strength": 5,  "defense": 5,  "dexterity": 5}
}
'''
