# 📄 SynthePDF.ai

**AI-powered PDF summarization and document Q&A.**  
Built with LangChain, Gemini (or OpenAI), and Streamlit.

---

## 🌟 About the Project

**SynthePDF.ai** is a lightweight web application that transforms long, complex PDFs into short, easy-to-read summaries using a large language model (LLM). Users can also ask follow-up questions about the uploaded document.

This project was built as a personal portfolio piece to demonstrate practical skills in:
- LLM orchestration with LangChain
- Building interactive AI applications with Streamlit
- PDF parsing and information extraction
- Prompt engineering and chain composition

---

## ✨ Features

- 📄 **Upload PDF files** (any length)
- 🧠 **Summarize PDF content** using a custom LLM prompt
- ❓ **Ask questions** about the document contents
- 📋 Modern UI with clear output presentation
- 🔐 Secure environment variable handling for API keys

---

## 📸 Preview

![demo screenshot](https://your-screenshot-url-here)  
_The interface shows raw text preview, summary section, and an interactive Q&A input._

---

## 🛠️ Tech Stack

| Layer        | Technology                |
|--------------|---------------------------|
| Frontend     | Streamlit                 |
| LLM Routing  | LangChain                 |
| AI Model     | Google Gemini 2.0         |
| PDF Parsing  | PyMuPDF (`fitz`)          |
| Secrets Mgmt | `dotenv` + OS Environment |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/synthepdf-ai.git
cd synthepdf-ai
```
### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

```windows
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Set your API key
```
GOOGLE_API_KEY=your_google_gemini_api_key
```

### 5. Run the app
```
streamlit run app.py
```