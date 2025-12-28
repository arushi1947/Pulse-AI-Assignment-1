import json
import os

DATA_DIR = "data"

def load_daily_reviews(target_date):
    """
    Loads reviews for a given date (YYYY-MM-DD)
    """
    file_path = os.path.join(DATA_DIR, f"{target_date}.json")

    if not os.path.exists(file_path):
        print(f"[WARN] No data file for {target_date}")
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
