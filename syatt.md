# Run it on Hugging Face Space
## 1. fork

## 2. remove README.md

## 3. remove case/*.png

## 4. use python to read HF Secrets config for AI Provider and Channel
```python
import os
import json

or_key = os.environ.get("OR_KEY", "sk-or-v1-...for-example")
tg_token = os.environ.get("TG_TOKEN", "for-example")

if or_key is not None:
    print(f"OR_KEY IS CONFIGURED:{or_key}")
else:
    print("PLEASE SET OR_KEY .")
    
    
if tg_token is not None:
    print(f"TG_TOKEN IS CONFIGURED:{tg_token}")
else:
    print("PLEASE SET TG_TOKEN .")

data = {

  "providers": {
    "openrouter": {
      "apiKey": "{or_key}"
    }
  }


  "agents": {
    "defaults": {
      "model": "upstage/solar-pro-3:free",
      "provider": "openrouter"
    }
  }


  "channels": {
    "telegram": {
      "enabled": true,
      "token": "{tg_token}",
      "allowFrom": ["jmnanobot"]
    }
  }
  
}


config_path = "/root/.nanobot"
config_file_name = "config.json"
config_file = os.path.join(config_path, config_file_name) 

os.makedirs(config_path, exist_ok=True)

if not os.path.exists(config_file):
    with open(config_file, "w") as json_file:
        #file.write("Hello, World from os module!")
        json.dump(data, json_file, indent=4)
else:
    print(f"File '{config_file}' already exists. Not overwriting.")


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

