from hero import Hero
import random

class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютерный Герой")

    def start(self):
        print("Начинаем игру 'Битва героев'!")
        while self.player.is_alive() and self.computer.is_alive():
            self.turn()

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

    def turn(self):
        if random.choice([True, False]):
            self.player.attack(self.computer)
        else:
            self.computer.attack(self.player)

        print(f"{self.player.name} здоровье: {self.player.health}")
        print(f"{self.computer.name} здоровье: {self.computer.health}")
        print()
