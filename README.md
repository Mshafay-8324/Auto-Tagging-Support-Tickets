# 🎫 AI-Powered Support Ticket Auto-Tagging System

An AI-powered support ticket classification system that automatically predicts the most relevant categories for customer support requests using Large Language Models (LLMs). The project explores **Zero-Shot** and **Few-Shot Prompting** techniques with the Groq API and LLaMA 3.1, providing an interactive Streamlit interface for real-time ticket classification.

This project was developed as part of the **DevelopersHub Corporation AI/ML Engineering Internship (Phase 2 - Task 5).**

---

## 🚀 Features

- AI-powered support ticket classification
- Zero-Shot Prompting
- Few-Shot Prompting
- Interactive Streamlit web interface
- Top-3 category prediction
- Prompt engineering experimentation
- Groq API integration
- LLaMA 3.1 8B Instant model
- Clean and responsive UI

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Groq API
- LLaMA 3.1 8B Instant
- Prompt Engineering
- Pandas
- python-dotenv

---

## 📂 Project Structure

```text
Auto-Tagging-Support-Tickets/
│
├── app.py
├── streamlit_app.py
├── evaluate.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env                 # Not included in repository
├── ticket.csv           # Local dataset
└── venv/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Auto-Tagging-Support-Tickets.git

cd Auto-Tagging-Support-Tickets
```

---

### 2. Create a virtual environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` file

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Running the Project

### Terminal Version

```bash
python app.py
```

---

### Streamlit Version

```bash
streamlit run streamlit_app.py
```

---

## 🧠 Prompting Techniques

### Zero-Shot Prompting

The model classifies support tickets without seeing any prior examples.

Example:

```
Ticket:
The application crashes whenever I upload a file.
```

Predicted Categories

```
Bug Report
Performance Issue
Data Sync Issue
```

---

### Few-Shot Prompting

The model receives several labelled examples before classifying a new support ticket.

This improves prediction quality by giving the LLM contextual guidance through prompt engineering.

---

## 📋 Supported Categories

- Feature Request
- Subscription Cancellation
- Performance Issue
- Security Concern
- Login Issue
- Payment Problem
- Bug Report
- Refund Request
- Data Sync Issue
- Account Suspension

---

## 📊 Evaluation

An evaluation pipeline is included to compare model predictions against dataset labels.

During experimentation, it was observed that the provided dataset contains **label inconsistencies**, where identical ticket descriptions are associated with different categories. Because of this, quantitative accuracy alone is not a reliable indicator of model performance.

The project therefore emphasizes **prompt engineering** and qualitative evaluation of Zero-Shot and Few-Shot prompting strategies.

---

## 📸 Application Preview

### Streamlit Interface

- Ticket input box
- Zero-Shot mode
- Few-Shot mode
- Top-3 predicted categories
- Interactive and responsive UI

---

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Large Language Models (LLMs)
- Prompt Engineering
- Zero-Shot Learning
- Few-Shot Learning
- AI-powered text classification
- API integration
- Streamlit application development
- Python programming
- Generative AI workflows

---

## 📌 Future Improvements

- Confidence score estimation
- Multi-label classification
- Batch ticket processing
- Export predictions to CSV
- Retrieval-Augmented ticket classification
- Fine-tuned classification models
- Support for custom category sets
- Docker deployment

---

## 👨‍💻 Author

**Mohammad Shafay**

AI/ML Engineering Intern

DevelopersHub Corporation

GitHub: https://github.com/Mshafay-8324

---

## 📄 License

This project was developed for educational purposes as part of the DevelopersHub AI/ML Engineering Internship.
