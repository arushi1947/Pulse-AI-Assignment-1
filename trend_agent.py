import json
import os
from collections import Counter

DAILY_TOPIC_DIR = os.path.join("memory", "daily_topics")
OUTPUT_DIR = "output"


def save_daily_topics(date, canonical_topics):
    os.makedirs(DAILY_TOPIC_DIR, exist_ok=True)
    counts = Counter(canonical_topics)

    file_path = os.path.join(DAILY_TOPIC_DIR, f"{date}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(counts, f, indent=2)

from datetime import datetime, timedelta


def generate_trend_report(target_date):
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    end_date = datetime.strptime(target_date, "%Y-%m-%d")
    start_date = end_date - timedelta(days=29)

    date_list = [
        (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
        for i in range(30)
    ]

    all_topics = set()
    daily_data = {}

   
    for date in date_list:
        file_path = os.path.join(DAILY_TOPIC_DIR, f"{date}.json")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                daily_counts = json.load(f)
        else:
            daily_counts = {}

        daily_data[date] = daily_counts
        all_topics.update(daily_counts.keys())

    
    output_file = os.path.join(OUTPUT_DIR, f"trend_report_{target_date}.csv")

    with open(output_file, "w", encoding="utf-8") as f:
        header = ["Topic"] + date_list
        f.write(",".join(header) + "\n")

        for topic in sorted(all_topics):
            row = [topic]
            for date in date_list:
                row.append(str(daily_data[date].get(topic, 0)))
            f.write(",".join(row) + "\n")

    print(f"[OK] Trend report generated: {output_file}")


