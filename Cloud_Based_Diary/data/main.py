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
        print(f" Saved as: {result}")
    else:
        print(" Error saving file.")
        input("\nPress Enter to continue...")

def handle_list():
    print("\n[Your Vault]")
    files = manager.list_entries()
    
    if not files:
        print("No entries found.")
        return

    for f in files:
        print(f"  {f}")

    input("\nPress Enter to continue...")      

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
        print(" File not found.")
    input("\nPress Enter to continue...")    

def handle_update():
    print("\n--- Update Entry ---")
    filename = input("Enter filename to update: ")
    new_text = input("Add your new text: ")
    
    if manager.update_entry(filename, new_text):
        print(" Entry updated successfully.")
    else:
        print(" File not found.")  
        input("\nPress Enter to continue...")  

def handle_delete():
    print("\n---Delete Entry---")
    filename = input("Enter entry to be deleted : ")

    if manager.delete_entry(filename):
        print("Entry")
    else:
        print("File not found")    
def run_menu():
    while True:
        print("\n--- CLOUD DIARY v1 ---")
        print("1. Add Entry")
        print("2. List Entries")
        print("3. Read Entry")
        print("4. Delete Entry")
        print("5. Update Entry")   
        print("6. Exit")
        
        choice = input("Select > ")
        
        if choice == "1":
            handle_add()
        elif choice == "2":
            handle_list()
        elif choice == "3":
            handle_read()
        elif choice == "4":     # Corrected: Now points to Delete
            handle_delete()
        elif choice == "5":     # Corrected: Now points to Update
            handle_update()
        elif choice == "6":     # Corrected: Now points to Exit
            print("Bye!")
            sys.exit()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    run_menu()            