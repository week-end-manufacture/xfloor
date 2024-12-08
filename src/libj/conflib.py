import os
import json

class ConfLib:
    def __init__(self, prog_name):
        self.prog_name = prog_name
        self.json_file_path = self.set_json_file_path()
        self.config = self.load_json()

    def set_json_file_path(self):
        home_dir = os.path.expanduser("~")

        return os.path.join(home_dir, '.config', self.prog_name, 'config.json')

    def load_json(self):
        if not os.path.exists(self.json_file_path):
            raise FileNotFoundError(f"JSON file not found: {self.json_file_path}")
        
        with open(self.json_file_path, 'r') as file:
            return json.load(file)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set_env_variables(self):
        for key, value in self.config.items():
            os.environ[key] = str(value)

    def open_config(self):
        os.system(f"open {self.json_file_path}")