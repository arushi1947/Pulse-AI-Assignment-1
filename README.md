# 📈 TrendPulse AI – Agentic Review Trend Detection System

## Overview

TrendPulse AI is an agentic AI-powered trend detection system designed to analyze large volumes of user reviews and identify emerging feedback patterns over time.

The system processes reviews in daily batches, extracts high-recall topics using LLM-powered agents, intelligently merges semantically similar topics through persistent memory, and generates rolling trend reports to help organizations monitor evolving user sentiment and product feedback.

Unlike traditional topic modeling approaches such as LDA or TopicBERT, TrendPulse AI leverages a modular agent architecture that prioritizes semantic understanding, consistency, scalability, and maintainability.


## 🚀 Key Features

### 🤖 Agentic AI Architecture

* Modular multi-agent pipeline
* Independent agents with specialized responsibilities
* Easy to extend and maintain

### 📝 Intelligent Topic Extraction

* LLM-based topic identification
* High-recall feedback extraction
* Captures nuanced user concerns and suggestions

### 🧠 Persistent Memory System

* Topic registry for long-term memory
* Maintains consistency across processing cycles
* Prevents duplicate topic creation

### 🔄 Semantic Deduplication

* Detects semantically similar topics
* Merges related feedback themes
* Improves trend accuracy and reporting quality

### 📊 Trend Analytics

* Daily topic aggregation
* Rolling 30-day trend analysis
* Historical topic tracking
* CSV report generation

### ⚡ Scalable Processing

* Batch-based review ingestion
* Suitable for large review datasets
* Modular processing pipeline


## 🏗️ System Architecture

```text
Daily Review Batch
        │
        ▼
┌──────────────────┐
│ Ingestion Agent  │
└──────────────────┘
        │
        ▼
┌─────────────────────────┐
│ Topic Extraction Agent  │
│     (LLM Powered)       │
└─────────────────────────┘
        │
        ▼
┌─────────────────────────┐
│ Deduplication Agent     │
│ Semantic Similarity     │
└─────────────────────────┘
        │
        ▼
┌─────────────────────────┐
│ Persistent Topic Memory │
│      Registry           │
└─────────────────────────┘
        │
        ▼
┌─────────────────────────┐
│ Daily Topic Counts      │
└─────────────────────────┘
        │
        ▼
┌─────────────────────────┐
│ Trend Aggregation Agent │
└─────────────────────────┘
        │
        ▼
30-Day Trend Report (CSV)
```


## 📂 Project Structure

```bash
trendpulse-ai/
│
├── agents/
│   ├── ingestion_agent.py
│   ├── topic_extraction_agent.py
│   ├── deduplication_agent.py
│   └── trend_agent.py
│
├── data/
│
├── memory/
│   ├── topic_registry.json
│   └── daily_topics/
│
├── output/
│
├── main.py
└── README.md
```

---

## ⚙️ How It Works

### 1. Ingestion Agent

* Reads daily review batches
* Validates and prepares data
* Passes reviews to downstream agents

### 2. Topic Extraction Agent

* Uses LLM-powered reasoning
* Extracts user feedback themes
* Generates candidate topics

### 3. Deduplication Agent

* Compares new topics against memory
* Identifies semantic similarity
* Prevents duplicate topic creation

### 4. Persistent Memory

* Stores canonical topics
* Maintains topic history
* Enables long-term consistency

### 5. Trend Aggregation Agent

* Aggregates topic frequencies
* Tracks trend evolution
* Produces rolling trend reports


## 🛠️ Technology Stack

### Core Technologies

* Python
* JSON-based Memory Store

### AI & NLP

* Large Language Models (LLMs)
* Semantic Similarity Matching
* Topic Extraction
* Text Analysis

### Data Processing

* Batch Processing
* Trend Aggregation
* CSV Reporting


## 📊 Output

The system generates trend reports showing:

* Emerging user concerns
* Frequently discussed topics
* Topic growth over time
* Long-term feedback patterns
* Product improvement opportunities

Example Output:

```csv
Topic,Frequency,Trend
Login Issues,152,Increasing
App Crashes,89,Stable
Battery Drain,64,Increasing
UI Improvements,45,Decreasing
```


## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/trendpulse-ai.git
cd trendpulse-ai
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python main.py
```

---
