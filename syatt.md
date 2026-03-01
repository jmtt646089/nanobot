# Run it on Hugging Face Space
## 1. fork

## 2. remove README.md

## 3. remove case/*.png

## 4. use python to read HF Secrets config for AI Provider and Channel
```python
import os
import json

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
    
    
    # Path.home() / ".nanobot" /"config.json" also ok
    jm_config_file = Path("~/.nanobot/config.json")

    # 1. Ensure the parent directory exists
    jm_config_file.parent.mkdir(parents=True, exist_ok=True)
    
    # 2. Write the JSON object to the file
    # Using the 'with open' context manager for robust file handling
    try:
        with open(jm_config_file, 'w', encoding='utf-8') as jm_f:
            json.dump(jm_data, jm_f, ensure_ascii=False, indent=4)
        print(f"Successfully wrote data to {jm_config_file}")
    except IOError as e:
        print(f"Error writing to file: {e}")

    jm_workspace = Path.home() / ".nanobot" /"workspace" 
    # or Path("/root/.nanobot/workspace")
    jm_workspace.mkdir(parents=True, exist_ok=True)

    # SYATT --- for running on Hugging Face Space --- end ---

```

## 5. edit Dockerfile
```Dockerfile
ENTRYPOINT ["nanobot"]
CMD ["gateway"]
```

## 6. HF Space Create and change its README.md
add app_port: 18790  

```YAML
title: Agent
emoji: 📈
colorFrom: pink
colorTo: indigo
sdk: docker
app_port: 18790
pinned: false
license: mit
```

## 7. download gh repo and upload to HF Space via Web UI

## 8. or push repo from GH to HF with GH action

