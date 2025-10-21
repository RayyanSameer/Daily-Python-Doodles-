#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

name = str(input("Enter a name "))

def oldmacdonals(name):
    if len(name) < 4:
        print("Must be above 4 charecters")
    else:
        return name[0].upper + name[1:3] + name[3].upper + name[4]    