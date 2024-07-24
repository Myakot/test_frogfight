from config import ASSASSIN_HEALTH_MULT, ADVENTURER_ATTACK_MULT, CRAFTSMAN_ARMOR_MULT
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
