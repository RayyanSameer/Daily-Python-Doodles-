#Sets: Unordered and Unique 
course = {"History","Art","Home EC"}
print(course)

#Every print shuffles the order 
#Sets shine when validating memberships 
#Sets also help validate common values ACROSS sets 

course = {"History","Art","Home EC"}
course2 = {"Painting","Design","Art"}

#to check whats the same here we use the intersection

print(course.intersection(course2))

#Whats NOT in a given set 

print(course.difference(course2))
#Union is used to see ALL the courses

print(course.union(course2)) 