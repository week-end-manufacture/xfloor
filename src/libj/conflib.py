import os
import json
import shutil

class ConfLib:
    def __init__(self, prog_name):
        self.prog_name = prog_name
        self.home_dir = os.path.expanduser("~")
        self.config_dir = os.path.join(self.home_dir, f'.{self.prog_name}')
        self.config_file = os.path.join(self.config_dir, 'config.json')
        self.config = self.load_json()

    def set_json_file_path(self):
        home_dir = os.path.expanduser("~")

        return os.path.join(home_dir, '.config', self.prog_name, 'config.json')
    
    def ensure_config_file(self):
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir)
        
        if not os.path.exists(self.config_file):
            shutil.copy(self.default_config_file, self.config_file)
            print(f"Copied default config to {self.config_file}")

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