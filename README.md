# 📧 Agentic RAG Email Responder

This project implements an **Agentic Retrieval-Augmented Generation (RAG)** pipeline that classifies customer emails, retrieves answers from a structured knowledge base, generates a reply, and sends it via email.

## 🚀 Features

- 🔍 Email classification (intent and category detection)
- 📚 Knowledge base retrieval using semantic embeddings
- 🧠 LLM-based response generation
- 📩 Automatic email reply via SMTP
- 🧱 Modular agent-based architecture

## 📁 Project Structure

├── main.py
├── .env
├── kb.csv
└── agents/
├── loader_agent.py
├── indexer_agent.py
├── classifier_agent.py
├── retriever_agent.py
├── responder_agent.py
└── email_sender_agent.py

---

## 🔧 Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/agentic-rag-email.git
cd agentic-rag-email
```
### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a .env file in the project root with your email credentials:

```bash
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

## How to Use

You can use the system by calling the function in main.py:
```bash
recipient = "example@example.com"
email_text = "Hi, I want to track my order placed last week. Can you help me?"
agentic_rag_pipeline_with_email(email_text, recipient)

```
Sample Output:
```bash
Classification: {'category': 'Shipping', 'intent': 'track_order'}
Retrieved Context: You can track your order using the link provided...
Reply: Hello! Thanks for reaching out. You can track your order using the link provided...
Email sent successfully to example@example.com

```