#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.

num1 = int(input("Enter a number : "))
num2 = int(input("Enter another number : "))
def lesser_of_two_evens(num1,num2):
    if num1 % 2 == 0 and   num2 % 2 == 0:
        #Return the lesser number 
        if num1 > num2:
            print(num2)
        else:
            print(num1)    
    else:
        #Return the greater number
        if num1 > num2:
            print(num1)
        else:
            print(num2)     

    

lesser_of_two_evens(num1,num2)