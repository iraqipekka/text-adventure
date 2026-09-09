#Handle player input to trigger different events and tasks such as moving to different areas or interacting with items etc.
#Handle different scenes (ex. area, combat) and run different code depending on where the player is using functions.
#Be able to store items permanently in an inventory using lists or dictionaries.
#Be able to save and load game progress eventually using json.
#Add as you go.

import random

inventory = {1 : None , 2 : None, 3 : None, 4 : None, 5 : None}

def insert_item(item):

    for slot in inventory:    

        if inventory[slot] is None:
            inventory[slot] = item
            print(f"[Aquired] {item}")
            return

    print("Inventory is full")
    


def remove_item(item):

    for slot in inventory:

        if inventory[slot] == item:
            inventory[slot] = None
            print(f"[Dropped] {item}")
            return

    print("Nothing in inventory")
    

def tutorial():

    while True:

        action = int(input("You wake up in strange room, there is a door in front of you, to your left is a strange hallway. \n 1. Try the door \n 2. Turn left into the hallway \n"))


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

                drawer = int(input("You turn left into the hallway. In front of you is a drawer. \n 1. Open the drawer \n 2. Go back "))

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

                    case 2: 
                        clear()

def clear():

    print("\033[H\033[J", end="")

clear()
tutorial()