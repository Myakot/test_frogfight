from config import ASSASSIN_HEALTH_MULT, ADVENTURER_ATTACK_MULT, CRAFTSMAN_ARMOR_MULT
import random
import math

from frog import Frog


class Assassin(Frog):
    def __init__(self):
        super().__init__()

    def modify_params(self):
        self.health *= ASSASSIN_HEALTH_MULT


class Adventurer(Frog):
    def __init__(self):
        super().__init__()

    def modify_params(self):
        self.attack *= ADVENTURER_ATTACK_MULT


class Craftsman(Frog):
    def __init__(self):
        super().__init__()

    def modify_params(self):
        self.armor *= CRAFTSMAN_ARMOR_MULT


class Sniper(Frog):
    def __init__(self):
        super().__init__()

    def calculate_damage(self):
        return random.randint(math.floor(self.attack / 2), math.floor(self.attack * 2))

    def modify_params(self):
        pass


class Tank(Frog):
    def __init__(self):
        super().__init__()

    def calculate_armor(self):
        return random.randint(math.floor(self.armor / 2), self.armor)

    def modify_params(self):
        pass
