import random

equipment = []

greek_layout = [
    ["spartan camp", "spartan camp", "blank", "forest", "forest"],
    ["giant's path", "blank", "blank", "wolf pack", "ancient tomb"],
    ["bandit outpost", "giant's path", "blank", "blank", "forest"],
    ["mountain", "mountain", "blank", "athenian wall", "athenian wall"],
    ["labyrinth entrance", "giant's path", "athenian wall", "war supplies", "temple of athena"]
]

locations = ["minotaur", "chest", "snake"]
random.shuffle(locations)

labyrinth_layout = [
    ["empty", "empty", locations[1], "wall", "empty", "empty", "empty", "empty", "empty"],
    ["empty", "wall", "wall", "wall", "empty", "wall", "wall", "wall", "empty"],
    ["empty", "empty", "empty", "wall", "empty", "empty", "empty", "wall", locations[0]],
    ["empty", "wall", "empty", "wall", "empty", "wall", "empty", "wall", "wall"],
    ["empty", "wall", "empty", "empty", "empty", "wall", "empty", "empty", "empty"],
    ["empty", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "empty"],
    [locations[2], "wall", "empty", "empty", "empty", "empty", "empty", "wall", "empty"],
    ["wall", "wall", "empty", "wall", "wall", "wall", "empty", "wall", "empty"],
    ["enter", "empty", "empty", "wall", "snake", "empty", "empty", "empty", "empty"]
]

tiles = {
    "empty": {
        "description": "Nothing interesting seems to be around",
        "printable": "          ",
        "interacted": True
    },
    "blank": {
        "description": "Nothing interesting seems to be around",
        "printable": "    +     ",
        "interacted": True
    },
    "spartan camp": {
        "description": "A military outpost heavily fortified with the equipment to treat wounds and resupply",
        "printable": " Spartan  ",
        "interacted": True
    },
    "forest": {
        "description": "Below the towering trees, the dense foliage suffocates the floor. Visibility is incredibly low",
        "printable": "  Forest  ",
        "interacted": True
    },
    "giant's path": {
        "description": "A path travelled commonly by the giants. Be careful, you might run into one!",
        "printable": "  Giants  ",
        "interacted": True
    },
    "wolf pack": {
        "description": "A pack of wolves exploiting the low visibility in the forest",
        "printable": "  Forest  ",
        "interacted": True
    },
    "ancient tomb": {
        "description": "The entrance to an ancient tomb found deep in the jungle. Finding it is a miracle!",
        "printable": "   Tomb   ",
        "interacted": False
    },
    "bandit outpost": {
        "description": "A group of bandits that have been taking high value spartan captives",
        "printable": " Bandits  ",
        "interacted": False
    },
    "mountain": {
        "description": "Steep, treacherous, terrain that even the giant's struggle to traverse. Not fit for climbing",
        "printable": " \033[37mMountain\033[0m ",
        "interacted": True
    },
    "athenian wall": {
        "description": "A heavily fortified wall protecting the inner city of Athens",
        "printable": "   Wall   ",
        "interacted": True
    },
    "war supplies": {
        "description": "Military supplies meant for fighting sparta",
        "printable": " Supplies ",
        "interacted": False
    },
    "temple of athena": {
        "description": "People come from all around to give gifts to athena. Surprisingly little security",
        "printable": "  Athena  ",
        "interacted": True
    },
    "labyrinth entrance": {
        "description": "The floor collapsed to reveal a massive opening leading deep underground",
        "printable": "    ?     ",
        "interacted": True
    },
    "wall": {
        "description": "You shouldn't be on this tile!",
        "printable": "   \033[37mWall\033[0m   ",
        "interacted": True
    },
    "snake": {
        "description": "Snakes seem to have infested every deep ",
        "printable": "    ?     ",
        "interacted": True
    },
    "chest": {
        "description": "Contains a randomly generated weapon (name not attached to stats)",
        "printable": "    ?     ",
        "interacted": False
    },
    "minotaur": {
        "description": "A mythical creature that is half human, half bull. Appears to be angry...",
        "printable": "    ?     ",
        "interacted": True
    },
    "enter": {
        "description": "The entrance to the minotaur labyrinth",
        "printable": "  Enter   ",
        "interacted": True
    }
}

actions = """\033[37m-------------------------------------------
Actions:
    * (W)alk
    * (I)nteract
    * (M)ap
    * (E)quipment
    * (Q)uit
-------------------------------------------\033[0m"""
