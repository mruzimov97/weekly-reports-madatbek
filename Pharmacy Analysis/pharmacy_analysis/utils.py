import logging
import json

# Configure logging
def setup_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def save_json(data, path):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
