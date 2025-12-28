def deduplicate_topics(raw_topics):
    
    return raw_topics
import json
import os
from difflib import SequenceMatcher

MEMORY_FILE = os.path.join("memory", "topic_registry.json")
SIMILARITY_THRESHOLD = 0.75


def load_topic_registry():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_topic_registry(registry):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2)


def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


def deduplicate_topics(raw_topics):
    
    registry = load_topic_registry()
    canonical_topics = []

    for topic in raw_topics:
        topic = topic.lower().strip()
        matched = False

        for canonical, variants in registry.items():
            score = similarity(topic, canonical)

            if score >= SIMILARITY_THRESHOLD:
               
                if topic not in variants:
                    variants.append(topic)
                canonical_topics.append(canonical)
                matched = True
                break

        if not matched:
            
            registry[topic] = [topic]
            canonical_topics.append(topic)

    save_topic_registry(registry)
    return canonical_topics

