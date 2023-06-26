import setup


class Map:
    def __init__(self, startX, startY, map):
        self.position = [startX, startY]
        self.map = map
        self.available = [True, True, True, True]
        self.get_available()

        self.row_break = ""
        for x in self.map[0]:
            self.row_break += "+----------"
        self.row_break += "+"

    def get_available(self):
        for x in range(0, 4):
            self.available[x] = False
        if self.position[1] > 0:
            self.available[0] = True
        if self.position[0] > 0:
            self.available[3] = True
        if self.position[1] < len(self.map) - 1:
            self.available[2] = True
        if self.position[0] < len(self.map[0]) - 1:
            self.available[1] = True

    def print_directions(self):
        print("\033[37m-------------------------------------------")
        print("Directions: ")
        if self.available[0]:
            print("    *(N)orth")
        if self.available[1]:
            print("    *(E)ast")
        if self.available[2]:
            print("    *(S)outh")
        if self.available[3]:
            print("    *(W)est")
        print("-------------------------------------------\033[0m")

    def move(self, direction):
        if direction == "n" and self.available[0]:
            self.position[1] -= 1
        elif direction == "e" and self.available[1]:
            self.position[0] += 1
        elif direction == "s" and self.available[2]:
            self.position[1] += 1
        elif direction == "w" and self.available[3]:
            self.position[0] -= 1
        else:
            print("\033[91mYou cannot move in that direction\033[0m")
        self.get_available()

    def print_map(self):
        tile_position = [0, 0]
        for row in self.map:
            print(self.row_break)
            for column in row:
                if tile_position[0] == self.position[0] and tile_position[1] == self.position[1]:
                    print(f"|\033[32m{setup.tiles[column]['printable']}\033[0m", end="")
                else:
                    print(f"|{setup.tiles[column]['printable']}", end="")
                tile_position[0] += 1
            print("|")
            tile_position[1] += 1
            tile_position[0] = 0
        print(self.row_break)

    def print_description(self):
        print(f"\033[37m{self.map[self.position[1]][self.position[0]].upper()}:")
        print(f"{setup.tiles[self.map[self.position[1]][self.position[0]]]['description']}\033[0m")
