from Character import *
from Tile import *

# amuffin = Player("amuffin", 1, "you are mom", ["asdf", "asdf"])
# carl = Skeleton("carl", 1, "", [])

# amuffin.printcharsheet()

# carl.bonesattack(amuffin)

# amuffin.printcharsheet()

theMap = [["#", "#", "#"],
          ["#", ".", "#"],
          ["#", ".", "#"],
          ["#", "#", "#"]]

wall = Tile("#", "A wall.")
floor = Tile(".", "The floor.")

tilesDict = {
    "#": wall,
    ".": floor
}

print(tilesDict["#"].desc)
userInput = input('input: ')

