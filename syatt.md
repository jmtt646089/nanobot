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

