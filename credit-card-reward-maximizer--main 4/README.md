# 💳 Credit Card Reward Maximizer (Gemini + RAG Edition)

An AI-powered credit card rewards comparison tool that helps users find the best credit card for their spending habits and maximize rewards using Retrieval-Augmented Generation (RAG).

---

## 🚀 Overview

Credit Card Reward Maximizer analyzes credit card reward programs and recommends the best card based on:

- Spending category  
- Purchase amount  
- Selected credit cards  

This version is powered by:

- **Google Gemini (LLM)**
- **HuggingFace Local Embeddings**
- **FAISS Vector Database**
- **Streamlit Web Interface**

No OpenAI dependency. Fully updated to Gemini architecture.

---

## ✨ Features

### 🔍 Smart AI Recommendations
- Compares multiple credit cards
- Extracts reward rates from official websites
- Calculates estimated earnings
- Recommends the best card with explanation

### 🎯 Flexible Inputs
- Select multiple credit cards
- Choose spending category
- Optional vendor input
- Enter purchase amount

### 🧠 AI + RAG Architecture
- Scrapes official card websites
- Splits content into chunks
- Creates vector embeddings
- Retrieves relevant reward rules
- Uses Gemini to analyze and recommend

---

## 🧠 Technology Stack

| Component | Technology |
|------------|------------|
| Frontend | Streamlit |
| LLM | Google Gemini (`gemini-pro-latest`) |
| Embeddings | HuggingFace (`all-MiniLM-L6-v2`) |
| Vector Store | FAISS |
| Web Scraping | Requests + BeautifulSoup |
| Orchestration | LangChain |

---

## 🛠 Installation

### 🔹 Prerequisites

- Python 3.9+
- pip
- Google Gemini API Key

---

### 1️⃣ Clone Repository

```bash
git clone <your-repository-url>
cd credit-card-reward-maximizer
```

---

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
pip install langchain-google-genai google-generativeai sentence-transformers
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in project root:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

Get API key from:

https://aistudio.google.com/app/apikey

---

### 5️⃣ Run Application

```bash
streamlit run app.py
```

App runs at:

```
http://localhost:8501
```

---

## 🔄 How It Works

### 1️⃣ Data Collection
- Scrapes official credit card pages
- Cleans HTML content
- Extracts reward information

### 2️⃣ RAG Processing
- Splits content into 800-character chunks
- Converts chunks into vector embeddings (HuggingFace)
- Stores embeddings in FAISS
- Retrieves relevant reward text per card

### 3️⃣ AI Analysis
- Gemini processes retrieved reward data
- Extracts reward percentages
- Calculates estimated earnings
- Recommends best credit card

---

## 📂 Project Structure

```
credit-card-reward-maximizer/
│
├── app.py
├── cards_data.py
├── llm.py
├── rag.py
├── web_fetcher.py
├── requirements.txt
├── README.md
└── .env (not committed)
```

---

## ⚠️ Notes

- Some websites use heavy JavaScript; static scraping may not capture dynamic content.
- Gemini free tier has rate limits.
- Designed for academic and demonstration purposes.

---

## 🎓 Academic Highlights

This project demonstrates:

- Retrieval-Augmented Generation (RAG)
- Vector embeddings & similarity search
- AI-powered recommendation systems
- Web scraping integration
- LangChain-based LLM orchestration
- Real-world AI application design

---

## 📌 Disclaimer

This tool provides informational analysis. Credit card rewards, terms, and conditions may change. Always verify details with official issuers.

---

## 👨‍💻 Author

Developed as part of a university AI project.

---

**Version:** Gemini + Local Embeddings Edition  
