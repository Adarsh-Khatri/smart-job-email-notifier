# 🚀 # 🚀 Smart Job Email Notifier
AI-powered system to detect job-related emails and send instant Telegram alerts.


An AI-powered system that automatically detects job-related emails from Gmail and sends real-time alerts to Telegram.

---

## 📌 Overview

# 🚀 Smart Job Email Notifier is a smart email monitoring system that filters important job, internship, and placement-related emails using NLP-based logic and instantly notifies the user via Telegram.

This project automates the job search process by ensuring that no important opportunity is missed.

---

## ✨ Features

* 📩 Fetch emails using Gmail API
* 🤖 Intelligent job email detection (keyword/NLP-based)
* 📲 Instant Telegram notifications
* 🔁 Duplicate email prevention system
* ⏱️ Automated periodic email checking
* 🔐 Secure authentication using OAuth 2.0

---

## 🏗️ System Architecture

Gmail API → Email Fetcher → AI Classifier → Filtered Emails → Telegram Bot

---

## 🛠️ Tech Stack

* **Python**
* **Gmail API**
* **Telegram Bot API**
* **FastAPI** (optional backend)
* **Schedule (automation)**

---

## 📂 Project Structure

```
smart-job-email-notifier
/
│
├── main.py
├── email_reader.py
├── classifier.py
├── telegram.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/your-username/smart-job-email-notifier.git
cd smart-job-email-notifier

```

---

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Setup Gmail API

* Go to Google Cloud Console
* Enable Gmail API
* Create OAuth Credentials (Desktop App)
* Download `credentials.json`

---

### 5. Setup Telegram Bot

* Create bot using BotFather
* Get BOT TOKEN
* Get CHAT ID

---

### 6. Create `.env` file

```
TELEGRAM_TOKEN=your_token_here
CHAT_ID=your_chat_id
```

---

### 7. Run the Project

```
python main.py
```

---

## 🔄 Automation

The system runs continuously and checks for new job emails at fixed intervals.

---

## 🔐 Security

Sensitive files like:

* `.env`
* `credentials.json`
* `token.json`

are excluded using `.gitignore`.

---

## 🚀 Future Enhancements

* 🧠 ML-based email classification (BERT / NLP models)
* 📊 Dashboard using FastAPI
* 📅 Job deadline extraction
* 📬 Multi-email account support
* ☁️ Cloud deployment for 24/7 execution

---

## 💡 Use Case

This system helps students and job seekers stay updated with opportunities without manually checking emails.

---

## 👨‍💻 Author

Adarsh Khatri

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
