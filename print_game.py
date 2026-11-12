

def print_start(name, num):
    print(f"""
================================
          NEW GAME
================================

Player name: {name}
Number of rounds: {num}

""")



def print_round(counter, player_score, computer_score, text, name):
    print(f"""
---------- ROUND {counter} ----------

{name}:    🎲 {player_score}
Computer: 🎲 {computer_score}

{text}

""")




def print_end(name, comp_points, player_points, text):
    print(f"""
================================
          GAME OVER
================================

{name}:    {player_points} points
Computer: {comp_points} points

{text}

Game saved successfully!

    """)