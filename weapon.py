class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power

weapon = Weapon('blicky',11)
print(weapon.name)
print(weapon.attack_power)