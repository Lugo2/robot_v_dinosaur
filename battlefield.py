from robot import Robot
from dinosaur import Dinosaur
class Battleflield:
    def run_game(self):
        def __init__(self):
            self.robot = Robot('Mini Boy')
            self.dinosaur = Dinosaur('Jenkins', 11)

        def display_welcome(self):
            self.print('Tonight! We are proud to host a marvel of a battle between: The Legendery Jenkins and The BIG,but not so big, Mini Boy!')
            self.print('Who shall win? Wariors ready? GO!')

            def battle_phase(self):
                both_alive = True
                while both_alive == True:
                    self.robot = Robot('Mini Boy')
                    self.dinosaur = Dinosaur('Jenkins', 11)
                    if self.dinosaur.health >= 0:
                        self.robot.attack(self.dinosaur.health)
                    elif self.robot.health >= 0:
                        self.dinosaur.attack(self.robot.health)
                    elif self.robot.health == 0:
                        winner = self.robot.name
                    elif self.dinosaur.health == 0:
                        winner = self.dinosaur.name
                def display_winner(self):
                    self.print(f'Well, that concludes it folks. Tonights winner is: {winner}')


        