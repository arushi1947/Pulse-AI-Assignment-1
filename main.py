print("MAIN.PY STARTED")


from agents.ingestion_agent import load_daily_reviews
from agents.topic_extraction_agent import extract_topics
from agents.deduplication_agent import deduplicate_topics
from agents.trend_agent import save_daily_topics, generate_trend_report

def run_pipeline(target_date):
    reviews = load_daily_reviews(target_date)
    raw_topics = extract_topics(reviews)
    canonical_topics = deduplicate_topics(raw_topics)

    save_daily_topics(target_date, canonical_topics)
    generate_trend_report(target_date)

if __name__ == "__main__":
    run_pipeline("2024-06-02")
