#Simple Text Based Contact Manager 

contacts = []  #List to store contact dictionaries
contact_names = set()

while True:
    print("Welcome to contacts!")
    print("Press 1 to add a new contact")
    print("Press 2 to delete a contact")
    print("Press 3 to update a contact")
    print("Press 4 to search a contact")
    print("Press 5 to quit")

    choice = input("Enter your choice 1/2/3/4/5: ")
    if choice == 1: 
        contact_name = input("Enter name : ")
        contact_number = input("Enter number: ")
        for item in contacts:
            if len(contacts) == 0:
                contacts.append()
                


   




    



