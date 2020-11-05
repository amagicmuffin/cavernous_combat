class Character:
    def __init__(self, name, health, inventory, skills):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.skills = skills
        # TODO: add a "possibleskills" attribute?
        # TODO: status effects

    def takedamage(self, damage):
        self.health -= damage

    def printcharsheet(self):  # TODO: used for debugging, make prettier later
        print(vars(self))


class Player(Character):
    pass


class Enemy(Character):
    pass


class Skeleton(Enemy):
    def bonesattack(self, target):
        target.health -= 2


# debug code down here
amuffin = Player("amuffin", 1, "you are mom", ["asdf", "asdf"])
carl = Skeleton("carl", 1, "", [])

amuffin.printcharsheet()

carl.bones(amuffin)

amuffin.printcharsheet()
