import os
import yaml


#function to load the configurations
def load_config(config_path: str = None):
    if config_path is None:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = os.path.join(BASE_DIR, "config", "config.yaml")
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    with open(config_path, 'r')  as file:
        config =  yaml.safe_load(file)
        if config is None:
            raise ValueError(f"Config file {config_path} is empty or invalid")
        return config
