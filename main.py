from game import Game

def main():
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()

if __name__ == "__main__":
    main()
