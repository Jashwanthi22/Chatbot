#  Chatbot J

A conversational AI assistant developed by **Jashwanthi.K**, built with [Streamlit](https://www.google.com/search?q=https%3A%2F%2Fstreamlit.io%2F) and powered by [Groq](https://www.google.com/search?q=https%3A%2F%2Fgroq.com%2F) using [LangChain](https://www.google.com/search?q=https%3A%2F%2Fwww.langchain.com%2F).

## Features
- **Custom Landing Screen**: Branded welcome page with a one-click start button.
- **Interactive Multi-Turn Chat**: Fast response generation via Groq's `openai/gpt-oss-20b` model.
- **Crimson & Wine Theme**: Styled in a custom dark-mode crimson aesthetic.
- **Sidebar Controls**: Easy navigation and instant chat history reset.

## Quickstart

### 1. Clone & Set Up Environment
```bash
git clone https://github.com/YOUR_USERNAME/Chatbot-J.git
cd Chatbot-J
python -m venv .venv

# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Add API Key
Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Run the App
```bash
streamlit run chatbotv2.py
```

## Tech Stack
- **Frontend**: Streamlit
- **LLM**: Groq (`openai/gpt-oss-20b`)
- **Framework**: LangChain (`langchain-groq`)

---
**Author**: [Jashwanthi.K](https://www.google.com/search?q=https%3A%2F%2Fgithub.com%2F)
