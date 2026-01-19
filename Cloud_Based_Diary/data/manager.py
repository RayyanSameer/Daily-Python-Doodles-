import os 
import datetime


DATA_DIR = "data" 

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def add_entry(title ,mood,text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    if not title:
        title = f"{timestamp}.txt"
    else:
        clean_title = title.replace(" ","_")
        clean_title =f"{clean_title}.txt"

        filepath = os.path.join(DATA_DIR, title) 
#Write

    try:
        with open(filepath,"w") as file:
            file.write(f"Mood: {mood}\n\n{text}")
        return title
    except OSError as e:
        f"Mood: {mood}\n\n{text}"

