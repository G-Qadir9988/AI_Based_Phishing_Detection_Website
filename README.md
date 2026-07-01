# 🛡️ Phishing Shield: AI-Based Phishing Website Detection Tool

[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Core-Python%20v3.13-3776AB?logo=python)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/ML%20Core-Scikit--Learn-F7931E?logo=scikit-learn)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-Educational%20Use-green)](#-license)

### 🚀 AI-Powered Cyber Threat Intelligence & Phishing Link Detection Platform

A professional cybersecurity auditing tool designed to inspect target URLs, extract deep forensic feature vectors, calculate Shannon entropy/risk parameters, and deliver instant classification verdicts using a Supervised Random Forest Classifier and an interactive, high-contrast Streamlit interface.

---

## 👨‍💻 Developed By
* **Noor Malik** & **Ghulam Qadir**
* 🎓 *Cyber Security Lab – Final Semester Project*
* 🏫 *Air University, Islamabad*

---

## 📌 Project Description
The **AI-Based Phishing Website Detection Tool** is a modern intelligent system engineered to intercept social engineering and brand spoofing attack vectors before deployment. 

The system operates via a dual-layer defensive approach:
1. **Rule-Based Heuristic Parser:** Client-side runtime validation of brand spoofing indicators, token entropy, domain obfuscation patterns, and transport layer security (HTTPS).
2. **Supervised Machine Learning Core:** Backend processing utilizing an optimized Random Forest Ensemble Model trained on extensive datasets to detect zero-day phishing infrastructure.

---

## ✨ Key Features

### 🧠 AI & Data Science Features
* **Random Forest Classifier Core:** High-precision array tree classification running on `phishing_model_professional.pkl`.
* **Heuristic Feature Breakdown:** Instant tabular dissection of URL parameters (Brand impersonation checks for PayPal, Google, Binance, etc.).
* **Smart Risk Engine:** Real-time generation of weighted priority safety metrics based on suspicious tokens and red flags.

### 💻 Frontend Suite Features
* **Dynamic Theme Control:** Completely responsive architecture adapting instantly to high-contrast **Light Mode** and **Dark Mode** user choices.
* **Streamlit Pipeline:** Fast and responsive text rendering layers engineered to solve "white-on-white" text visibility bugs.
* **Session State Log Logic:** Complete session tracking with an integrated Undo option to reverse previous scans.

### ⚙️ Engine Operations & Controls
* **Live Telemetry Specs:** Simulated server health counters tracking blocked packets and active firewall states.
* **Log Purging & Exports:** Interactive logging table providing one-click tabular actions to download history arrays or wipe caches.

---

## 🛠️ Technologies Used

| Technology | Purpose |
| :--- | :--- |
| **Streamlit** | Unified Frontend Engine & Interactive Dashboard Layout |
| **Python** | System Core Backend Automation & Algorithmic Computations |
| **Scikit-learn** | Random Forest Training Pipelines & Model Tuning |
| **Pandas** | Tabular Matrix Configurations & Data Wrangling |
| **NumPy** | High-Performance Array Mathematics |
| **Joblib** | Model Serialization and Binary Serialization Deployment |
| **Hashlib** | MD5 Generation for Unique Investigation Identifier Tags |

---

## 📂 Project Structure

```text
AI-Based-Phishing-Website-Detection-Tool/
├── backend/
│   ├── dataset/
│   │   └── Phishing_Legitimate_full.csv
│   ├── models/
│   ├── venv/
│   ├── app.py
│   ├── phishing_model_professional.pkl
│   └── train.py
├── demo/
│   ├── .gitkeep
│   ├── dashboard.jpeg
│   ├── detected_emotions.jpeg
│   ├── developers_info.jpeg
│   ├── insights_logs.jpeg
│   ├── journal_analysis.jpeg
│   ├── risk_assessment_profile_1.jpeg
│   ├── risk_assessment_profile_2.jpeg
│   ├── settings.jpeg
│   ├── tech_community_and_content_channels.jpeg
│   ├── video demo link.txt
│   └── Video Project 1.mp4
├── report/
│   ├── .gitkeep
│   ├── Phishing Detection Report.docx
│   └── Phishing Detection Report.pdf
├── .gitattributes
├── .gitignore
├── LICENSE
└── README.md

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

