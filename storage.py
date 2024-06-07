import json

def save_duko(duko):
    with open("duko.json", "w") as f:
        json.dump(duko.__dict__, f)

def load_duko():
    with open("duko.json", "r") as f:
        return DUKO(**json.load(f))
