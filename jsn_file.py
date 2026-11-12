import json

path = "jsn_file.json"

def dump_new_game(new_game):
    try:
        with open(path, "r", encoding="utf-8") as file:
            arr = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        arr = []

    arr.append(new_game)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(arr, file, indent=2, ensure_ascii=False)



def load_games():
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

