"""Configuration loading utilities."""

import json
from pathlib import Path
import os # SYATT --- for running on Hugging Face Space --- for use of HF Secrets

from nanobot.config.schema import Config


def get_config_path() -> Path:
    """Get the default configuration file path."""
    return Path.home() / ".nanobot" / "config.json"

    


def get_data_dir() -> Path:
    """Get the nanobot data directory."""
    from nanobot.utils.helpers import get_data_path
    return get_data_path()


def load_config(config_path: Path | None = None) -> Config:
    """
    Load configuration from file or create default.

    Args:
        config_path: Optional path to config file. Uses default if not provided.

    Returns:
        Loaded configuration object.
    """


    # SYATT --- for running on Hugging Face Space --- Begin --- var starting with jm_ to avoid conflicts with original code
    jm_or_key = os.environ.get("OR_KEY", "sk-or-v1-...for-example")
    jm_tg_token = os.environ.get("TG_TOKEN", "for-example")
    
    if jm_or_key is not None:
        #print(f"OR_KEY IS CONFIGURED:{jm_or_key}")
        print(f"OR_KEY IS CONFIGURED.")
    else:
        print("PLEASE SET OR_KEY .")
        
        
    if jm_tg_token is not None:
        print(f"TG_TOKEN IS CONFIGURED.")
    else:
        print("PLEASE SET TG_TOKEN .")
    
    jm_data = {
    
      "providers": {
        "openrouter": {
          "apiKey": "{jm_or_key}"
        }
      },
    
    
      "agents": {
        "defaults": {
          "model": "upstage/solar-pro-3:free",
          "provider": "openrouter"
        }
      },
    
    
      "channels": {
        "telegram": {
          "enabled": True,
          "token": "{jm_tg_token}",
          "allowFrom": ["jmnanobot"]
        }
      },
      
    }
    
    # also can use this path Path.home() / ".nanobot" /"config.json" this is an object, not a string, need use pathlib
    jm_config_path = "/root/.nanobot" 
    jm_config_file_name = "config.json"
    jm_config_file = os.path.join(jm_config_path, jm_config_file_name) 
    
    os.makedirs(jm_config_path, exist_ok=True)
    
    if not os.path.exists(jm_config_file):
        with open(jm_config_file, "w") as jm_json_file:
            #file.write("Hello, World from os module!")
            json.dump(jm_data, jm_json_file, indent=4)
    else:
        print(f"File '{jm_config_file}' already exists. Not overwriting.")

    jm_workspace = Path.home() / ".nanobot" /"workspace" # or Path("/root/.nanobot/workspace")
    jm_workspace.mkdir(parents=True, exist_ok=True)


    # SYATT --- for running on Hugging Face Space --- end ---
    

    
    
    path = config_path or get_config_path()

    if path.exists():
        try:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
            data = _migrate_config(data)
            return Config.model_validate(data)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Warning: Failed to load config from {path}: {e}")
            print("Using default configuration.")

    return Config()


def save_config(config: Config, config_path: Path | None = None) -> None:
    """
    Save configuration to file.

    Args:
        config: Configuration to save.
        config_path: Optional path to save to. Uses default if not provided.
    """
    path = config_path or get_config_path()
    path.parent.mkdir(parents=True, exist_ok=True)

    data = config.model_dump(by_alias=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def _migrate_config(data: dict) -> dict:
    """Migrate old config formats to current."""
    # Move tools.exec.restrictToWorkspace → tools.restrictToWorkspace
    tools = data.get("tools", {})
    exec_cfg = tools.get("exec", {})
    if "restrictToWorkspace" in exec_cfg and "restrictToWorkspace" not in tools:
        tools["restrictToWorkspace"] = exec_cfg.pop("restrictToWorkspace")
    return data
