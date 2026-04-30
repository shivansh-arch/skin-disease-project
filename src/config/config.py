import yaml
import os

class Config:
    def __init__(self, config_path="configs/config.yaml"):
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found at {config_path}")
        
        with open(config_path, "r", encoding="utf-8") as file:
            self.config = yaml.safe_load(file)

    def get(self, *keys):
        """
        Access nested config values
        Example: config.get("training", "batch_size")
        """
        value = self.config
        for key in keys:
            value = value[key]
        return value