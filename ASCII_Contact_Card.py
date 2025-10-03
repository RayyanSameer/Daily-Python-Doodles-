#Generates an ASCII style minimalist  business card

#Take user information

first_name = input("Enter first name : ")
last_name = input("Enter last name: ")
conc_name = first_name + last_name
contact = input("Enter your contact number")
email = input("Enter your email: ")
company = input("Enter your company: ")
role = input("Enter your role : ")

#Generate the dimensions of the card 

lines = [conc_name,role,company,contact,email]
max_len = max(len(line) for line in lines)
max_height = max_len + 5 

#Genaerate the actual card 

print("\n" + "+" + "_" * (max_height + 15) + " +")  #Top line 
for line in lines:
    print("| "  +  line.center(max_height + 15) + "|") #Centered text
print( "+" + "_" * (max_height + 15) + " +") # Bottom line 