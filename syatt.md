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
        
    # ======= SEE added code in commands.py ======

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

