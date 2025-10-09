#Simple text based to do , to reinforce lists 

tasks = [] #input tasks 
count = 0
max_tasks = 100

#Menu


                  
while True:
    #Menu

    user_choice = int(input("Would you like to do:"))
    print("1. Add Tasks")
    print("2. Delete Tasks")
    print("3. Mark as done")
    print("4. Show Tasks")
    print("0. Quit")

    if user_choice == 1: #Add Tasks
        num = int(input("How many things will you do today? : "))
        for i in range(num):
            task = input(f"Enter task {i + 1}: ")
            tasks.append({"task": task, "done": False})

            #Delete Tasks
    elif user_choice == 2:
        task_number = int(input("Enter task  number to delete: "))
        if 0<= task_number< len(tasks):
            removed = tasks.pop(index)
            print(f"Task '{removed['task']}' deleted.")
        else:
            print("Invalid task number.")

    elif user_choice == "5":
        print("Goodbye! 👋")
        break

    elif user_choice == "3":
        index = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print(f"Task '{tasks[index]['task']}' marked as done.")
        else:
            print("Invalid task number.")

    elif user_choice == "5":
        print("Goodbye! 👋")
        break

    else:
        print("Please enter a valid option.")


                   
        




