from jsn_file import load_games




def show_history_games():
    games = load_games()
    if not games:
        print("no game history")
        return

    for index, game in enumerate(games, start=1):
        name = game["player_name"]
        p_score = game["player_score"]
        c_score = game["computer_score"]
        winner = game["winner"]

        print(f"Game {index}: {name} ({p_score}) vs Computer ({c_score}) | Winner: {winner}")
