#Tiny program to take input and display in a given format 
#Day 1
first_name = (input("Enter your First Name : "))
last_name = (input("Enter your last Name : "))
conc_name = first_name + last_name
contact = (input("Enter your phone contact : "))


details = { "Name ": conc_name,
           "Contact ": contact}
print(details)