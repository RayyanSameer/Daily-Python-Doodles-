import customtkinter as ctk
import manager  
import os
from tkinter import messagebox
import datetime

# 1. SETUP THEME
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class DiaryApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("Cloud Diary Vault (Secured)")
        self.geometry("900x600")

        # --- LAYOUT CONFIGURATION ---
        # We use a 2-Column Grid:
        # Column 0 = Sidebar (Small)
        # Column 1 = Main Area (Big)
        self.grid_columnconfigure(1, weight=1) 
        self.grid_rowconfigure(0, weight=1)   

        # --- LEFT SIDEBAR (File List) ---
        self.sidebar_frame = ctk.CTkScrollableFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
       


        # --- NEW CODE START ---
        self.clock_label = ctk.CTkLabel(self.sidebar_frame, text="Loading...", font=("Consolas", 14))
        self.clock_label.pack(pady=5)
        
        # --- SEARCH BAR ---
        self.search_entry = ctk.CTkEntry(self.sidebar_frame, placeholder_text="🔍 Search...")
        self.search_entry.pack(padx=10, pady=(10, 0), fill="x")
        
        # Bind the typing event (KeyRelease) to the filter function
        self.search_entry.bind("<KeyRelease>", self.filter_list)

        # Start the timer loop
        self.update_clock()

        self.refresh_btn = ctk.CTkButton(self.sidebar_frame, text=" Refresh List", command=self.load_file_list)
        self.refresh_btn.pack(padx=10, pady=10)

        self.add_btn = ctk.CTkButton(self.sidebar_frame, text = "New Entry", command= self.add_entry_dialog)
        self.add_btn.pack(padx = 10, pady = 10)

        # --- RIGHT AREA (Editor) ---
        self.main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

       
        self.entry_title = ctk.CTkLabel(self.main_frame, text="Select an entry...", font=ctk.CTkFont(size=24))
        self.entry_title.pack(anchor="w", pady=(0, 10))

        # Text Box 
        self.text_area = ctk.CTkTextbox(self.main_frame, width=600, height=400, font=("Consolas", 14))
        self.text_area.pack(fill="both", expand=True)

        # Save Button (Bottom Right)
        self.save_btn = ctk.CTkButton(self.main_frame, text=" Save Changes", fg_color="green", command=self.save_current_entry)
        self.save_btn.pack(anchor="e", pady=10)

        self.delete_btn = ctk.CTkButton(self.main_frame, text=" Delete", fg_color="red", command=self.delete_current_entry)
        self.save_btn.pack(anchor="e", pady=10, side="left")

        # Helper Variable to track which file we are editing
        self.current_filename = None

        # Load the files immediately on start
        self.load_file_list()

    def load_file_list(self, query=None):
        """ Clears sidebar and re-adds buttons (with optional filtering) """
        
        # 1. Clear old buttons (Protect System Buttons)
        for widget in self.sidebar_frame.winfo_children():
            if isinstance(widget, ctk.CTkButton):
                if widget not in [self.refresh_btn, self.add_btn]:
                    widget.destroy()

        # 2. Get all files
        files = manager.list_entries()
        
        # 3. Filter them (if a query exists)
        if query:
            files = [f for f in files if query in f.lower()]

        # 4. Create buttons
        for f in files:
            btn = ctk.CTkButton(self.sidebar_frame, text=f, fg_color="transparent", border_width=2,
                                text_color=("gray10", "#DCE4EE"),
                                command=lambda filename=f: self.load_entry(filename))
            btn.pack(fill="x", pady=2, padx=10)

    def load_entry(self, filename):
        """ Decrypts file and puts text into the box WITH TIMESTAMP """
        content = manager.read_entry(filename)
        
        if content and " Error" in content:
            messagebox.showerror("Error", content)
            return

        # --- NEW TIMESTAMP LOGIC ---
        filepath = os.path.join(manager.DATA_DIR, filename)
        if os.path.exists(filepath):
            timestamp = os.path.getmtime(filepath)
            date_str = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        else:
            date_str = "Unknown"
        # ---------------------------

        self.current_filename = filename
        
        # Update Title with Date
        self.entry_title.configure(text=f"{filename}   (Last Saved: {date_str})")
        
        self.text_area.delete("0.0", "end")
        self.text_area.insert("0.0", content)
    def save_current_entry(self):
        """ Grabs text from box and encrypts it back to disk """
        if not self.current_filename:
            return # No file selected

        
        new_text = self.text_area.get("0.0", "end")
        
       
        success = manager.overwrite_entry(self.current_filename, new_text)
        
        if success:
            self.save_btn.configure(text=" Saved!", fg_color="green")
            
            self.after(2000, lambda: self.save_btn.configure(text=" Save Changes", fg_color="#2CC985"))
        else:
            self.save_btn.configure(text=" Error", fg_color="red")


    def add_entry_dialog(self):
        title_dialog = ctk.CTkInputDialog(text="Enter Diary Title", title = "New entry")
        filename = title_dialog.get_input()

        if not filename:
            return
        
        mood_dialog = ctk.CTkInputDialog(text="Current Mood:", title="New Entry")
        mood = mood_dialog.get_input()

        if not mood: 
            mood = "Neutral"

        manager.add_entry(filename, mood, "")
        self.load_file_list()   


    def update_clock(self):
        # Get current time
        current_time = datetime.datetime.now().strftime("%Y-%m-%d\n%H:%M:%S")
        
        # Update the label
        self.clock_label.configure(text=current_time)
        
        # Schedule next update in 1000ms (1 second)
        self.after(1000, self.update_clock)   

    def delete_current_entry(self):
        # 1. Safety Check: Is a file selected?
        if not self.current_filename: 
            return

        # 2. Confirmation Dialog
        confirm = messagebox.askyesno("Delete Entry", f"Are you sure you want to delete {self.current_filename}?") 
        
        if confirm:
            # 3. Call Manager to delete
            manager.delete_entry(self.current_filename)

            
            self.text_area.delete("0.0", "end")  # Wipe the text box
            self.entry_title.configure(text="Select an entry...")
            self.current_filename = None 
            
            # 5. REFRESH THE LIST 
            self.load_file_list()
            
           
            self.delete_btn.configure(text="Deleted!")
            self.after(1000, lambda: self.delete_btn.configure(text=" Delete"))   

    def filter_list(self, event=None):
       
        query = self.search_entry.get().lower() 
        self.load_file_list(query)    


     


        
       

if __name__ == "__main__":
    app = DiaryApp()
    app.mainloop()