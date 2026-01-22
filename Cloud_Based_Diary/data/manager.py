import os
import datetime
import hashlib
from cryptography.fernet import Fernet

# --- Configuration ---
DATA_DIR = "data"
KEY_FILE = "secret.key"
AUTH_FILE = "auth.hash"

# Ensure data storage exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# --- Security Initialization ---
def _load_cipher():
    """Loads the encryption key and initializes the Fernet cipher."""
    if not os.path.exists(KEY_FILE):
        print(f"CRITICAL: '{KEY_FILE}' not found. Please run setup.")
        return None
    try:
        key = open(KEY_FILE, "rb").read()
        return Fernet(key)
    except Exception as e:
        print(f"CRITICAL: Failed to load key. {e}")
        return None

cipher = _load_cipher()


# --- File Operations ---

def list_entries():
    """Returns a list of all files in the data directory."""
    if not os.path.exists(DATA_DIR):
        return []
    return [f for f in os.listdir(DATA_DIR) if f.endswith(".txt")]

def add_entry(title, mood, text):
    """Creates a new encrypted entry."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Sanitize filename
    if not title:
        filename = f"{timestamp}.txt"
    else:
        clean_title = title.replace(" ", "_")
        filename = f"{clean_title}.txt"

    # Prepare content
    raw_content = f"Mood: {mood}\n\n{text}"
    return save_entry(filename, raw_content)

def read_entry(filename):
    """Reads and decrypts a specific file."""
    filepath = os.path.join(DATA_DIR, filename)
    
    if not os.path.exists(filepath):
        return None
    
    if not cipher:
        return "Error: Encryption system not initialized."

    try:
        with open(filepath, "rb") as f:
            encrypted_data = f.read()
            
        decrypted_bytes = cipher.decrypt(encrypted_data)
        return decrypted_bytes.decode()
        
    except Exception:
        return " Error: Decryption failed. Key may differ or file is corrupt."

def save_entry(filename, text):
    """Encrypts and overwrites the specified file."""
    filepath = os.path.join(DATA_DIR, filename)
    
    if not cipher:
        return False

    try:
        encrypted_data = cipher.encrypt(text.encode())
        with open(filepath, "wb") as f:
            f.write(encrypted_data)
        return True
    except OSError:
        return False

def delete_entry(filename):
    """Permanently deletes a file."""
    filepath = os.path.join(DATA_DIR, filename)
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
            return True
    except OSError:
        return False


# --- Authentication System ---

def is_password_set():
    """Checks if the master password hash exists."""
    return os.path.exists(AUTH_FILE)

def set_master_password(password):
    """Hashes and stores the new master password."""
    hashed = hashlib.sha256(password.encode()).hexdigest()
    with open(AUTH_FILE, "w") as f:
        f.write(hashed)

def verify_password(password):
    """Verifies the input password against the stored hash."""
    if not is_password_set():
        return False

    try:
        with open(AUTH_FILE, "r") as f:
            stored_hash = f.read().strip()
            
        input_hash = hashlib.sha256(password.encode()).hexdigest()
        return stored_hash == input_hash
    except Exception:
        return False