import random
import setup


def generateWeapon():
    names = ["Great Sword", "Sword of Apostate", "Dire Flail", "Scimitar", "Morningstar", "War Hammer"]
    dice_options = [4, 6, 8, 10, 24]
    dice = dice_options[random.randint(0, 4)]
    num_dice = random.randint(4, 23) // dice
    if num_dice == 0:
        num_dice = 1
    bonus = random.randint(2, 5)
    return f"{names[random.randint(0, 5)]} ({num_dice}d{dice} + {bonus})"


def loopMovement(current_map):
    while True:
        current_map.print_directions()
        userInput = input("Enter a direction: ").lower()[:1]
        if userInput == "q":
            quit()
        elif userInput == "b":
            break
        elif userInput == "m":
            if current_map != "minotaur" or "labyrinth map" in setup.equipment:
                current_map.print_map()
        else:
            current_map.move(userInput)
        if userInput in ["n", "e", "s", "w"]:
            print(f"Position: \033[32m{current_map.map[current_map.position[1]][current_map.position[0]]}\033[0m")


def liToString(li):
    result = ""
    for item in li:
        result += f"{item}, "
    return result[0: len(result) - 2]


def interact(current_map):
    current_tile = current_map.map[current_map.position[1]][current_map.position[0]]
    if not setup.tiles[current_tile]["interacted"]:
        setup.equipment.append(generateWeapon())
        if current_tile == "ancient tomb":
            setup.equipment.append("labyrinth map")
        print(f"\033[37m{liToString(setup.equipment)}\033[0m")
        setup.tiles[current_tile]["interacted"] = True
