#Add more options to combat (use item, run)
#Add a view inventory button
#Start the next area (town) and add the first quest
#Be able to save and load game progress eventually using json.
#Add as you go.
import random

class Player:

    def __init__(self, hp = 10, atk = 3):
        self.hp = hp
        self.atk = atk

    def dmgTaken(self, dmg):
        self.hp -= dmg


class Wolf:

    def __init__(self, hp = 12, dmg = 3, hitrate = 6, name = "Wolf"):
        self.hp = hp
        self.dmg = dmg
        self.name = name
        self.hitrate = hitrate

    def dmgTaken(self, atk):
        self.hp -= atk

class Bear:

    def __init__(self, hp = 25, dmg = 4, hitrate = 7, name = "Bear"):
        self.hp = hp
        self.dmg = dmg
        self.name = name
        self.hitrate = hitrate
        
    def dmgTaken(self, atk):
        self.hp -= atk 

class Dagger:

    def __init__(self, dmg = 2, name = "Dagger"):
        self.dmg = dmg
        self.name = name

    def equip(self, player):
        player.atk += self.dmg

    def unequip(self, player):
        player.atk -= self.dmg

    def __str__(self):
        return self.name

class Potion:

    def __init__(self, heal = 5, name = "Potion"):
        self.heal = heal
        self.name = name

    def healing(self, player):
        player.hp += self.heal
        input(f"Used {self.name}. You healed for {self.heal} health \n [Enter]")

    def __str__(self):
        return self.name
        




player = Player()
dagger = Dagger()
potion1 = Potion()
wolf1 = Wolf()



inventory = {1 : None , 2 : None, 3 : None, 4 : None, 5 : None}



def insert_item(item):

    for slot in inventory:    

        if inventory[slot] is None:
            inventory[slot] = item
            print(f"[Aquired {item}]")
            return

    print("Inventory is full")
    


def remove_item(item):

    for slot in inventory:

        if inventory[slot] == item:
            inventory[slot] = None
            print(f"[Dropped {item}]")
            return

    print("Nothing in slot")

def use_item():

    clear()
    show_inventory()
    choice = int(input("Use an item \n"))
    
    item = inventory[choice]

    if item == potion1:
        item.healing(player)
        return item
    else:
        input("Nothing usable in slot \n [Enter]")
        clear()
    

def show_inventory():

    print("{", end="")

    for slot, item in inventory.items():
        print(f"{slot}: {item}", end=" ")

    print("}")


def tutorial():

    while True:

        action = int(input("You wake up in strange room, there is a door in front of you, to your left is a strange hallway. \n 1. Try the door \n 2. Turn left into the hallway \n 0. Inventory \n"))

        match action:
            case 1:

                clear()

                if "key" in inventory.values():

                    clear()
                    remove_item("key")
                    input("The door unlocks. The opening is completely white, not allowing you to see anything. Letting your curiosity get the better of you, you step in. \n [Enter]")
                    print("[SYSTEM] TUTORIAL FINISHED")
                    return

                input("You try the door, it's locked. \n [Enter] Go back")
                clear()
            case 2: 

                clear()

                drawer = int(input("You turn left into the hallway. In front of you is a drawer. \n 1. Open the drawer \n 2. Go back \n "))

                match drawer:
                    case 1:
                        if "key" in inventory.values():
                            clear()
                            input("The drawer is empty \n [Enter] Go back")
                            clear()
                        else:
                            clear()
                            insert_item("key")
                            input("You open the drawer, inside of it is a key. \n [Enter] Go back")
                            clear()
                    case _:
                        clear()

                    
            case 0:
                clear()
                show_inventory()
                
            case _:
                clear()


def clear():

    print("\033[H\033[J", end="")


def combat(enemy):

    

    while player.hp > 0 and enemy.hp > 0:

        showCombatStatus(player, enemy)
        fightact = int(input("\n 1. Attack \n 2. Item \n 3. Run \n"))

        enemyhitrate = random.randint(0,10)
        playerhitrate = random.randint(0,10)

        match fightact:
            case 1:
                if playerhitrate > 3:
                    clear()
                    enemy.dmgTaken(player.atk)
                    showCombatStatus(player, enemy)
                    input(f"You dealt {player.atk} damage \n [Enter]")

                    if enemy.hp <= 0:
                        input("You won \n [Enter]")
                        clear()
                        result = "Win"
                        return result

                else:
                    clear()
                    showCombatStatus(player, enemy)
                    input("You missed \n [Enter]")
            case 2:

                if use_item() == potion1:
                    remove_item(potion1)
                    continue
                else:
                    continue
                    clear()
            case _: 
                clear()
                continue

        if enemyhitrate > enemy.hitrate:
            clear()
            player.dmgTaken(enemy.dmg)
            showCombatStatus(player, enemy)
            input(f"You recieved {enemy.dmg} damage \n [Enter]")

            if player.hp <= 0:
                input("You died \n [Enter]")
                clear()
                result = "Loss"
                return result
        else:
            clear()
            showCombatStatus(player, enemy)
            input(f"The {enemy.name} missed \n [Enter]")


def showCombatStatus(player, enemy):
    clear()
    print(f"Health = {player.hp}")
    print(f"{enemy.name} health = {enemy.hp}")
    

def forest():

    clear()

    while True:

        action = int(input("You find yourself in a forest. in front of you are three paths. \n 1. Path one \n 2. Path two \n 3. Path three \n 0. Inventory \n"))

        match action:
            case 1:
                #If the quest is done then it opens
                clear()
                input("Theres a large gate blocking the way, you're not cool enough to open it yet. \n [Enter] Go back")
                clear()
            case 2:
                clear()
                fight = int(input("Theres a pathway leading to a small town, a wolf is roaming around on it. \n 1. Press the wolf \n 2. Go back \n "))

                match fight:
                    case 1:
                            clear()

                            if  combat(wolf1) == "Win":
                                #Goto next area (town)
                                clear()
                            else:
                                forest()
                    case _: 
                        clear()
            case 3:
                clear()
                box = int(input("In front of you is a wooden chest. Open it? \n 1. Yes \n 2. No \n "))

                if box == 1:

                    if dagger in inventory.values():
                        clear()
                        input("The box is empty")
                        clear()
                        continue

                    
                    insert_item(dagger)
                    dagger.equip(player)
                    insert_item(potion1)
                    input("[Enter] Go back")
                    clear()
                else:
                    clear()
            case 0:
                clear()
                show_inventory()



clear()

tutorial()
forest()