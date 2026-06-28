# Hackathon Management System

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org) [![Flask](https://img.shields.io/badge/Backend-Flask-green)](https://flask.palletsprojects.com) [![SQLite](https://img.shields.io/badge/DB-SQLite-blue)](https://www.sqlite.org)

The Hackathon Management System is a comprehensive, enterprise-grade web platform specifically engineered to streamline the organization, management, and execution of large-scale hackathons, competitive coding events, and professional tender bidding processes. Built on a highly robust and scalable Flask (Python) backend paired with a lightweight SQLite database (which can be seamlessly migrated to PostgreSQL for enterprise deployments), this system provides event organizers with an intuitive, end-to-end administrative console.

Organizers are equipped with a powerful suite of tools to seamlessly handle mass participant registration, dynamic team formation workflows, and secure document submissions within isolated collaborative workspaces. To address the complexities of modern competitive events, the platform integrates state-of-the-art AI-driven auditing services natively into the submission pipeline. By utilizing sophisticated local Isolation Forest machine learning models, the system autonomously analyzes submission patterns to detect anomalies, plagiarism, or irregular tender bids in real-time.

Furthermore, integrated Natural Language Processing (NLP) summarization algorithms automatically parse lengthy project proposals and technical documents, providing judges and reviewers with concise, digestible executive summaries. This significantly reduces manual evaluation time and ensures a fair, transparent, and highly efficient judging process. With robust role-based access control (RBAC), real-time notification systems, and comprehensive audit logs, the Hackathon Management System delivers a technologically advanced, secure environment tailored for academic institutions, corporate innovation labs, and government tech initiatives.

## 🚀 Key Technologies
- **Web Server**: Flask (Python)
- **Database**: SQLite3
- **AI Services**: Local Isolation Forest models (anomaly detection) and NLP summarizers

## 📦 Getting Started & Installation
```bash
# Install Python dependencies
pip install -r requirements.txt

# Launch the server
python app.py
```

## 📜 License
This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.
