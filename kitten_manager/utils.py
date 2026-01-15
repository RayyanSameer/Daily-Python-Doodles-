#Filesystem and logic helper 

import os 
import json
from models import Kitten

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pass_time(kitten_list):
        print("Time Passes....")
        for cat in kitten_list:
              cat.hunger += 5
              cat.thirst += 5

def save(kitten_list):
    data = []
    for cat in kitten_list:
        data.append(cat.to_dict())

    try:
            with open("kittens.json" , "w") as file:
                  json.dump(data, file,indent=4)
            print("Saved")
    except Exception as e:
          print(f"Error {e}")

def load_data():
    try:
        with open("kittens.json", "r") as file:
            data = json.load(file) 
            loaded_cats = []
            for cat_data in data:
                
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
        return None

def get_valid_int(prompt, min_val , max_val):
    while True:
        try:
            user_input = input(prompt)
            value = int(user_input)
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Error: Number must be between {min_val} and {max_val}.")
        except ValueError:
            print("Error: That is not a number. Try again.")  

