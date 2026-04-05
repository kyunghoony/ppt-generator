import os
import yaml
from typing import Dict, Any

def load_preset(preset_name: str = "default") -> Dict[str, Any]:
    """Loads the preset configuration, merging with default if necessary."""
    base_dir = os.path.dirname(os.path.dirname(__file__))
    default_path = os.path.join(base_dir, "presets", "default", "config.yaml")
    
    config = {}
    if os.path.exists(default_path):
        with open(default_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f) or {}
            
    if preset_name != "default":
        preset_path = os.path.join(base_dir, "presets", preset_name, "config.yaml")
        if os.path.exists(preset_path):
            with open(preset_path, "r", encoding="utf-8") as f:
                preset_config = yaml.safe_load(f) or {}
                # Simple merge
                for k, v in preset_config.items():
                    if isinstance(v, dict) and isinstance(config.get(k), dict):
                        config[k].update(v)
                    else:
                        config[k] = v
                
    return config

def load_template(preset_name: str, template_name: str) -> Dict[str, Any]:
    """Loads a specific deck template from a preset."""
    base_dir = os.path.dirname(os.path.dirname(__file__))
    template_path = os.path.join(base_dir, "presets", preset_name, f"{template_name}.yaml")
    
    if os.path.exists(template_path):
        with open(template_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    return {}
