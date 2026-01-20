import sys
import manager

def handle_add():
    # 1. Ask User
    print("\n--- NEW ENTRY ---")
    title = input("Title (Press Enter for Auto): ").strip()
    mood = input("Mood: ")
    text = input("Text: ")

    # 2. Call Manager
    result = manager.add_entry(title, mood, text)

    # 3. Show Result
    if result:
        print(f"✅ Saved as: {result}")
    else:
        print("❌ Error saving file.")

def handle_list():
    print("\n[Your Vault]")
    files = manager.list_entries()
    
    if not files:
        print("No entries found.")
        return

    for f in files:
        print(f" 📄 {f}")

def handle_read():
    # 1. Ask which file
    filename = input("Enter filename to read (e.g., My_Day.txt): ")
    
    # 2. Call Manager
    content = manager.read_entry(filename)
    
    # 3. Show Result
    if content:
        print("\n" + "="*20)
        print(content)
        print("="*20 + "\n")
    else:
        print("❌ File not found.")

def run_menu():
    # THE INFINITE LOOP
    while True:
        print("\n--- CLOUD DIARY v1 ---")
        print("1. Add Entry")
        print("2. List Entries")
        print("3. Read Entry")
        print("4. Exit")
        
        choice = input("Select > ")
        
        if choice == "1":
            handle_add()
        elif choice == "2":
            handle_list()
        elif choice == "3":
            handle_read()
        elif choice == "4":
            print("Bye.")
            sys.exit()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    run_menu()