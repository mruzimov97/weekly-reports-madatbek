import json
import pandas as pd
import glob
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)

def load_csv_files(directory: Path) -> pd.DataFrame:
    files = glob.glob(str(directory / "*.csv"))
    if not files:
        logging.warning(f"No CSV files found in {directory}. Returning empty DataFrame.")
        return pd.DataFrame()
    return pd.concat([pd.read_csv(f) for f in files])

def load_json_files(directory: Path) -> pd.DataFrame:
    try:
        files = glob.glob(str(directory / "*.json"))
        if not files:
            logging.warning(f"No JSON files found in {directory}. Returning empty DataFrame.")
            return pd.DataFrame()

        data = []
        for f in files:
            try:
                with open(f, "r") as file:
                    data.append(json.load(file))
            except json.JSONDecodeError as e:
                logging.error(f"Skipping invalid JSON file {f}: {e}")

        valid_data = [pd.DataFrame(d) for d in data if d]
        return pd.concat(valid_data) if valid_data else pd.DataFrame()

    except FileNotFoundError as e:
        logging.error(f"Error loading JSON files from {directory}: {e}")
        return pd.DataFrame()
