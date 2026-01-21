courses = ['History','Physics','Maths','CompSci'] #Lists use  []
#Lists are indexed starting with zero

print(courses[2]) #Prints maths 

print(courses[-1]) #Prints the back of the index 

#Accessing range of values 

#First two values 

print(courses[0:2]) #Excludes 2 , includes 0
print(courses[2:]) # Starts from two
print(len(courses)) #Returns lenth of list


#List methods 
# Append method 
courses.append("Art")

#Append to specific area 
#Insert method 
courses.insert(2,'Art')

#Extend method : used for multiple values 
courses2 = ["Music","Finance","Health","Geography"]
courses.extend(courses2)
print(courses)

#Deleting an element 
courses.remove("Maths")
print(courses)

#List Sorting
courses.sort(reverse=True)
print(courses)

#Finding the index of a certain value 
print(courses.index("CompSci"))

#Check if X in list :
print("Car" in courses)

#ListLoops
for item in courses:
    print(item)