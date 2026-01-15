# Simple Menu Driven Contact Manager

contacts = {}

while True:
    print("\nWelcome to this simple contact manager!")
    print("What would you like to do?")
    print("(1) Add contact")
    print("(2) Remove contact")
    print("(3) Search contact")
    print("(4) Update contact")
    print("(5) Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        # Add contact
        n = int(input("How many contacts would you like to add?: "))
        for _ in range(n):
            name = input("Enter Name: ")
            value = input("Enter Value (e.g., phone or email): ")
            contacts[name] = value
        print("Contacts added successfully!")

    elif choice == '2':
        # Remove contact
        target = input("Who would you like to remove?: ")
        if target in contacts:
            del contacts[target]
            print(f"Contact '{target}' removed.")
        else:
            print("Contact not found.")

    elif choice == '3':
        # Search contact
        to_search = input("Enter name to search: ")
        if to_search in contacts:
            print(f"Found: {to_search} → {contacts[to_search]}")
        else:
            print("Contact not found.")

    elif choice == '4':
        # Update contact
        to_update = input("Enter name to update: ")
        if to_update in contacts:
            new_value = input("Enter new value: ")
            contacts[to_update] = new_value
            print(f"Contact '{to_update}' updated.")
        else:
            print("Contact not found.")

    elif choice == '5':
        # Exit
        print("Bye!")
        break

    else:
        print("Enter a valid number.")
