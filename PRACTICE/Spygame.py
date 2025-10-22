#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spygame(nums):
    userinput = input("Enter a series of numbers: ")
    nums = [int(n) for n in userinput.split()]

    code = [0,0,7]
    code_index = 0
    for num in nums:
        if num == code[code_index]:
            code_index += 1
    if code_index == len(code):
        print("Found the spy! ")
        return True
    
    print("Not found!")
    return False    

spygame() 
