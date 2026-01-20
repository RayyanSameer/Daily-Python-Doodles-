import os
import datetime
from cryptography.fernet import Fernet

DATA_DIR = "data"
KEY_FILE = "secret.key"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)



def load_key():
    return open(KEY_FILE, "rb").read()
key = load_key()
cipher = Fernet(key)

def add_entry(title, mood, text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
   
    if not title:
        filename = f"{timestamp}.txt"
    else:
     
        clean_title = title.replace(" ", "_")
        filename = f"{clean_title}.txt"

    
    filepath = os.path.join(DATA_DIR, filename)
    
  
    try:
        with open(filepath, "w") as f:
           
            f.write(f"Mood: {mood}\n\n{text}")
        return filename
    except OSError:
        return None

def list_entries():
   
    return os.listdir(DATA_DIR)

def read_entry(filename):
    filepath = os.path.join(DATA_DIR, filename)
    
   
    if not os.path.exists(filepath):
        return None  
    
    # 2. Open and Read
    try:
        with open(filepath, "r") as f:
            content = f.read()
        return content
    except OSError:
        return None

def delete_entry(filename):
    filepath = os.path.join(DATA_DIR, filename)
    
    if not os.path.exists(filepath):
        return False
        
    try:
        os.remove(filepath)
        return True
    except OSError:
        return False


def update_entry(filename, new_text):
    filepath = os.path.join(DATA_DIR,filename)

    if not os.path.exists(filepath):
        return False
    
    try:
        with open(filepath,"a") as f:
            f.write("\n\n" + "-"*10 + " [UPDATE] " + "-"*10 + "\n")
            f.write(new_text)
        return True
    except OSError:
        return False    

    
# --- MANUAL TEST ZONE ---
if __name__ == "__main__":
    print("🤖 Testing Manager Logic...")
    
    # 1. Test Adding
    print("\n1. Creating Entry...")
    file_created = add_entry("Commute Thoughts", "Tired", "Traffic was terrible.")
    print(f"   -> Result: {file_created}")

    # 2. Test Reading
    print("\n2. Reading Entry...")
    content = read_entry(file_created)
    print(f"   -> Content Read: {content}")
    
    # 3. Test Deleting
    print("\n3. Deleting Entry...")
    deleted = delete_entry(file_created)
    print(f"   -> Deleted: {deleted}")    