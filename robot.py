from weapon import Weapon
class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('blicky',11)

    def attack(self, dinosaur):
        dino_health = dinosaur
        dino_health -= self.active_weapon
        
