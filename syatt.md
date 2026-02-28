# Run it on Hugging Face Space
## 1. fork

## 2. remove README.md

## 3. remove case/*.png

## 4. use python to read HF Secrets config for AI Provider and Channel
```python
import os

ai_provider_api_key = os.environ.get("AI_PROVIDER_API_KEY", "PLEASE SET AI PROVIDER API KEY")

if ai_provider_api_key is not None:
    print(f"AI_PROVIDER_API_KEY IS CONFIGURED.}")
else:
    print("PLEASE SET AI_PROVIDER_API_KEY.")

hf_token = os.environ.get("HF_TOKEN")
if hf_token:
    from huggingface_hub import HfApi
    hf_api = HfApi(token=hf_token)

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

