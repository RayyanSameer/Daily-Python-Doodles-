import csv 
import os
from datetime import datetime

FILENAME = "diary.csv"

def create_entry(entries, text):
    
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "text": text
    }
    entries.append(entry)

def load_entries():
    entries = []
    if not os.path.exists(FILENAME):
        return entries
    
    try:
        with open(FILENAME, "r", newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                entries.append(row)
    except Exception as e:
        print(f"Error loading file: {e}")
    return entries

def save_all_entries(entries):
    with open(FILENAME, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["date", "text"])
        writer.writeheader()
        writer.writerows(entries)

def update_entry(entries, index, new_text):
    if 0 <= index < len(entries):
        entries[index]["text"] = new_text
        save_all_entries(entries)
        print("Entry updated.")
    else:
        print("Error: Invalid entry number.")

def delete_entry(entries, index):
    if 0 <= index < len(entries):
        removed = entries.pop(index)
        save_all_entries(entries)
        print(f"Deleted entry from {removed['date']}.")
    else:
        print("Error: Invalid entry number.")

def list_entries(entries):
    if not entries:
        print("\n--- Your diary is empty ---")
        return
    print("\n--- Diary Entries ---")
    for i, entry in enumerate(entries):
        print(f"[{i}] {entry['date']} — {entry['text']}")

# Main Loop
if __name__ == "__main__":
    entries = load_entries()
    
    while True:
        print("\n[1] Add  [2] List  [3] Update  [4] Delete  [5] Quit")
        choice = input("Choice: ").strip()

        try:
            if choice == "1":
                text = input("How are you feeling today? ")
                create_entry(entries, text)
                save_all_entries(entries)
                
            elif choice == "2":
                list_entries(entries)

            elif choice == "3":
                list_entries(entries)
                idx = int(input("Which index to update? "))
                new_text = input("Enter new text: ")
                update_entry(entries, idx, new_text)

            elif choice == "4":
                list_entries(entries)
                idx = int(input("Which index to delete? "))
                confirm = input(f"Delete entry [{idx}]? (y/n): ").strip().lower()
                if confirm == "y":
                    delete_entry(entries, idx)
                else:
                    print("Cancelled.")

            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")
        
        except ValueError:
            print("Error: Please enter a valid number for the index.")