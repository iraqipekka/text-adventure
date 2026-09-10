import random

class Player:

    def __init__(self, hp = 10, atk = 3, gold = 0):
        self.hp = hp
        self.atk = atk
        self.gold = gold

    def dmgTaken(self, dmg):
        self.hp -= dmg


class Wolf:

    def __init__(self, hp = 12, dmg = 3, hitrate = 5, name = "Wolf"):
        self.hp = hp
        self.dmg = dmg
        self.name = name
        self.hitrate = hitrate

    def dmgTaken(self, atk):
        self.hp -= atk

class Bear:

    def __init__(self, hp = 25, dmg = 4, hitrate = 6, name = "Bear"):
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

    

class Sword:

    def __init__(self, dmg = 10, name = "Sword"):
        self.dmg = dmg
        self.name = name

    def equip(self, player):
        player.atk += self.dmg

    def __str__(self):
        return self.name

class Drip:

    def __init__(self, defense = 40, name = "Drip"):
        self.defense = defense
        self.name = name

    def equip(self, player):
        player.hp += self.defense

    def __str__(self):
        return self.name

class bigPotion:

    def __init__(self, heal = 50, name = "Big Potion"):
        self.heal = heal
        self.name = name

    def healing(self, player):
            player.hp += self.heal
            input(f"Used {self.name}. You healed for {self.heal} health \n [Enter]")
    
    def __str__(self):
        return self.name

class Dragon:

    def __init__(self, hp = 100, dmg = 12, hitrate = 5, name = "The Dragon"):
        self.hp = hp
        self.dmg = dmg
        self.hitrate = hitrate
        self.name = name

    def dmgTaken(self, atk):
        self.hp -= atk 
    
        



player = Player()
dagger = Dagger()
potion1 = Potion()
wolf1 = Wolf()
bear1 = Bear()
sword = Sword()
drip = Drip()
bigpotion = bigPotion()



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
        remove_item(item)
        return 
    elif item == bigpotion:
        item.healing(player)
        remove_item(item)
    else:
        input("Nothing usable in slot \n [Enter]")
        clear()
    

def show_inventory():

    print("{", end="")

    for slot, item in inventory.items():
        print(f"{slot}: {item}", end=" ")


    print("}")

    print(f"Gold = {player.gold}")

def get_choice(phrase):

    action = input(phrase)

    if action == "":
        clear()
        return

    action = int(action)
    return action

def tutorial():

    while True:

        action = get_choice("You wake up in strange room, there is a door in front of you, to your left is a strange hallway. \n 1. Try the door \n 2. Turn left into the hallway \n 0. Inventory \n")

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

                action = get_choice("You turn left into the hallway. In front of you is a drawer. \n 1. Open the drawer \n 2. Go back \n ")

                match action:
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

    if player.hp <= 50 and drip in inventory.values():
        player.hp = 50
    elif player.hp <= 10 and drip not in inventory.values():
        player.hp = 10
        

    while player.hp > 0 and enemy.hp > 0:

        showCombatStatus(player, enemy)
        action = get_choice("\n 1. Attack \n 2. Item \n 3. Run \n")

        enemyhitrate = random.randint(0,10)
        playerhitrate = random.randint(0,10)

        match action:
            case 1:
                if playerhitrate > 2:
                    clear()
                    enemy.dmgTaken(player.atk)
                    showCombatStatus(player, enemy)
                    input(f"You dealt {player.atk} damage \n [Enter]")

                    if enemy.hp <= 0:
                        input("You won \n [Enter]")
                        input("Recieved 20 gold \n [Enter]")
                        player.gold += 20
                        clear()
                        result = "Win"
                        return result

                else:
                    clear()
                    showCombatStatus(player, enemy)
                    input("You missed \n [Enter]")
            case 2:

                if use_item() == potion1:
                    continue
                else:
                    continue
                    clear()

            case 3:
                input("You can't run lmao \n [Enter]")
                continue
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
                input("You lost 5 gold")
                player.gold -= 5
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
    

def forest(wolfDead = False):

    clear()


    while True:

        action = get_choice("You find yourself in a forest. in front of you are three paths. \n 1. Path one \n 2. Path two \n 3. Path three \n 0. Inventory \n")

        match action:
            case 1:
                if drip in inventory.values():
                    clear()
                    action = get_choice("The gates open for you. A big dragon jumps at you. \n [Enter]")
                    clear()
                    if combat(Dragon()) == "Win":
                        clear()
                        print("Congratulations! You won the game. \n [SYSTEM] closing...")
                        exit()
                else:
                        
                    clear()
                    input("Theres a large gate blocking the way, you're not cool enough to open it yet. \n [Enter] Go back")
                    clear()
            case 2:
                clear()

                if wolfDead == False:
                    action = get_choice("Theres a pathway leading to a small town, a wolf is roaming around on it. \n 1. Press the wolf \n 2. Go back \n ")

                    match action:
                        case 1:
                                clear()

                                if  combat(wolf1) == "Win":
                                    town()
                                    
                                else:
                                    forest()
                        case 0: 
                            clear()
                            show_inventory()
                        case _:
                            clear()

                else: 
                    action = get_choice("Go to town? \n 1. Yes \n 2. Go back \n")

                    match action:
                        case 1:
                            clear()
                            town()
                        case 2: 
                            clear()
                        case _:
                            clear()

            case 3:
                clear()
                action = get_choice("In front of you is a wooden chest. Open it? \n 1. Yes \n 2. No \n ")

                if action == 1:

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

def town():

  

    while True:

        

        action = get_choice("You enter the town. There's a guy staring at you. Where do you want to go? \n 1. Talk to the guy \n 2. Forest \n 3. Shop \n 4. Bear farm \n 0. Inventory \n")

        match action:
            case 1:
                if sword in inventory.values():
                    clear()
                    input("[The guy] I have other matters to attend to. Go away. \n [Enter] Go back")
                    clear()
                else:

                    clear()
                    input("[The guy] I'm addicted to blacksmithing and I need a weapon. Please bring me a weapon. \n [Enter] Hand him the dagger")

                    remove_item(dagger)

                    input("[The guy] Ah. Thanks. Now I can finally quench the addiction. I'll upgrade it for you. [Enter] Recieve new weapon")

                    insert_item(sword)
                    dagger.unequip(player)
                    sword.equip(player)

                    input("[The guy] Heres some armor as well cause you lack drip \n [Enter] Recieve drip")

                    insert_item(drip)
                    drip.equip(player)

                    input("You feel cooler. \n [Enter]")
                    clear()
            case 2:
                forest(True)
            case 3:
                clear()
                shop()
            case 4:
                clear()
                combat(Bear())
            case 0:
                clear()
                show_inventory()
            case _:
                clear()


def shop():

    

    while True:


        action = get_choice("[Plug] dO yOU wAnT tO bUY pOtIoN?? \n 1. Yes \n 2. No \n")

        match action:
            case 1:
                if player.gold < 100:
                    input("[Plug] gET oUt mY sHop bRoke bOi \n [Enter] Okay")
                    clear()
                    town()
                else:
                    insert_item(bigpotion)
                    show_inventory()
                    input("[Enter] Back")
                    clear()
            case 2:
                clear()
                town()








clear()

tutorial()
forest()