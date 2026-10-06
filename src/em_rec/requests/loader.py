import yaml
from pathlib import Path


def load_request_config(request_path: str) -> dict:
    src_path = Path(request_path)

    if not src_path.exists():
        raise FileNotFoundError(f"File not found or path doesnt exists: {src_path}")
    
    with src_path.open("r", encoding="utf8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError("Reuest data cant be parsed into dictionary")
    if "dataset" not in data:
        raise ValueError("Parameter 'dataset' not found in request dictionary")
    
    return data
    
