from config import ASSASSIN_HEALTH_MULT, ADVENTURER_ATTACK_MULT, CRAFTSMAN_ARMOR_MULT
from random import randint
from math import floor

from toad import Toad


class Assassin(Toad):
    """
    Класс жабы-ассасина.

    Дополнительные атрибуты:
    - health_mult (float): множитель здоровья.
    """
    def __init__(self):
        super().__init__()

    def modify_params(self):
        self.health *= ASSASSIN_HEALTH_MULT


class Adventurer(Toad):
    """
    Класс жабы-приключенца.

    Дополнительные атрибуты:
    - attack_mult (float): множитель атаки.
    """
    def __init__(self):

        super().__init__()

    def modify_params(self):
        """
        Изменяет параметры жабы-ассасина.
        """
        self.attack *= ADVENTURER_ATTACK_MULT


class Craftsman(Toad):
    """
    Класс жабы-ремесленника.

    Дополнительные атрибуты:
    - armor_mult (float): множитель брони.
    """
    def __init__(self):
        super().__init__()

    def modify_params(self):
        self.armor *= CRAFTSMAN_ARMOR_MULT


class Sniper(Toad):
    """
    Класс жабы-снайпера.

    Дополнительные атрибуты:
    - damage_range: верхний диапазон урона увеличен в х2 раза.
    """
    def __init__(self):
        super().__init__()

    def calculate_damage(self):
        return randint(floor(self.attack / 2), floor(self.attack * 2))

    def modify_params(self):
        pass


class Tank(Toad):
    """
    Класс жабы-танка.

    Дополнительные атрибуты:
    - armor_mult: минимальный диапазон брони увеличен с 0 до половины "надетой" брони.
    """
    def __init__(self):
        super().__init__()

    def calculate_armor(self):
        return randint(floor(self.armor / 2), floor(self.armor))

    def modify_params(self):
        pass
