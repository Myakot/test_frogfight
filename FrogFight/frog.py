from random import randint
from math import floor
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
        return randint(floor(self.attack / 2), floor(self.attack))

    def calculate_armor(self):
        return randint(0, floor(self.armor))
