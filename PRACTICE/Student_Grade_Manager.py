# Student Grade Manager
students = []  # list holding students

while True:
    print("Welcome to Grading Manager!")
    print("What would you like to do?")
    print(""" (1) Add Students \n (2) Delete Students \n (3) View Students \n (4) Update Students \n  (5) Quit \n""")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        no_of_students = int(input("How many students would you like to add? "))
        for _ in range(no_of_students):
            student_name = input("Enter name: ")
            student_usn = input("Enter USN: ")
            students.append({"Name": student_name, "USN": student_usn})

    elif choice == 2:
        target = input("Who would you like to delete? ")
        for student in students:
            if student["Name"] == target:
                students.remove(student)
                print(f"Deleted {target}!")
                break
        else:
            print("Student not found.")

    elif choice == 3:
        print("Current Students:")
        for student in students:
            print(student)

    elif choice == 4:
        target = input("Who would you like to update? ")
        for student in students:
            if student["Name"] == target:
                student["Name"] = input("Enter new name: ")
                student["USN"] = input("Enter new USN: ")
                print(f"Updated {target}!")
                break
        else:
            print("Student not found.")

    elif choice == 5:
        print("Exiting Grading Manager. Goodbye!")
        break

