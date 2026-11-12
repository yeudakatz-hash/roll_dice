from jsn_file import load_games




def show_statistics_games():
    games = load_games()
    if not games:
        print("no game history")
        return

    count_games = 0
    player_win = 0
    comp_win = 0
    tie = 0

    for game in games:
        count_games += 1
        if game["winner"] == "computer":
            comp_win += 1
        elif game["winner"] == "tie":
            tie += 1
        else:
            player_win += 1

    print(f"games: {count_games} \n player_wins: {player_win}\ncomputer wins: {comp_win}\ntie_wins: {tie}")
    return