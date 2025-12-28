import re

# Common stopwords to ignore
STOPWORDS = {
    "the", "is", "was", "and", "a", "an", "to", "of", "for",
    "in", "on", "with", "it", "this", "that", "very"
}

# Simple keyword buckets (can be expanded later)
ISSUE_KEYWORDS = {
    "delivery": ["delivery", "delivered", "late"],
    "food": ["food", "meal", "dish", "stale", "cold", "bad"],
    "app": ["app", "map", "gps", "crash", "bug", "slow"],
    "payment": ["payment", "refund", "money", "wallet"]
}


def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text


def extract_topics(reviews):
    """
    Extracts raw topics from reviews with high recall.
    Returns a list of short topic phrases.
    """
    topics = []

    for review in reviews:
        text = review.get("text", "")
        if not text:
            continue

        clean_text = normalize_text(text)
        words = clean_text.split()

        # Remove stopwords
        words = [w for w in words if w not in STOPWORDS]

        # Detect issue categories
        for category, keywords in ISSUE_KEYWORDS.items():
            if any(k in words for k in keywords):
                # Build a short topic phrase
                matched_words = [w for w in words if w in keywords]
                if matched_words:
                    topic = f"{category} {' '.join(matched_words)}"
                else:
                    topic = category

                topics.append(topic.strip())

    return topics
