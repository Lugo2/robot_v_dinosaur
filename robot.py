from weapon import Weapon
from dinosaur import Dinosaur
class Robot:
    def __init__(self, name):
        self.robo_name = name
        self.robo_health = 100
        self.active_weapon = Weapon()

    def robo_attack(self, dinasaur):
        pass