import os

class Kitten():
    def __init__(self,name,age,weight,hunger,thirst,emotion):
        self.name = name
        self.age = age
        self.weight = weight
        self.hunger = hunger
        self.thirst = thirst
        self.emotion = emotion

    def stats(self):
        print(f"Name: {self.name} | Age: {self.age} | Weight: {self.weight}g | Hunger : {self.hunger} | thirst {self.thirst} ")
        print(f"Status: {self.emotion}")
        print("_" * 30)

    def feed(self):
        print(f"Feeding {self.name}.....")
        self.weight += 20
        self.hunger -= 20
        self.emotion = "Happy"

def clear():
    os.system('cls' if os.name =='nt' else 'clear')    


simba = Kitten("Simba", 1, 500,50,20,"Hangry")
scar = Kitten("Scar", 2 , 260,50,10, "Sad")

while True:

    clear()


    print("\n---KITTEN MANAGER----")
    print("Press [S] to see stats")
    print("Press [F] to feed Simba")
    print("Press [Q] to quit")

    action = input("Selection: ").upper()

    if action == 'S':
        simba.stats()
        scar.stats()
        input("\nPress Enter to return to menu...")
    elif action == 'F':
        simba.feed() 
        input("\nPress Enter to return to menu...")
    elif action == 'Q':
        print("Bye!")
        break
    else:
        print("Invalid command ")       


