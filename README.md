This project implements an agentic AI-based trend detection system to analyze user reviews from the Google Play Store and identify emerging feedback patterns over time.
The system processes reviews in daily batches, extracts high-recall feedback topics using an AI agent, intelligently deduplicates semantically similar topics using persistent memory, and generates rolling 30-day trend reports.
The solution avoids traditional topic modeling techniques such as LDA or TopicBERT and instead uses a modular agent architecture designed for robustness, scalability, and semantic consistency.
The solution follows an agent-based pipeline, where each agent has a single, well-defined responsibility.
Daily Review Batch
        ↓
Ingestion Agent
        ↓
Topic Extraction Agent (LLM-based)
        ↓
Topic Deduplication Agent
        ↓
Persistent Topic Registry (Memory)
        ↓
Daily Topic Counts
        ↓
Trend Aggregation Agent
        ↓
30-Day Topic Trend Report (CSV)
Folder Structure
pulsegen-trend-agent/
├── agents/
│   ├── ingestion_agent.py
│   ├── topic_extraction_agent.py
│   ├── deduplication_agent.py
│   └── trend_agent.py
│
├── data/                 
├── memory/
│   ├── topic_registry.json
│   └── daily_topics/
│
├── output/               

── main.py
└── README.md
