from pathlib import Path
from typing import Dict, Any
import json

class Settings:
    def __init__(self):
        self.config_path = Path('config/config.json')
        self.default_config = {
            'max_iterations': 1000,
            'gui_theme': 'light',
            'debug_mode': False
        }
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        if self.config_path.exists():
            with open(self.config_path) as f:
                return json.load(f)
        return self.default_config 