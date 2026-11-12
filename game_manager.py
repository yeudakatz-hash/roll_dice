import random
from print_game import *
from validation import *
from structure import *
from jsn_file import dump_new_game


def play():

    num , name = details()
    print_start(name, num)
    comp_points = 0
    player_points = 0
    counter = 0
    for i in range(num):
        counter += 1
        player_score, computer_score = play_round()
        winner = calculate_winner(player_score, computer_score)
        if winner == "player":
            text = f"{name} wins this round!"
            player_points += 1
        if winner == "computer":
            text = "Computer wins this round!"
            comp_points += 1
        else:
            text = "It's a tie"
        print_round(counter, player_score, computer_score, text, name)
        build_round(counter, player_score, computer_score, winner)
    win_game = calculate_winner(player_points, comp_points)
    if win_game == "player":
        text = f"WINNER: {name}!"
    if win_game == "computer":
        text = "WINNER: Computer!"
    else:
        text = "It's a tie"
    print_end(name, comp_points, player_points, text)
    struc = build_main(name, num, player_points, comp_points, win_game)
    dump_new_game(struc)












def play_round():
    return roll_dice(), roll_dice()


def roll_dice():
    return random.randint(1,6)


def calculate_winner(player_score, computer_score):
    if player_score > computer_score:
        return "player"
    elif computer_score > player_score:
        return "computer"
    else:
        return "tie"