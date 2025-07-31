# Gemini-AI
KANI's GPT 🔮
A simple Streamlit web app that integrates with Google's Gemini API (via `google-generativeai`) to answer user questions using state-of-the-art language models.
## 🚀 Features
- ✅ Ask any question and get AI-generated answers.
- ✅ Simple, clean UI built with Streamlit.
- ✅ Powered by `gemini-pro` from Google Generative AI.
## 📁 Project Structure
├── app.py # Streamlit app code
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## 🧠 Tech Stack

- [Streamlit](https://streamlit.io/)
- [Google Generative AI Python SDK](https://pypi.org/project/google-generativeai/)
- Gemini Pro Model (`gemini-pro`)

## 🔐 Setup

> ⚠️ You'll need an API key from Google AI Studio: https://makersuite.google.com/app/apikey

### 1. Clone the repo

```bash
git clone https://github.com/your-username/kanis-gpt.git
cd kanis-gpt
```
### 2. Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the app
streamlit run app.py

### ⚙️Configuration
Replace the API key in app.py with your own:

genai.configure(api_key="YOUR_API_KEY_HERE")

### 📦requirements.txt
streamlit
google-generativeai

### 📄 License
This project is open source and available under the MIT License.
