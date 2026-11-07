import json
import os
from Student import Student


class FileManager:
    def __init__(self, filename="students.json"):
        self.filename = filename

    def save_data(self, students):
        try:
            data = [student.to_dict() for student in students]

            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4)

            print("Records saved successfully!")

        except (OSError, TypeError) as error:
            print("Error saving records:", error)

    def load_data(self):
        if not os.path.exists(self.filename):
            return []

        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("Invalid data format.")

            return [Student.from_dict(item) for item in data]

        except (OSError, json.JSONDecodeError, ValueError, KeyError, TypeError) as error:
            print("Error loading records:", error)
            return []