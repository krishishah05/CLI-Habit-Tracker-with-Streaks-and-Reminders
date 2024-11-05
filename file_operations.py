# file_operations.py
import json
import os

FILE_PATH = "habits.json"

def load_habits():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    return {}

def save_habits(habits):
    with open(FILE_PATH, "w") as file:
        json.dump(habits, file, indent=4)
