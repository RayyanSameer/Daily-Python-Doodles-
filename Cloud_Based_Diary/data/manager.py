import os 
import datetime

DATA_DIR = "data" 

# Ensure vault exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def add_entry(title, mood, text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # --- LOGIC FIX: One filename variable ---
    if not title:
        filename = f"{timestamp}.txt"
    else:
        # Clean the title and add extension
        clean_title = title.replace(" ", "_")
        filename = f"{clean_title}.txt"

    filepath = os.path.join(DATA_DIR, filename) 

    try:
        with open(filepath, "w") as file:
            # We write clean metadata inside the file
            file.write(f"Title: {title if title else 'Untitled'}\n")
            file.write(f"Date: {timestamp}\n")
            file.write(f"Mood: {mood}\n")
            file.write("-" * 20 + "\n\n")
            file.write(text)
        return filename
        
    except OSError as e:
        return None

def list_entries():
    # Returns a LIST of filenames
    if not os.path.exists(DATA_DIR):
        return []
    return os.listdir(DATA_DIR)

def read_entry(filename):
    # 1. Build path
    filepath = os.path.join(DATA_DIR, filename)
    
    # 2. Check existence
    if not os.path.exists(filepath):
        return None # Signal failure
    
    # 3. Read and Return
    try:
        with open(filepath, "r") as file:
            return file.read() # Return the text to Main
    except Exception:
        return None