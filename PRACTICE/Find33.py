#FIND 33:
#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

#def find33():
"""   userinput = (input("Enter some numbers "))
    
#    numbers = [int(n) for n in userinput.split()]
#    for i in range(len(numbers) - 1):
        if numbers[i]== 3 and numbers[i+1] == 3:
            print(f"{numbers} has  matching pairs of 3 ")
            return True
        

    print(f"{numbers} has no matching pairs of 3 ")
    return False    
        
find33()
"""

def find33():
    userinput = input("Enter some numbers: ")

    if "33" in userinput:
       print(f"{userinput} has matching pairs of 3")
       return True
    else:
            print(f"{userinput} has no matching pairs of 3")
            return False 
    
find33()
