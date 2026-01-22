# 🔒 Cloud Diary Vault (v1.0)

A secure, local-first desktop diary application built with Python. It features military-grade encryption (Fernet), a modern GUI (CustomTkinter), and a full CRUD system with password protection.

## ✨ Features
* **Military-Grade Security:** All entries are encrypted using `cryptography` (Fernet) before touching the disk.
* **Authentication Gate:** SHA-256 Hashed Master Password protection on startup.
* **Modern UI:** Dark-mode enabled interface built with `customtkinter`.
* **Search & Filter:** Live search filtering for finding entries instantly.
* **CRUD System:** Create, Read, Update, and Delete diary entries securely.

## 🛠️ Tech Stack
* **Language:** Python 3.12+
* **GUI:** CustomTkinter (Tkinter wrapper)
* **Security:** Fernet (Symmetric Encryption), SHA-256 (Hashing)
* **Storage:** Local Encrypted Flat-files (Migration to AWS S3 planned for v2.0)

## 🚀 Setup & Installation

### Prerequisites
* Python 3.10 or higher
* Linux/Windows/MacOS

### Installation
1.  **Clone the repository**
    ```bash
    git clone [https://github.com/RayyanSameer/Daily-Python-Doodles-.git]
    cd Cloud_Diary_Vault
    ```

2.  **Create a Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **First Run (Security Setup)**
    The app will automatically generate encryption keys and prompt you to set a Master Password on the first launch.
    ```bash
    python3 gui.py
    ```

## 📂 Project Structure
```text
Cloud_Diary_Vault/
│
├── data/                  # Encrypted diary entries (Auto-generated)
├── auth.hash              # SHA-256 Hashed Master Password
├── secret.key             # Fernet Encryption Key (DO NOT SHARE)
├── gui.py                 # Frontend: CustomTkinter Interface
├── manager.py             # Backend: Encryption, File I/O, Auth Logic
├── requirements.txt       # Dependency list
└── README.md              # Documentation


🗺️ Roadmap (DevOps Transformation)

    [x] v1.0: Secure Local Desktop App (Completed)

    [ ] v1.1: Containerization with Docker

    [ ] v1.2: CI/CD Pipeline via GitHub Actions (Linting & Testing)

    [ ] v2.0: Cloud Storage Integration (AWS S3)

🛡️ Security Note

This application stores the secret.key locally. If you lose this key, all data is permanently lost. There is no recovery backdoor.