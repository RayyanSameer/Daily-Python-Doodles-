#  Cloud Diary Vault (v2.0)

A secure, **Hybrid-Cloud** diary application built with a Microservices architecture. It features a headless REST API running on **AWS EC2**, a local **Streamlit** Web UI, and military-grade encryption (Fernet) for data security.

##  Features
* **Hybrid Sync:** Write entries on your local machine, securely stored on an AWS Cloud Server in Mumbai.
* **Military-Grade Security:** All entries are encrypted using cryptography (Fernet) before being saved to the server disk.
* **Headless Microservice:** The backend runs as a pure Dockerized API (FastAPI) on EC2.
* **Modern Web UI:** A beautiful, browser-based interface built with Streamlit (no HTML/CSS needed).
* **Authentication Gate:** SHA-256 Hashed Master Password protection for every save operation.

##  Tech Stack
* **Language:** Python 3.10+
* **Frontend:** Streamlit (Web UI)
* **Backend:** FastAPI (REST API)
* **Cloud:** AWS EC2 (Ubuntu Server 24.04 LTS)
* **Containerization:** Docker & Docker Compose
* **Security:** Fernet (Symmetric Encryption), SHA-256 (Hashing)

##  Setup & Installation

### Prerequisites
* Python 3.10+
* Docker Desktop (for local backend testing)
* An active AWS EC2 Instance (for production)

### 1. Backend Deployment (AWS Server)
SSH into your EC2 instance and run the container:

```bash
# Connect to your AWS Server
ssh -i "your-key.pem" ubuntu@<YOUR_EC2_IP>

# Clone & Launch
git clone [https://github.com/RayyanSameer/Cloud-Notes-Vault.git](https://github.com/RayyanSameer/Cloud-Notes-Vault.git)
cd Cloud-Notes-Vault
docker compose up --build -d

2. Frontend Usage (Local Laptop)

Run the interface on your local machine to connect to the cloud.
Bash

# Install Dependencies
pip install -r requirements.txt

# Launch the Web App
streamlit run frontend.py

 Project Structure
Plaintext

Cloud_Diary_Vault/
│
├── storage/               # Encrypted diary entries (On Server)
├── auth.hash              # SHA-256 Hashed Master Password
├── secret.key             # Fernet Encryption Key (DO NOT SHARE)
├── api.py                 # Backend: FastAPI REST Service
├── frontend.py            # Frontend: Streamlit Web Interface
├── manager.py             # Logic: Encryption & File Handling
├── Dockerfile             # Container Instructions
├── docker-compose.yml     # Orchestration Config
└── requirements.txt       # Dependency list

Roadmap (DevOps Transformation)

    [x] v1.0: Secure Local Desktop App (Tkinter)

    [x] v2.0: Hybrid Cloud Deployment (AWS EC2 + Docker)

    [ ] v3.0: Full Cloud Native (AWS S3 Storage + Cognito Auth)

    [ ] v4.0: Kubernetes Cluster Deployment (EKS)

 Security Note

This application relies on secret.key. If you lose this key, all data on the server is permanently unreadable. Backup your key securely.