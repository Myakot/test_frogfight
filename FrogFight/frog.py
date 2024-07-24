import random
import math
from abc import ABC, abstractmethod

from config import ATTACK, HEALTH, ARMOR


class Frog(ABC):
    def __init__(self):
        self.attack = ATTACK
        self.health = HEALTH
        self.armor = ARMOR

    @abstractmethod
    def modify_params(self):
        pass

    def calculate_damage(self):
        return random.randint(math.floor(self.attack / 2), math.floor(self.attack))

    def calculate_armor(self):
        return random.randint(0, self.armor)
