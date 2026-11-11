import json
import os

FILE_NAME = "donations.json"


def load_data():
    if not os.path.exists(FILE_NAME):
        return {"donations": [], "users": []}

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            return {"donations": [], "users": []}

        data.setdefault("donations", [])
        data.setdefault("users", [])

        return data

    except (json.JSONDecodeError, OSError):
        print("Unable to read data file. Starting with empty records.")
        return {"donations": [], "users": []}


def save_data(data):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

        print("Data saved successfully!")

    except OSError:
        print("Error: Unable to save data.")