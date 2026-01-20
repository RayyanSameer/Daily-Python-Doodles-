

# 🕵️ AWS Spy Bot (API Monitor)

A Python-based automation pipeline that fetches user data from a public API, generates a local report, and securely archives it to an AWS S3 Bucket. The application is fully containerized using Docker for consistent deployment across any environment (Local Laptop, AWS EC2, etc.).

## 🚀 Features

* **Data Extraction:** Fetches JSON user data from `jsonplaceholder.typicode.com`.
* **Report Generation:** Parses data and compiles a readable `user_report.txt`.
* **Cloud Archiving:** Automatically creates a unique S3 Bucket (if missing) and uploads the report.
* **Containerized:** Runs in an isolated Docker container with all dependencies included.
* **Secure:** Uses AWS credentials via volume mounting or environment variables (no hardcoded keys).

## 🛠️ Tech Stack

* **Language:** Python 3.9
* **Cloud:** AWS S3 (via Boto3 SDK)
* **Container:** Docker
* **Version Control:** Git

## 📂 Project Structure

```text
api_monitor/
├── Dockerfile          # Blueprint for the container
├── spy.py              # Script 1: Fetches data & writes report
├── aws_upload.py       # Script 2: Uploads report to S3
├── user_report.txt     # Output file (Generated automatically)
└── README.md           # Documentation

📋 Prerequisites

    Docker installed on your machine.

    AWS Account with an Access Key & Secret Key.

    AWS Permissions: The user/role must have s3:CreateBucket and s3:PutObject permissions.

⚙️ Setup & Installation
1. Clone the Repository
Bash

git clone [https://github.com/YOUR_USERNAME/Daily-Python-Doodles.git](https://github.com/YOUR_USERNAME/Daily-Python-Doodles.git)
cd Daily-Python-Doodles/api_monitor

2. Configure AWS Credentials

Ensure you have your AWS credentials set up locally.

    Linux/Mac: ~/.aws/credentials

    Windows: %USERPROFILE%\.aws\credentials

If you don't have this file, create it:
Ini, TOML

[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
region = ap-south-1

🐳 Running with Docker (Recommended)
1. Build the Image

Build the Docker container from the blueprint.
Bash

docker build -t spy-bot-v2 .

2. Run the Pipeline

We run the container and mount your local AWS credentials so the bot can access S3 securely.

Linux / Mac / EC2:
Bash

docker run --rm -v ~/.aws:/root/.aws spy-bot-v2 sh -c "python spy.py && python aws_upload.py"

Windows (PowerShell):
PowerShell

docker run --rm -v $HOME\.aws:/root/.aws spy-bot-v2 sh -c "python spy.py && python aws_upload.py"

💻 Running Locally (Without Docker)

If you want to test the scripts directly on your machine:

    Create a Virtual Environment:
    Bash

    python -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate

    Install Dependencies:
    Bash

    pip install requests boto3

    Run the Scripts:
    Bash

    python spy.py          # Generates user_report.txt
    python aws_upload.py   # Uploads to S3

⚠️ Security Note

    Never commit your .env or .pem files to GitHub.

    This project uses a .gitignore file to prevent accidental leaks of sensitive data.

    If running on EC2, it is recommended to use IAM Roles instead of access keys for better security.