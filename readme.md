# Hackathon Management System

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org)
[![Flask](https://img.shields.io/badge/Backend-Flask-green)](https://flask.palletsprojects.com)
[![SQLite](https://img.shields.io/badge/DB-SQLite-blue)](https://www.sqlite.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

The Hackathon Management System is a comprehensive, enterprise-grade web platform specifically engineered to streamline the organization, management, and execution of large-scale hackathons, competitive coding events, and professional tender bidding processes. Built on a highly robust and scalable Flask (Python) backend paired with a lightweight SQLite database (which can be seamlessly migrated to PostgreSQL for enterprise deployments), this system provides event organizers with an intuitive, end-to-end administrative console.

Organizers are equipped with a powerful suite of tools to seamlessly handle mass participant registration, dynamic team formation workflows, and secure document submissions within isolated collaborative workspaces. To address the complexities of modern competitive events, the platform integrates state-of-the-art AI-driven auditing services natively into the submission pipeline. By utilizing sophisticated local Isolation Forest machine learning models, the system autonomously analyzes submission patterns to detect anomalies, plagiarism, or irregular tender bids in real-time.

Furthermore, integrated Natural Language Processing (NLP) summarization algorithms automatically parse lengthy project proposals and technical documents, providing judges and reviewers with concise, digestible executive summaries. This significantly reduces manual evaluation time and ensures a fair, transparent, and highly efficient judging process. With robust role-based access control (RBAC), real-time notification systems, and comprehensive audit logs, the Hackathon Management System delivers a technologically advanced, secure environment tailored for academic institutions, corporate innovation labs, and government tech initiatives.

---

## ✨ Features

- **🚀 Collaborative Workspaces** — Dedicated rooms and dashboards for team members to collaborate on submissions.
- **💼 Bid & Tender Management** — Structuring and submission system for formal hackathon project tenders.
- **🧠 Anomaly Detection (AI)** — Machine learning pipeline using Isolation Forest to audit bids and identify collusive or plagiarized submissions.
- **📄 NLP Summarization** — Automatic text processing of uploaded project descriptions to extract key features and summaries.
- **💬 System Assistant** — Context-aware AI chatbot interface providing immediate help to participants on rules and guides.

### 📊 Backend Core Services Breakdown

| Service Module | File Path | Algorithm / Technology | Primary Purpose |
| :--- | :--- | :--- | :--- |
| **ML Auditing** | `services/ml_service.py` | Isolation Forest | Analyzes bids features for outliers, spikes, and potential collusive behavior. |
| **NLP Processing** | `services/nlp_service.py` | TF-IDF / Summarizers | Generates automated summaries and extracts key keywords from files. |
| **System Chatbot** | `services/chatbot_service.py` | Local AI Assistant | Answers queries on event guidelines and platform documentation. |
| **Data Handler** | `services/database_service.py` | SQLite Wrapper | Manages connection states, transactions, and session persistence. |
| **File Processor** | `services/file_handler.py` | Local Secure File I/O | Standardizes document uploads and performs input validation. |

---

## 🏗️ Project Architecture

```
hackathon-management-system/
├── app.py                     # Main Flask Application Router
├── init_system.py             # System Bootstrap & Data Seeding
├── actms.db                   # Local SQLite Database file
├── requirements.txt           # Pip dependency file
├── pyproject.toml             # Python packaging config
├── uv.lock                    # Fast python package manager lockfile
├── models/                    # Serialized Machine Learning models
│   ├── isolation_forest.pkl   # Pre-trained Isolation Forest classifier
│   └── scaler.pkl             # StandardScaler for feature scaling
├── services/                  # Business Logic & Backend Services
│   ├── chatbot_service.py     # AI Chatbot service
│   ├── database_service.py    # DB transaction management
│   ├── file_handler.py        # Secure file uploads
│   ├── ml_service.py          # Isolation Forest scoring
│   └── nlp_service.py         # Summary generation
├── static/                    # Frontend Client Assets
│   ├── icons/                 # SVG graphics and assets
│   ├── js/                    # Client-side JavaScript modules
│   └── styles/                # CSS layout and themes
└── templates/                 # Server-Side Rendered Templates
    ├── dashboard.html         # Main user home dashboard
    ├── bids.html              # Bidding submission console
    ├── ai_analysis.html       # AI-audit analytics panel
    ├── chat.html              # Interactive helpdesk chatbot
    └── base.html              # Core layout master template
```

---

## 🛠️ Tech Stack

| Layer | Technology | Detail |
| :--- | :--- | :--- |
| **Web Server** | Flask (Python) | Lightweight WSGI micro-framework |
| **Database** | SQLite3 | Local storage with relational schemas |
| **Machine Learning** | Scikit-Learn | Isolation Forest model for anomaly detection |
| **NLP** | NLTK / Text Summarization | Summary extraction & keyword tokenization |
| **Styling & CSS** | Custom CSS | Clean grids, animations, and dark/light palettes |
| **Client Interaction**| Vanilla JS | Dynamic async updates via Fetch API |
| **Environment** | UV / Pip | Fast dependency resolver and runtime controller |

---

## 🚀 Getting Started & Installation

### Prerequisites
- **Python 3.11+**
- **pip** or **uv** (Recommended)

### Installation & Initialization

Using **uv** (Recommended):
```bash
# Clone the repository
git clone https://github.com/vemana4/hackathon-management-system.git
cd hackathon-management-system

# Sync dependencies and create venv
uv sync

# Bootstrap the database and generate initial models
uv run python init_system.py

# Launch the Flask server
uv run python app.py
```

Using standard **pip**:
```bash
# Clone the repository
git clone https://github.com/vemana4/hackathon-management-system.git
cd hackathon-management-system

# Create virtual environment and install packages
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Bootstrap the database and generate initial models
python init_system.py

# Launch the Flask server
python app.py
```

---

## 📜 License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Built with ❤️ by <a href="https://github.com/vemana4">Vemana Hemanth Babu</a>
</p>
