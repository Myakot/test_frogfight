from random import randint
from math import floor
from abc import ABC, abstractmethod

from config import ATTACK, HEALTH, ARMOR


class Toad(ABC):
    """
    Абстрактный класс для ЖАБ.

    Attributes:
        attack (int): атака жабы.
        health (int): здоровье жабы.
        armor (int): броня жабы.
    """
    def __init__(self):
        """
        Инициализация жабы с заданными параметрами.
        """
        self.attack = ATTACK
        self.health = HEALTH
        self.armor = ARMOR

    @abstractmethod
    def modify_params(self):
        """
        Абстрактный метод для изменения параметров жабы.
        """
        pass

    def calculate_damage(self):
        """
        Вычисляет урон, наносимый лягушкой.

        return:
            int: урон, наносимый лягушкой.
        """
        return randint(floor(self.attack / 2), floor(self.attack))

    def calculate_armor(self):
        """
        Вычисляет броню жабы.

        return:
            int: броня жабы.
        """
        return randint(0, floor(self.armor))
