
results = []


def build_main(name, num, player_score, computer_score, winner):
    global results
    struc = {
        "player_name": name,
        "rounds": num,
        "player_score": player_score,
        "computer_score": computer_score,
        "winner": winner,
        "results": list(results)
    }
    results = []
    return struc




def build_round(counter, player_dice, computer_dice, winner):
    round_dict = {
        "round": counter,
        "player_dice": player_dice,
        "computer_dice": computer_dice,
        "winner": winner
    }
    results.append(round_dict)
