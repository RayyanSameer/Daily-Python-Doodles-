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
        if self.hunger <= 0:
            print(f"{self.name} is full !")
        else:

            print(f"Feeding {self.name}.....")
            self.weight += 20
            self.hunger -= 20
            self.emotion = "Happy"

            if self.hunger < 0:
                self.hunger = 0


    def play(self):
        if self.hunger > 40:
            print(f"{self.name} is too hungry!")        
            self.emotion = "Grumpy"
        else:
             print(f"You rwave the laser pointer. {self.name} goes crazy!")
             self.emotion = "Ecstatic"
             self.hunger += 15
             print(f"{self.name} is tired but happy.")         


def time(kitten_list):
    for cat in kitten_list:
        cat.hunger += 5
        cat.thirst += 5              

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
    
    print("\n=== KITTEN MANAGER v3.0 ===")
    print("Current Colony:")
    for index, cat in enumerate(cats):
        print(f"[{index + 1}] {cat.name} (Hunger: {cat.hunger} | Mood: {cat.emotion})")

    print("\n[A] Actions (Feed/Play)")
    print("[S] View Full Stats")
    print("[X] Save & Quit")

    action = input("\nSelection: ").upper()

    if action == 'S':
        print("\n--- STATS ---")
        for cat in cats:
            cat.stats()
        input("Press Enter...")

    elif action == 'A':
        # 1. Select the Cat
        try:
            cat_idx = int(input("Enter Cat Number: ")) - 1
            if 0 <= cat_idx < len(cats):
                selected_cat = cats[cat_idx]
                
                # 2. Select the Action
                print(f"\nSelected: {selected_cat.name}")
                print("[1] Feed")
                print("[2] Play")
                sub_choice = input("Choose Action: ")
                
                if sub_choice == '1':
                    selected_cat.feed()
                elif sub_choice == '2':
                    selected_cat.play()
                else:
                    print("Invalid Action.")
                
                # 3. Entropy (Time Passes only when you act)
                time(cats)
                input("Press Enter...")
                
            else:
                print("Invalid Cat Number.")
                input("Press Enter...")
        except ValueError:
            print("Please enter a number!")
            input("Press Enter...")

    elif action == 'X':
        print("Saving data...")
        save_data(cats)
        print("System Shutdown. Goodbye.")
        break
    
    else:
        print("Invalid Command.")
        input("Press Enter...")