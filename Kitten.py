import os
import json

class Kitten():
    def __init__(self,name,age,weight,hunger,thirst,emotion):
        self.name = name
        self.age = age
        self.weight = weight
        self.hunger = hunger
        self.thirst = thirst
        self.emotion = emotion

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "weight": self.weight,
            "hunger": self.hunger,
            "thirst": self.thirst,
            "emotion": self.emotion
        }    

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

def load_data():
    try:
        with open("kittens.json","r") as file:
            data = json.load(file) 
            loaded_cats = []
            for cat_data in data:
                # Create a NEW Kitten object using the saved data
                new_cat = Kitten(
                    cat_data["name"], 
                    cat_data["age"], 
                    cat_data["weight"], 
                    cat_data["hunger"], 
                    cat_data["thirst"], 
                    cat_data["emotion"]
                )
                loaded_cats.append(new_cat)
            return loaded_cats
    except FileNotFoundError:
        return None # No file found, new game   

def save_data(kitten_list): #OBJ to dict
    data = []
    for cat in kitten_list:
        data.append(cat.to_dict())

    try:
        with open("kittens.json", "w") as file:#save to disk
            json.dump(data, file, indent=4)
        print("Game saved!")        
    except Exception as e:
        print(f"Error saving data: {e}")


cats = load_data()

if cats is None:
    print("No savefile found ")
    simba = Kitten("Simba", 1, 500,50,20,"Hangry")
    scar = Kitten("Scar", 2 , 260,50,10, "Sad")
    cats = [scar,simba]
else:
    print("Loaded! Welcome back!")
    simba = cats[1]
    scar = cats[0]    
    input("Press Enter to continue...")



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
        save_data(cats)
        break
    else:
        print("Invalid command ")       


