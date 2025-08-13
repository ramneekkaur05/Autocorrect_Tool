# ✏️ Autocorrect Tool
(setup instructions included at last)

This is a **Streamlit-based Autocorrect Application** that allows users to:

- ✅ Enter any text with spelling or grammatical mistakes  
- ✅ Automatically correct errors using **Google Gemini 1.5 Flash** (via LangChain)  
- ✅ Optionally switch to a simple correction mode using **TextBlob**  
- ✅ View corrected text instantly in an interactive UI  

---

## 📸 App Preview
- 📝 Input text in a clean **Streamlit text area**  
- ⚡ Instant correction results powered by AI  
- 🎯 Grammar and spelling corrected without changing meaning  
- 🔄 Uses **Gemini LLM** for intelligent context-aware correction  

---

## 🚀 Features
- ✍️ **Grammar + spelling correction** in one click  
- 🧠 **Context-aware** suggestions using Gemini LLM  
- 📚 Fallback option to **TextBlob** for offline correction  
- 🖥️ Minimal, easy-to-use **Streamlit UI**  
- 🔑 API key management using **python-dotenv**  

---

## 🧰 Tech Stack

| Component     | Technology             |
|--------------|------------------------|
| Frontend     | Streamlit              |
| LLM Engine   | LangChain              |
| LLM Model    | Google Gemini 1.5 Flash|
| Fallback     | TextBlob               |
| Env Vars     | python-dotenv          |

---

## ⚙️ Setup Instructions
Follow these steps to run the app locally on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/autocorrect-tool.git
cd autocorrect-tool
```
### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables
```bash
GOOGLE_API_KEY=your_google_api_key_here
```

### 5. Run the Streamlit App
```bash
streamlit run app.py
```
---

## Contributions are welcome! Please fork the repository and submit a pull request with your improvements 😊
