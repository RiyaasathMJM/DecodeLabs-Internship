# 🤖 DecodeLabs — Project 1: Rule-Based AI Chatbot

**Batch 2026 | Powered by DecodeLabs**

[![Phase](https://img.shields.io/badge/Phase-3_Complete-success)]()
[![Architecture](https://img.shields.io/badge/Architecture-Deterministic-blue)]()
[![Complexity](https://img.shields.io/badge/Complexity-O(1)-brightgreen)]()
[![Flask](https://img.shields.io/badge/Backend-Flask-red)]()
[![License](https://img.shields.io/badge/License-MIT-yellow)]()

---

## 📋 Overview

A professional **Rule-Based AI Chatbot** built as part of the DecodeLabs Industrial Training Kit. This project demonstrates mastery of **Control Flow and Logic** through a deterministic, white-box architecture — no neural networks, no black boxes, just clean logic.

> 💡 **Key Principle:** Every response is traceable, explainable, and reproducible. Hallucination risk: **0%**.

---

## 🏗️ Architecture

| Component | Implementation |
|-----------|----------------|
| **Type** | Deterministic Logic Engine (System 2) |
| **Data Structure** | Hash Map / Dictionary |
| **Lookup Complexity** | O(1) Constant Time |
| **Model** | IPO (Input → Process → Output) |
| **Backend** | Flask (Python) |
| **Frontend** | Vanilla JS + HTML/CSS |
| **Hallucination Risk** | 0% |

### System Flow

```
User Input
    │
    ▼
Input Sanitization
(lowercase + strip whitespace)
    │
    ▼
Fuzzy Keyword Matching
    │
    ▼
Hash Map Lookup  ──→  O(1) Response Retrieval
    │
    ▼
Output to UI
```

---

## 🎯 Key Features

- ✅ **Hash Map response engine** — no messy if-elif chains
- ✅ **Input sanitization** — case & whitespace normalization
- ✅ **Fuzzy keyword matching** — handles partial and near-match inputs
- ✅ **Multi-user session management** — isolated per-user context
- ✅ **Conversation history tracking** — maintains chat state
- ✅ **White-box traceability** — every decision is explainable
- ✅ **RESTful API architecture** — clean Flask endpoints
- ✅ **Responsive dark-themed UI** — mobile-friendly design

---

## 🗂️ Project Structure

```
decode-labs-project1-chatbot/
│
├── app.py                  # Flask app entry point
├── chatbot.py              # Core rule-based logic engine
├── responses.py            # Hash map of intents and responses
├── requirements.txt        # Python dependencies
│
├── static/
│   ├── css/
│   │   └── style.css       # Dark theme UI styles
│   └── js/
│       └── chat.js         # Frontend chat logic
│
├── templates/
│   └── index.html          # Main chat interface
│
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/RiyaasathMJM/decode-labs-project1-chatbot.git
cd decode-labs-project1-chatbot

# 2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

### Access the App

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

---

## 🔌 API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Serves the chat UI |
| `POST` | `/chat` | Accepts user message, returns bot response |
| `GET` | `/history` | Returns conversation history for session |
| `DELETE` | `/reset` | Clears current session history |

### Example Request

```bash
curl -X POST http://127.0.0.1:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "hello"}'
```

### Example Response

```json
{
  "response": "Hello! How can I help you today?",
  "intent": "greeting",
  "confidence": "exact_match"
}
```

---

## 🧠 How It Works

### 1. Input Sanitization

```python
def sanitize(text):
    return text.strip().lower()
```

### 2. Hash Map Lookup (O(1))

```python
responses = {
    "hello":   "Hello! How can I help you today?",
    "bye":     "Goodbye! Have a great day.",
    "help":    "Sure! Ask me anything.",
    # ... more intents
}
```

### 3. Fuzzy Keyword Matching

If an exact match isn't found, the engine scans the input for known keywords and returns the best partial match.

---

## 📦 Dependencies

```txt
Flask==3.0.0
```

Install all at once:

```bash
pip install -r requirements.txt
```

---

## 🧪 Running Tests

```bash
python -m pytest tests/
```

---



## 🛣️ Roadmap

- [x] Phase 1 — Core hash map engine
- [x] Phase 2 — Flask REST API
- [x] Phase 3 — Fuzzy matching + session management
- [ ] Phase 4 — Intent confidence scoring
- [ ] Phase 5 — Admin dashboard for response management

---

## 👨‍💻 Author

Built with ❤️ as part of the **DecodeLabs Industrial Training Program — Batch 2026**.

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
