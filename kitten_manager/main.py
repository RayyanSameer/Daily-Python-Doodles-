from models import Kitten
from utils import clear, load_data, save, pass_time,get_valid_int

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
        print("Which cat? ")
        cat_idx = get_valid_int("Enter cat number: ", 1, len(cats))
        selected_cat = cats[cat_idx - 1]

        print(f"\nSelected: {selected_cat.name}")

        #Action
        print("[1] Feed ")
        print("[2] Play")
        choice = get_valid_int("Choose Action: ",1 ,2)

        if choice == 1:
            selected_cat.feed()
        elif choice == 2:
            selected_cat.play()

        # 3. Entropy
        pass_time(cats)
        input("Press Enter...")

    elif action == 'X':
        print("Saving data...")
        save(cats) # Ensure this matches the function name in utils.py
        print("System Shutdown. Goodbye.")
        break
    
    else:
        print("Invalid Command.")
        input("Press Enter...")    

