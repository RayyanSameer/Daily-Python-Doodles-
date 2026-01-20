#  CLI Cloud Diary (Phase 1)

A robust, local-first command-line diary application built in Python. 
Designed with a "Three-Tier Architecture" to separate user interface from business logic.

##  Features

* **Create Entries:** Auto-timestamps entries and sanitizes filenames (spaces -> underscores).
* **Read Entries:** View your past journal entries directly in the terminal.
* **List Vault:** See all stored files in your local data vault.
* **Delete Entries:** Safely remove files with existence checks.
* **Crash-Proof:** Handles missing files and IO errors gracefully.

##  Architecture

This project follows a strict **Separation of Concerns**:

* **`main.py` (The Interface):** * Acts as the "Front Desk." 
    * Handles all user inputs (`input`) and displays (`print`).
    * **Rule:** Never touches the hard drive directly.
* **`manager.py` (The Engine):** * Acts as the "Back Office."
    * Handles file I/O, path management, and data validation.
    * **Rule:** Never interacts with the user (no `print` or `input`).
* **`data/` (The Vault):**
    * A dedicated directory where all text files are stored.

##  usage

1.  **Run the application:**
    ```bash
    python main.py
    ```

2.  **Follow the menu:**
    ```text
    --- CLOUD DIARY v1 ---
    1. Add Entry
    2. List Entries
    3. Read Entry
    4. Delete Entry
    5. Exit
    ```

##  Roadmap (Phase 2 & 3)

* [ ] **Encryption:** Implement Fernet symmetric encryption to lock files.
* [ ] **Cloud Sync:** Integrate AWS S3 (`boto3`) for off-site backups.
* [ ] **GUI:** Build a `Tkinter` front-end (replacing `main.py`).

##  Author

Built by Rayyan
 January 2026*