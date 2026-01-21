#Tuples are immutable 

courses1 = ["Maths","Science","Computers"]
courses2 = courses1
print(courses1)
print(courses2)

courses1[1] = "Art" #Appends possible in list 
print(courses1 , courses2) #not in tuple 

