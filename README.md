# README

# 🧠 Data Cleanup & Profiling Agent (100% Local)

This project implements a **local autonomous AI agent** that behaves like a junior data scientist:
it loads a CSV file, analyzes it, decides how to clean it, applies transformations, and documents what it did.

Everything runs **locally**, on **CPU**, with an **open-source LLM**.

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


