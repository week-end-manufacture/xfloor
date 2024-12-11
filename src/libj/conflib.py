import os
import json
import shutil

class ConfLib:
    def __init__(self, app_name):
        self.app_name = app_name
        self.home_dir = os.path.expanduser("~")
        self.config_dir = os.path.join(self.home_dir, '.config', f'{self.app_name}')
        self.config_file = os.path.join(self.config_dir, 'config.json')
        self.default_config_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),'config',  'config.json')

        self.ensure_config_file()

    def ensure_config_file(self):
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir)
        
        if not os.path.exists(self.config_file):
            shutil.copy(self.default_config_file, self.config_file)
            print(f"Copied default config to {self.config_file}")

    def load_json(self):
        with open(self.config_file, 'r') as file:
            return json.load(file)

    def get(self, key, default=None):
        config = self.load_json()
        return config.get(key, default)

    def set_env_variables(self):
        config = self.load_json()
        for key, value in config.items():
            os.environ[key] = str(value)

    def open_config(self):
        os.system(f'open {self.config_dir}')