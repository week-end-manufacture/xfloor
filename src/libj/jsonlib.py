import os
import json

class JsonLib:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        self.data = self.load_json()

    def load_json(self):
        if not os.path.exists(self.json_file_path):
            raise FileNotFoundError(f"JSON file not found: {self.json_file_path}")
        
        with open(self.json_file_path, 'r') as file:
            return json.load(file)

    def save_json(self):
        with open(self.json_file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
        self.save_json()