import manager
import sys

#Menu
while True:
    print("CLI Cloud Diary")
    print("1. Add Entry ")
    print("2.Delete Entry")
    print("3.List Entry")
    print("4.Exit")

    choice = int(input("Enter your choice : "))
    if choice == "1:
        title = str(input("Enter title: "))
        mood = str(input("How are you feeling today? : "))
        text = str(input("Your entry here"))

        saved_file = [title,mood,text]
        if saved_file in DATA_DIR:
            print("Success")
        else:
            print("Failed")
    elif choice ==  2:
        all_entries =  manager.list_entries()
        for i in all_entries:
            print(i)
    elif choice == 3:
        #Added ;ater on
        
    elif choice == 4:
        print("Bye")
        sys.exit()
    else:
        print("Invalid Command")


