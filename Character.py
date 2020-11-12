class Character:
    def __init__(
        self,
        name,
        health,
        is_stunned=False,
        is_burning=False,
        is_poisoned=False,
        is_withered=False,
    ):
        self.name = name
        self.health = health
        self.is_stunned = is_stunned
        self.is_burning = is_burning
        self.is_poisoned = is_poisoned
        self.is_withered = is_withered
        # TODO: more status effects later maybe (add buffs lol)

    def takedamage(self, damage):
        self.health -= damage

    def printcharsheet(self):  # TODO: used for debugging, make prettier later
        print(vars(self))


class Player(Character):
    def __init__(
        self,
        name,
        health,
        inventory,
        is_stunned=False,
        is_burning=False,
        is_poisoned=False,
        is_withered=False,
    ):
        super().__init__(name, health, is_stunned, is_burning, is_poisoned, is_withered)
        self.inventory = inventory


class Enemy(Character):
    pass
    # TODO: add favorite attack attirbute? add attack order attribute?
    #  or should those be handled within the individual enemy classes?
    #  example: Skeleton attacks with x, then y, then z, but will do f, then z if player below 30%.
    #  will also do heal if an ally is below 10%


class Skeleton(Enemy):
    def bonesattack(self, target):
        target.health -= 2
