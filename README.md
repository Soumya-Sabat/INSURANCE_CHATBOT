# INSURANCE_CHATBOT
# 🤖 NextGen Insurance & Career Chatbot

The **NextGen Insurance & Career Chatbot** is a dual-mode AI-powered assistant built entirely in Python. It combines smart insurance services with domain-specific career guidance using the latest technologies like Google Gemini API, OCR, sentiment analysis, and resume parsing.

---

## 🚀 Features

### 🛡 Insurance Bot
- Real-time insurance **quote calculation**
- Personalized **insurance recommendations** based on age/job
- OCR-powered **claim assistant**
- **Sentiment-based responses** for better user engagement

### 🎓 Career Bot
- Analyze **PDF resumes** to suggest career domains
- **Gemini API-based Q&A** for domains like:
  - Data Science
  - Blockchain
  - Cybersecurity
  - Web Development
  - Android Development
- Dynamic answer fetching and **auto-saving to JSON**
- Tracks previous questions via **domain memory core**
- **Sentiment analysis** on queries

---

## 🧠 Technologies Used

| Tool/Lib            | Purpose                           |
|---------------------|-----------------------------------|
| Python 3.10+        | Core development language         |
| google-generativeai | Gemini 1.5 Flash API integration  |
| pytesseract         | OCR for image-to-text processing  |
| Pillow              | Image handling for claims         |
| fitz (PyMuPDF)      | Resume PDF text parsing           |
| TextBlob            | Sentiment analysis                |
| dotenv              | Secure API key management         |
| JSON                | Persistent local data storage     |

---

## 📁 Project Structure

```plaintext
insurance_chatbot/
├── main.py                    # 🔧 Insurance mode
├── main_career.py             # 🎓 Career mode
├── domain_bot.py              # 💡 Q&A engine
├── gemini_api.py              # 🔮 Gemini API interface
├── resume_analyzer.py         # 📄 Resume parser
├── sentiment_predictor.py     # 🧠 Sentiment classifier
├── claim_assistant.py         # 🧾 OCR claim processor
├── quote_calculator.py        # 💸 Quote calculator
├── recommender.py             # 🎯 Policy recommender
├── domain_qa.json             # 📚 Cached Q&A
├── domain_memory.json         # 🧠 Domain memory
├── policy.json                # 🛡 Policy data
├── chat_history.json          # 💬 Chat log (optional)
└── .env                       # 🔐 API key
