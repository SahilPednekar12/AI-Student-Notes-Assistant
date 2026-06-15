# 📚 AI Study Assistant

An AI-powered learning platform that transforms study notes into **Revision Notes**, **Interactive Quizzes**, **Interview Questions**, and **AI-powered note-based conversations** using **Google Gemini** and **Streamlit**.

---

## 🚀 Features

### 📝 Revision Notes Generator

* Upload PDF, DOCX, or TXT notes
* Generate structured revision notes
* Download revision notes as PDF

### 🎯 Interactive Quiz Generator

* Generate MCQ quizzes from uploaded notes
* Auto-evaluate answers
* Instant score calculation
* Percentage-based performance analysis

### 🎤 Interview Questions Generator

* Generate interview questions from study material
* AI-generated answers included
* Download interview questions as PDF

### 💬 Chat With Notes

* Ask questions directly from uploaded notes
* AI answers based only on note content
* Session-based chat history
* Clear chat functionality

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Model

* Google Gemini 2.5 Flash

### Libraries Used

* google-generativeai
* streamlit
* PyPDF2
* python-docx
* reportlab
* python-dotenv

---

## 📂 Project Structure

```text
AI_Study_Assistant/
│
├── app.py
├── file_reader.py
├── revision_generator.py
├── quiz_generator.py
├── interview_generator.py
├── chat_generator.py
├── pdf_generator.py
│
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
└── uploads/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/SahilPednekar12/AI-Student-Notes-Assistant.git
```

### Move into Project Directory

```bash
cd AI-Student-Notes-Assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Get your free API key from:

https://aistudio.google.com/

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📸 Application Workflow

```text
Upload Notes
      │
      ▼
Extract Text
      │
      ▼
 ┌──────────────┬──────────────┬──────────────┬──────────────┐
 │ Revision     │ Quiz         │ Interview    │ Chat         │
 │ Notes        │ Generator    │ Questions    │ With Notes   │
 └──────────────┴──────────────┴──────────────┴──────────────┘
      │
      ▼
Google Gemini AI
      │
      ▼
Generated Study Material
```

---

## 🎯 Use Cases

* Students preparing for exams
* Interview preparation
* Quick revision before assessments
* Self-learning and note summarization
* AI-powered study assistance

---

## 🌟 Future Improvements

* Flashcard Generation
* Study Planner
* Topic-wise Difficulty Analysis
* Chat Export
* Multiple Document Support
* User Authentication
* Cloud Deployment

---

## 👨‍💻 Author

### Sahil Pednekar

AI & Machine Learning Enthusiast

GitHub: https://github.com/SahilPednekar12

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
