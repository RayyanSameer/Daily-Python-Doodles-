import os
import datetime
from cryptography.fernet import Fernet

DATA_DIR = "data"
KEY_FILE = "secret.key"

# Ensure data directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# --- SECURITY SETUP ---
def load_key():
    return open(KEY_FILE, "rb").read()

try:
    key = load_key()
    cipher = Fernet(key)
except FileNotFoundError:
    print(" CRITICAL ERROR: 'secret.key' not found! Run setup_security.py first.")
    cipher = None
# ----------------------

def add_entry(title, mood, text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    if not title:
        filename = f"{timestamp}.txt"
    else:
        clean_title = title.replace(" ", "_")
        filename = f"{clean_title}.txt"

    filepath = os.path.join(DATA_DIR, filename)
    
    # 1. Prepare Content
    raw_content = f"Mood: {mood}\n\n{text}"
    
    # 2. Encrypt
    if cipher:
        encrypted_data = cipher.encrypt(raw_content.encode())
    else:
        return None

    try:
        # 3. Write Bytes
        with open(filepath, "wb") as f:
            f.write(encrypted_data)
        return filename
    except OSError:
        return None

def list_entries():
    if not os.path.exists(DATA_DIR):
        return []
    return os.listdir(DATA_DIR)

def read_entry(filename):
    filepath = os.path.join(DATA_DIR, filename)
    
    if not os.path.exists(filepath):
        return None
    
    try:
        # 1. READ 
        with open(filepath, "rb") as f:
            encrypted_data = f.read()
            
        # 2. DECRYPT 
        decrypted_bytes = cipher.decrypt(encrypted_data)
        
        # 3. DECODE 
        return decrypted_bytes.decode()
        
    except Exception as e:
        return f" Error: Could not decrypt. ({e})"

def update_entry(filename, new_text):
    filepath = os.path.join(DATA_DIR, filename)
    
    if not os.path.exists(filepath):
        return False
    
    try:
        # 1. Read & Decrypt Old Data
        with open(filepath, "rb") as f:
            encrypted_data = f.read()
        
        current_content = cipher.decrypt(encrypted_data).decode()
        
        # 2. Add New Text
        updated_content = current_content + "\n\n" + "-"*10 + " [UPDATE] " + "-"*10 + "\n" + new_text
        
        # 3. Encrypt Everything
        new_encrypted_data = cipher.encrypt(updated_content.encode())
        
        # 4. Overwrite File
        with open(filepath, "wb") as f:
            f.write(new_encrypted_data)
            
        return True
    except Exception:
        return False

def delete_entry(filename):
    filepath = os.path.join(DATA_DIR, filename)
    if not os.path.exists(filepath):
        return False
    try:
        os.remove(filepath)
        return True
    except OSError:
        return False