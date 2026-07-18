# 🧠 Hybrid AI Vitamin Chatbot

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.x-black.svg)
![AI](https://img.shields.io/badge/AI-HuggingFace-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A full-stack AI chatbot built with **Flask**, combining a **rule-based expert system** and a **Large Language Model (LLM)** to answer questions about vitamins, nutrition, and dietary supplements.

Unlike traditional chatbots that send every request to an LLM, this project intelligently routes user queries to the most appropriate engine:

- ⚡ Fast Rule Engine for common questions
- 🤖 Hugging Face LLM for complex reasoning
- 🧠 Hybrid Router that decides which engine should answer

---

# Demo

> **Coming Soon**

Add a screenshot here after uploading one to:

```
docs/images/chatbot_home.png
```

```markdown
![Application Screenshot](docs/images/chatbot_home.png)
```

---

# Features

- Hybrid AI Architecture
- Rule-based Expert System
- Hugging Face LLM Integration
- Intelligent Query Routing
- REST API using Flask
- Modern Chat Interface
- Processing Time Metrics
- Response Metadata
- Logging
- Responsive UI
- Environment-based Configuration

---

# System Architecture

```text
                        User
                          │
                          ▼
                HTML / CSS / JavaScript
                          │
                          ▼
                    Flask REST API
                          │
                          ▼
              HybridChatbotService
                          │
             ┌────────────┴────────────┐
             ▼                         ▼
        Rule Engine              AI Service
             │                         │
             ▼                         ▼
    Knowledge Base            Hugging Face LLM
```

---

# Project Structure

```text
HybridAIVitaminChatbot/

├── ai/
│   ├── ai_service.py
│   ├── factory.py
│   └── providers/
│       └── huggingface_provider.py
│
├── chatbot/
│   ├── knowledge_base.json
│   └── rule_engine.py
│
├── services/
│   └── hybrid_chatbot_service.py
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── logs/
│
├── app.py
├── config.py
├── logging_config.py
├── requirements.txt
├── README.md
└── .env
```

---

# Technology Stack

## Backend

- Python
- Flask
- Hugging Face Inference API
- Logging

## Frontend

- HTML5
- CSS3
- JavaScript

## AI

- Hugging Face Hub
- Qwen2.5 Instruct Model

---

# Intelligent Routing

The application automatically determines whether a question should be answered by the Rule Engine or the AI model.

### Rule Engine Examples

```
Hello

What is Vitamin C?

Symptoms of Iron deficiency

Sources of Vitamin D
```

These receive near-instant responses.

---

### AI Examples

```
Explain the biochemical pathway of Vitamin D metabolism.

Compare Vitamin D2 and Vitamin D3.

What are the latest discoveries in Vitamin D research?
```

These are routed to the Large Language Model.

---

# Example API Response

```json
{
    "success": true,
    "source": "huggingface",
    "provider": "huggingface",
    "model": "Qwen/Qwen2.5-7B-Instruct",
    "response": "...",
    "processing_time_ms": 1734.26
}
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/SaiChaitanyaBond/HybridAIVitaminChatbot.git

cd HybridAIVitaminChatbot
```

Create a virtual environment

macOS / Linux

```bash
python3 -m venv hybrid_ai_chatbot_venv

source hybrid_ai_chatbot_venv/bin/activate
```

Windows

```bash
python -m venv hybrid_ai_chatbot_venv

hybrid_ai_chatbot_venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Configuration

Create a `.env` file.

Example

```text
HUGGINGFACE_API_TOKEN=your_token_here

HUGGINGFACE_MODEL=Qwen/Qwen2.5-7B-Instruct
```

---

# Run

```bash
python app.py
```

Open

```
http://localhost:5001
```

---

# Testing

Rule Engine

```bash
python test_rule_engine.py
```

AI Provider

```bash
python test_huggingface.py
```

Hybrid Service

```bash
python test_hybrid_chatbot.py
```

---

# Future Enhancements

- Conversation Memory
- Chat History
- Streaming Responses
- Markdown Rendering
- Docker Deployment
- Azure App Service Deployment
- GitHub Actions CI/CD
- User Authentication
- Dark Mode
- Retrieval-Augmented Generation (RAG)
- Vector Database Integration

---

# Educational Objectives

This project demonstrates:

- AI Application Development
- Hybrid AI Systems
- Expert Systems
- REST APIs
- Flask
- Large Language Models
- Software Architecture
- Modular Design
- Frontend Integration
- Python Best Practices

---

# Disclaimer

This application is intended for educational purposes only.

It does **not** provide medical advice, diagnosis, or treatment recommendations.

Always consult a qualified healthcare professional regarding medical concerns.

---

# Author

**Sai Chaitanya Bondada**

GitHub

https://github.com/SaiChaitanyaBond

Repository

https://github.com/SaiChaitanyaBond/HybridAIVitaminChatbot

---

If you found this project useful, please consider giving it a ⭐.