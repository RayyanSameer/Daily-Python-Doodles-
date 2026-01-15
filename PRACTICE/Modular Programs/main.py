from models import Kitten
from utils import clear, load_data, save, pass_time

cats = load_data()

if cats is None:
    print("No dave file found. Creating Kittens...")
    simba = Kitten("Simba", 1, 500, 50, 20, "Hangry")
    scar = Kitten("Scar", 2, 260, 50, 10, "Sad")
    cats = [simba, scar]
else:
    print("Save file loaded! Welcome back.")
    input("Press Enter to launch system...")


#Actual Program 

while True: #menu
    clear()

    print("\n=== Kitten Manager 4.0 ====")
    print("Current Colony")
    for index, cat in enumerate(cats):
        print(f"[{index + 1} ] {cat.name} (Hunger : ){cat.hunger} | Mood: {cat.emotion})")

    print("\n[A] Actions (Feed/Play)")
    print("[S] View Full Stats")
    print("[X] Save & Quit")

    action = input("\nSelection: ").upper()

    if action == 'S':
        print("STATS")
        for cat in cats:
            cat.stats()
        input("Press Enter ")

    elif action == "A":
        try:
            cat_idx    = int(input("Enter Cat Number: ")) -1
            if 0 <= cat_idx < len(cats):
                selected_cat = cats[cat_idx]

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
                
                pass_time(cats)
                input("Press Enter...")
            else:
                print("Invalid Cat Number.")
                input("Press Enter...")
        except ValueError:
            print("Please enter a number!")
            input("Press Enter...")

    elif action == 'X':
        print("Saving data...")
        save(cats)
        print("System Shutdown. Goodbye.")
        break
    
    else:
        print("Invalid Command.")
        input("Press Enter...")    

