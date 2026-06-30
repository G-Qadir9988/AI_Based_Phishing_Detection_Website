# 🛡️ AI Mental Health Companion System

[![React](https://img.shields.io/badge/Frontend-React%20%2B%20Vite-61dafb?logo=react)](https://react.dev/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/ML%2FNLP-Python%20%2B%20Scikit--Learn-3776AB?logo=python)](https://www.python.org/)
[![Firebase](https://img.shields.io/badge/Database-Firebase-FFCA28?logo=firebase)](https://firebase.google.com/)
[![License](https://img.shields.io/badge/License-Educational%20Use-green)](#-license)

### 🚀 AI-Powered Mental Health Analysis & Emotion Detection Platform

A professional AI-driven mental health companion system designed to analyze emotions, assess mental health risks, generate intelligent insights, and provide interactive analytics using NLP, Machine Learning, FastAPI, and React.

---

## 👨‍💻 Developed By
* **Noor Malik** & **Ghulam Qadir**
* 🎓 *Artificial Intelligence Lab – Final Semester Project*
* 🏫 *Air University, Islamabad*

---

## 📌 Project Description
The **AI Mental Health Companion System** is a modern web application designed to assist in emotional and mental health monitoring using advanced Machine Learning and Natural Language Processing (NLP). 

The platform seamlessly extracts emotional vectors from user text inputs and maps demographic variables to predict potential mental health constraints.

### Core Architecture Components:
* 🧠 **Emotion Detection using NLP:** Contextual understanding of conversational features.
* 📊 **Mental Health Risk Assessment:** Multi-variate predictive risk grouping.
* 📈 **AI Insights & Analytics:** Dynamic charts for trend forecasting.
* 📝 **Journal Analysis:** Text semantic parsing for mood monitoring.
* 🤖 **AI Prediction Models:** Classifiers optimized via Python training pipelines.

---

## ✨ Key Features

### 🧠 AI & Data Science
* **Emotion Mapping:** Token-based textual semantic classification.
* **Student Mental Health Predictor:** Predictive modeling utilizing structured behavioral inputs.
* **Risk Engine:** Real-time generation of priority flags for critical mental stress parameters.

### 💻 Frontend Suite
* **Fast React + Vite Architecture:** Optimized build configs for sub-second hot reloading.
* **Interactive Dashboard:** Beautifully animated telemetry charts and dashboard layout.
* **Cross-Device Responsive UI:** Designed with high contrast visibility modes.

### ⚙️ Backend & API Ecosystem
* **High-Performance Routing:** Modular backend architecture driven by FastAPI.
* **Predictive Endpoints:** Low-latency JSON-based model inference endpoints.
* **Interactive Documentation:** Native swagger spec routing out of the box.

---

## 🛠️ Technologies Used

| Technology | Purpose |
| :--- | :--- |
| **React.js** | Single Page Application Frontend UI Layer |
| **Vite** | Modern Frontend Tooling & Fast Bundling |
| **FastAPI** | High-Performance REST API Routing |
| **Python** | AI Core Infrastructure & Pipeline Logic |
| **Scikit-learn** | Model Compilation & Classic ML Classifiers |
| **Transformers / PyTorch** | Deep Learning Text Processing Environments |
| **Firebase** | Scalable NoSQL Data Persistence Layer |
| **Pandas & NumPy** | Matrix Math & Structural Data Wrangling |
| **Matplotlib & Seaborn** | Static Report Analysis Chart Renderers |

---

## 📂 Project Structure

```text
ai-mental-health-companion/
├── backend/
│   ├── dataset/
│   │   ├── Emotions dataset for NLP/ (test.txt, train.txt, val.txt)
│   │   └── Student Mental health/ (Student Mental health.csv)
│   ├── models/
│   ├── venv/
│   ├── emotion_nlp_model.pkl
│   ├── emotion_vectorizer.pkl
│   ├── main.py
│   ├── train_emotion_nlp.py
│   └── train_predictor.py
├── demo/
│   ├── (Screenshots & Video assets)
│   └── Video Project 1.mp4
├── frontend/
│   ├── public/
│   ├── src/
│   ├── index.html
│   └── package.json
├── notebooks/
│   ├── Journal_Text_Analysis.ipynb
│   └── Student_Mental_Health_Analysis.ipynb
└── report/
    ├── AI Mental Health report.docx
    └── AI Mental Health report.pdf


⚙️ Complete Setup Guide
🔹 Frontend Setup (React + Vite)
1. Dependencies Initialization:

Bash
cd frontend
npm install
2. Modern Vite Compilation Variant (Fallback Setup):

Bash
# Run if manual configuration replication is required
npm create vite@latest . -- --template react
npm install react react-dom
npm install -D vite @vitejs/plugin-react eslint
3. Run Local Frontend Instance:

Bash
npm run dev
🔹 Backend Setup (FastAPI + AI Engine)
1. Virtual Environment Setup:

Bash
cd backend
python -m venv venv
2. Activate Environment:

Windows (PowerShell): .\venv\Scripts\Activate

Linux/Mac: source venv/bin/activate

3. Install Engine Libraries:

Bash
pip install fastapi uvicorn transformers torch scikit-learn pandas numpy joblib imbalanced-learn jupyterlab seaborn matplotlib wordcloud
4. Execute Backend Server:

Bash
uvicorn main:app --reload
🌐 Swagger Interactive API Documentation: Open http://127.0.0.1:8000/docs

🧠 Training & Analytics Pipelines
Train ML Predictor Models
Bash
python train_predictor.py
python train_emotion_nlp.py
Run Experimental Notebooks
Bash
jupyter lab
📸 Project Screenshots
🏠 Dashboard
😊 Detected Emotions
👨‍💻 Developers Information
📊 Insights Logs
📝 Journal Analysis
⚠️ Risk Assessment Profiles
⚙️ Settings & Communication Channels
🎥 Project Demo Video
📹 Watch the live operation breakdown and complete technical video guide here:

👉 AI Mental Health Companion System - Demo Link

👥 Team Members
Noor Malik
Email: noormalik56500@gmail.com

LinkedIn: noormalik56500

Portfolio: noor-malik-portfolio.netlify.app

GitHub: @noormalik33

Ghulam Qadir
Email: gqitspecialist@gmail.com

LinkedIn: ghulam-qadir

Portfolio: ghulamqadir.netlify.app

GitHub: @G-Qadir9988

🌟 Community & Support
CoreIT Tech

📧 Email: coreittech1@gmail.com

▶️ YouTube Channel: @CoreITTech1

📸 Instagram Hub: @coreit.tech

⭐ Future Improvements
💬 Contextual Live AI Chatbot Interactivity.

🎙️ Voice Emotion Frequency Modulation Analysis.

🧠 Automated Dynamic Therapy Suggestion Arrays.

🛡️ Secure OAuth2 State-based User Authentication Engine.

📜 License
This architecture setup is built exclusively for the Artificial Intelligence Lab – Final Semester Project Framework Evaluation. Educational and research restrictions apply.

Special thanks to our supervisor Sir Yasir Ali, our mentors, and the broader open-source machine learning community.

💡 GitHub Repositories Ke Liye Pro-Tips:
Relative Paths Check: App ne ./demo/dashboard.jpeg wagaira ke paths bilkul sahi folder structure ke mutabiq map kiye hain, is liye GitHub par images direct load ho jayengi.

Badges Styling: Page ke header mein standard clean shields (React, FastAPI, Python) add kiye hain jo visibility score barha dete hain.
