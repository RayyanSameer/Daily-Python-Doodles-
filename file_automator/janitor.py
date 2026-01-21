import os 
import shutil

#Organize files 

def organize_files(base_path):
    print(f"Cleaning up : {base_path}")

    #Get files 
    files = os.listdir(base_path)

    #Construct path
    for filename in files:
        source_path = os.path.join(base_path,filename)

        #if only folder 
        if os.path.isdir(source_path):
            continue

        #Identify the type 
        file_type = "Others" #Default 
        if filename.endswith((".jpg",".png",".jpeg")):
            file_type = "Images"
        elif filename.endswith((".pdf",".txt",".doc")):
            file_type = "Documents"  
        elif filename.endswith(".exe"):
            file_type = "Apps"    

        #Destination 
        dest_folder = os.path.join(base_path, file_type)

        os.makedirs(dest_folder, exist_ok =True)

        #Move the file
        dest_path = os.path.join(dest_folder, filename)
            
        print(f"Moving {filename} -> {file_type}/")
        shutil.move(source_path, dest_path)

        print("--- Cleanup Complete ---")

if __name__ == "__main__":
        target = "messy_folder" 
    
    # Safety Check: Does the folder exist?
if os.path.exists(target):
        organize_files(target)
else:
        print("Error: 'messy_folder' does not exist. Did you create the sandbox?")

        
