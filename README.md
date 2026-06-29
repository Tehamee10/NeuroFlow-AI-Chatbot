# 🧠 NeuroFlow AI Chatbot

An AI-powered chatbot built with **Next.js**, **FastAPI**, **Pinecone**, **FastEmbed**, and **Google Gemini**. The chatbot uses Retrieval-Augmented Generation (RAG) to answer questions based on uploaded documents.

---

## 🚀 Features

* AI-powered conversational chatbot
* Document-based question answering
* FastAPI backend
* Next.js frontend
* Pinecone vector database
* FastEmbed for text embeddings
* Google Gemini for natural language generation
* Responsive chat interface
* Real-time communication between frontend and backend

---

## 🛠️ Tech Stack

### Frontend

* Next.js
* React
* Axios
* CSS

### Backend

* Python
* FastAPI
* Google Gemini API
* Pinecone
* FastEmbed
* python-dotenv

---

## 📂 Project Structure

```
NeuroFlow-AI-Chatbot
│
├── frontend-next/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── api.py
├── chatbot.py
├── upload.py
├── NeuroFlow_Complete_Documentation.docx
├── package.json
└── README.md
```

---

## ⚙️ How It Works

1. Upload a document.
2. The document is split into smaller chunks.
3. FastEmbed converts each chunk into vector embeddings.
4. Pinecone stores the embeddings.
5. When a user asks a question:

   * The query is converted into an embedding.
   * Pinecone retrieves the most relevant document chunks.
   * Gemini generates a natural-language response using the retrieved context.
6. The response is displayed in the Next.js chatbot interface.

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/Tehamee10/NeuroFlow-AI-Chatbot.git
```

### Backend

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```
PINECONE_API_KEY=YOUR_PINECONE_API_KEY
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Run the backend:

```bash
python -m uvicorn api:app --reload
```

---

### Frontend

```bash
cd frontend-next
npm install
npm run dev
```

Open:

```
http://localhost:3000
```

---

## 🧠 RAG Architecture

```
User Question
      │
      ▼
Next.js Frontend
      │
      ▼
FastAPI Backend
      │
      ▼
FastEmbed
(Query Embedding)
      │
      ▼
Pinecone
(Vector Search)
      │
      ▼
Relevant Document Chunks
      │
      ▼
Google Gemini
(Response Generation)
      │
      ▼
Chatbot Response
```

---

## 📸 Demo

Example Questions:

* What is NeuroFlow?
* What problem does NeuroFlow solve?
* What are the core features of NeuroFlow?
* How does NeuroFlow reduce cognitive load?
* Explain the architecture of NeuroFlow.

---

## 🔮 Future Improvements

* User authentication
* Chat history
* File upload from frontend
* Multiple document support
* Streaming AI responses
* Docker deployment
* Cloud deployment (Render/Vercel)

---

## 👨‍💻 Author

**Tehamee Raheel**

* Artificial Intelligence Undergraduate
* Dawood University of Engineering & Technology
* Passionate about AI, LLMs, NLP, and Generative AI

---

## 📄 License

This project is created for educational and internship assessment purposes.
