# README

# 🧠 Data Cleanup & Profiling Agent (100% Local)

This project implements a **local autonomous AI agent** that behaves like a junior data scientist:
it loads a CSV file, analyzes it, decides how to clean it, applies transformations, and documents what it did.

Everything runs **locally**, on **CPU**, with an **open-source LLM**.

Given a CSV file and a goal (“prepare this dataset for ML”), the agent:
- inspects the dataset
- detects data quality issues
- decides how to clean them
- applies transformations
- documents what it did

---

## 🏗 Architecture

User goal

↓

LLM (Mistral via Ollama)

↓

Agent loop (plan → act → observe)

↓

Python tools (pandas)

↓

Cleaned dataset + report

The LLM does not manipulate data directly.  
It decides which tools to call and why.

LLM as an autonomous decision-maker controlling a data pipeline.
The agent uses:
- a planning loop
- memory
- tool calling
- self-correction

---

## 🧠 Tech stack

- Python
- Pandas
- Ollama (local LLM server)
- Mistral 7B (open-source LLM)

No cloud. No API keys.

---

## 🚀 Setup

### 1. Install Ollama

Linux:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Mac:
```bash
brew install ollama
```

Start Ollama:
```bash
ollama serve
```

Pull the model:
```bash
ollama pull mistral
```

Test:
```bash
ollama run mistral
```

---

### 2. Python environment
```bash
python -m venv venv
source venv/bin/activate
pip install pandas requests
```

---

## 🧪 Run (work in progress)
Put a CSV file in data/sample.csv, then:
```bash
python main.py
```

You will see the LLM:
- inspect the dataset
- decide cleaning actions
- apply them
- iterate until it decides the dataset is ready

## 🧪 What this demonstrates

How LLMs can act as policy networks

How to build tool-using agents without LangChain or frameworks

How to design traceable, controllable AI systems for data workflows
