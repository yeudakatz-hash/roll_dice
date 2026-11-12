from menu import print_menu
from game_manager import *
from games_history import show_history_games
from show_statistics import show_statistics_games

def main():
    while True:

        choose = print_menu()

        if choose == "1":
            play()

        elif choose == "2":
            show_history_games()

        elif choose == "3":
           show_statistics_games()

        elif choose == "4":
            print("bye")
            break

        else:
            print("invalid choose!")
            continue

main()
