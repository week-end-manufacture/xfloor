import json
from typing import Any

class JsonLib:
    def __init__(self, json_str: str = None):
        self.data = self.load_json(json_str) if json_str else {}

    def load_json(self, json_str: str) -> Any:
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON string: {e}")

    def to_json_str(self) -> str:
        return json.dumps(self.data, indent=4)

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def set(self, key: str, value: Any):
        self.data[key] = value