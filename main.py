# Kyle Eidsness
# RPG Class Assignment
# April 24, 2023

from classes import Map
import setup
import functions

greek = Map(1, 1, setup.greek_layout)
minotaur = Map(0, 8, setup.labyrinth_layout)
current_map = greek

print(setup.actions)
while True:
    userInput = input("Enter an action (or O for Options): ").lower()[:1]
    if userInput == "q":
        quit()
    elif userInput == "w":
        functions.loopMovement(current_map)
    elif userInput == "m":
        current_map.print_map()
    elif userInput == "e":
        print(f"\033[37m{functions.liToString(setup.equipment)}\033[0m")
    elif userInput == "i":
        functions.interact(current_map)
        if current_map.map[current_map.position[1]][current_map.position[0]] == "labyrinth entrance" and "labyrinth map" in setup.equipment:
            current_map = minotaur
    elif userInput == "o":
        print(setup.actions)
    elif userInput == "l":
        current_map.print_description()
    else:
        print(f"\033[91m'{userInput}' is not a valid action\033[0m")
