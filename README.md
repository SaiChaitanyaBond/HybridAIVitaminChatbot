# 🥗 Hybrid AI Vitamin Chatbot

A full-stack **Hybrid AI Chatbot** that combines a **rule-based expert system** with a **Large Language Model (LLM)** from Hugging Face to provide educational information about vitamins, minerals, nutrition, and supplements.

The chatbot intelligently routes simple questions to a fast rule engine while sending complex or open-ended questions to an AI model, providing both speed and flexibility.

---

## 🚀 Features

- 🤖 Hybrid AI Architecture
  - Rule-based chatbot for common questions
  - Hugging Face LLM for complex queries
- 🧠 Intelligent query routing
- 💬 Modern web chat interface
- ⚡ Fast responses for predefined knowledge
- 🌐 REST API using Flask
- 📊 Response metadata
  - Response source
  - AI model
  - Processing time
- 📝 Application logging
- 🎨 Responsive UI
- 🔒 Environment variable configuration

---

## 📸 Application

### Home Screen

<img src="docs/images/chatbot_home.png" width="900">

> *(Replace this image with a screenshot of your chatbot.)*

---

## 🏗️ Architecture

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

## 📁 Project Structure

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
├── .env
└── README.md
```

---

## ⚙️ Technology Stack

### Backend

- Python 3.11+
- Flask
- Hugging Face Inference API
- Python Logging

### Frontend

- HTML5
- CSS3
- JavaScript (ES6)

### AI

- Hugging Face Hub
- Qwen 2.5 Instruct Model

---

## 🧠 How It Works

The chatbot uses a hybrid decision process.

### Rule-Based Processing

Questions like:

- Hello
- Goodbye
- Tell me about Vitamin D deficiency
- What are the symptoms of Iron deficiency?

are answered immediately using the internal knowledge base.

---

### AI Processing

Questions like:

- Explain the biochemical pathway of Vitamin D metabolism.
- Compare Vitamin D2 and Vitamin D3.
- What are the latest discoveries regarding Vitamin D?

are routed to the Hugging Face Large Language Model.

---

## 📊 Example Response

```json
{
    "success": true,
    "source": "huggingface",
    "provider": "huggingface",
    "model": "Qwen/Qwen2.5-7B-Instruct",
    "response": "...",
    "processing_time_ms": 1842.17
}
```

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/<your-github-username>/HybridAIVitaminChatbot.git

cd HybridAIVitaminChatbot
```

---

### Create Virtual Environment

macOS/Linux

```bash
python3 -m venv hybrid_ai_chatbot_venv

source hybrid_ai_chatbot_venv/bin/activate
```

Windows

```bash
python -m venv hybrid_ai_chatbot_venv

hybrid_ai_chatbot_venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file.

Example:

```text
HUGGINGFACE_API_TOKEN=your_api_token
HUGGINGFACE_MODEL=Qwen/Qwen2.5-7B-Instruct
```

---

### Run the Application

```bash
python app.py
```

Open:

```
http://localhost:5001
```

---

## 🧪 Testing

Rule Engine

```bash
python test_rule_engine.py
```

Hugging Face Provider

```bash
python test_huggingface.py
```

Hybrid Chatbot

```bash
python test_hybrid_chatbot.py
```

---

## 📈 Future Enhancements

- Conversation memory
- Streaming AI responses
- Markdown rendering
- Dark mode
- User authentication
- Chat history
- Azure App Service deployment
- Docker support
- CI/CD using GitHub Actions
- Unit and integration testing
- Retrieval-Augmented Generation (RAG)

---

## 📚 Learning Objectives

This project demonstrates:

- Hybrid AI systems
- Rule-based expert systems
- Large Language Model integration
- REST API development
- Flask application architecture
- Frontend and backend integration
- Logging and monitoring
- Modular software design
- Python best practices

---

## ⚠️ Disclaimer

This chatbot is intended for **educational purposes only**.

It does **not** provide medical diagnosis or treatment recommendations.

Always consult a qualified healthcare professional for medical advice.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Sai Chaitanya Bondada**

GitHub: https://github.com/<your-github-username>

LinkedIn: *(Add your LinkedIn profile if desired.)*

---

⭐ If you found this project useful, consider giving it a star!
