import json
import os


class FileHandler:

    def __init__(self):
        self.base_path = "app/database/"

    def read_file(self, filename):
        path = os.path.join(self.base_path, filename)

        if not os.path.exists(path):
            return []

        try:
            with open(path, "r") as f:
                return json.load(f)
        except:
            return []

    def write_file(self, filename, data):
        path = os.path.join(self.base_path, filename)

        with open(path, "w") as f:
            json.dump(data, f, indent=4)