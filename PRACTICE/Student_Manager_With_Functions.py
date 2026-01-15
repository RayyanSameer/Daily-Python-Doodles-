# Student Grade Manager
students = []  # list holding students


def addstudents():
    no_of_students = int(input("How many students would you like to add? "))
    for _ in range(no_of_students):
        student_name = input("Enter name: ")
        student_usn = input("Enter USN: ")
        students.append({"Name": student_name, "USN": student_usn})

def removestudents():
    target = input("Who would you like to delete? ")
    for student in students:
            if student["Name"] == target:
                students.remove(student)
                print(f"Deleted {target}!")
                break
            else:
                print("Student not found.")   

def view_students():
    print("Current Students:")
    for student in students:
        print(student)

def update_students():
    target = input("Who would you like to update? ")
    for student in students:
            if student["Name"] == target:
                student["Name"] = input("Enter new name: ")
                student["USN"] = input("Enter new USN: ")
                print(f"Updated {target}!")
                break
            else:
                print("Student not found.")        

def exit():
    print("Exiting Grading Manager. Goodbye!")
    quit()       
                     



while True:
    print("Welcome to Grading Manager!")
    print("What would you like to do?")
    print(""" (1) Add Students \n (2) Delete Students \n (3) View Students \n (4) Update Students \n  (5) Quit \n""")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        addstudents()

    elif choice == 2:
        removestudents()

    elif choice == 3:
        view_students()

    elif choice == 4:
        update_students()

    elif choice == 5:
        print("Exiting Grading Manager. Goodbye!")
        break

