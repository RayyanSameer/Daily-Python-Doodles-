import os
import datetime
from tkinter import messagebox
import customtkinter as ctk
import manager

# Global Configuration
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class LoginApp(ctk.CTk):
    """
    Handles the initial authentication gate.
    Dynamically switches between 'Registration' and 'Login' modes
    based on the existence of the auth file.
    """
    def __init__(self):
        super().__init__()
        self.title("Security Check")
        self.geometry("400x300")
        
        # Center grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(pady=40, padx=40, fill="both", expand=True)

        # Determine Mode: Register vs Login
        if not manager.is_password_set():
            self.lbl_text = "⚠️ Create Master Password"
            self.btn_text = "Set Password"
            self.is_registering = True
        else:
            self.lbl_text = "🔒 Enter Master Password"
            self.btn_text = "Unlock Vault"
            self.is_registering = False

        # UI Components
        self.label = ctk.CTkLabel(self.main_frame, text=self.lbl_text, font=("Arial", 16, "bold"))
        self.label.pack(pady=20)
        
        self.entry = ctk.CTkEntry(self.main_frame, show="*", width=200)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.attempt_login)

        self.btn = ctk.CTkButton(self.main_frame, text=self.btn_text, command=self.attempt_login)
        self.btn.pack(pady=10)

    def attempt_login(self, event=None):
        password = self.entry.get()
        
        if self.is_registering:
            if len(password) < 4:
                messagebox.showwarning("Weak Password", "Password must be at least 4 characters.")
                return
                
            manager.set_master_password(password)
            messagebox.showinfo("Success", "Password Set! Please log in.")
            self.destroy()
            start_main_app()
            
        else:
            if manager.verify_password(password):
                self.destroy()
                start_main_app()
            else:
                messagebox.showerror("Access Denied", "Incorrect Password.")
                self.entry.delete(0, "end")


class DiaryApp(ctk.CTk):
    """
    Main Application Window.
    Implements a Sidebar for file navigation and a Main Area for editing.
    """
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("Cloud Diary Vault (Secured)")
        self.geometry("900x600")

        # Layout: 2-Column Grid
        self.grid_columnconfigure(1, weight=1) 
        self.grid_rowconfigure(0, weight=1)   

        # --- LEFT SIDEBAR ---
        self.sidebar_frame = ctk.CTkScrollableFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="My Vault", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(padx=20, pady=(20, 10))

        # Live Clock
        self.clock_label = ctk.CTkLabel(self.sidebar_frame, text="Loading...", font=("Consolas", 14))
        self.clock_label.pack(pady=5)
        
        # Search Bar
        self.search_entry = ctk.CTkEntry(self.sidebar_frame, placeholder_text=" Search...")
        self.search_entry.pack(padx=10, pady=(10, 0), fill="x")
        self.search_entry.bind("<KeyRelease>", self.filter_list)

        # Sidebar Buttons
        self.refresh_btn = ctk.CTkButton(self.sidebar_frame, text=" Refresh List", command=self.load_file_list)
        self.refresh_btn.pack(padx=10, pady=10)

        self.add_btn = ctk.CTkButton(self.sidebar_frame, text="+ New Entry", command=self.add_entry_dialog)
        self.add_btn.pack(padx=10, pady=10)

        # --- MAIN EDITOR AREA ---
        self.main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        
        self.entry_title = ctk.CTkLabel(self.main_frame, text="Select an entry...", font=ctk.CTkFont(size=24))
        self.entry_title.pack(anchor="w", pady=(0, 10))

        self.text_area = ctk.CTkTextbox(self.main_frame, width=600, height=400, font=("Consolas", 14))
        self.text_area.pack(fill="both", expand=True)

        # Action Buttons Frame
        self.button_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.button_frame.pack(fill="x", pady=10)

        self.delete_btn = ctk.CTkButton(self.button_frame, text=" Delete", fg_color="#FF4444", hover_color="#8B0000", command=self.delete_current_entry)
        self.delete_btn.pack(side="left")

        self.save_btn = ctk.CTkButton(self.button_frame, text=" Save Changes", fg_color="green", command=self.save_current_entry)
        self.save_btn.pack(side="right")

        # State Variables
        self.current_filename = None

        # Initialization Hooks
        self.update_clock()
        self.load_file_list()

    def load_file_list(self, query=None):
        """Refreshes sidebar buttons, optionally filtering by query."""
        # Clear existing buttons (preserving system buttons)
        for widget in self.sidebar_frame.winfo_children():
            if isinstance(widget, ctk.CTkButton):
                if widget not in [self.refresh_btn, self.add_btn]:
                    widget.destroy()

        files = manager.list_entries()
        
        # Apply Search Filter
        if query:
            files = [f for f in files if query in f.lower()]

        # Generate Buttons
        for f in files:
            btn = ctk.CTkButton(self.sidebar_frame, text=f, fg_color="transparent", border_width=2,
                                text_color=("gray10", "#DCE4EE"),
                                command=lambda filename=f: self.load_entry(filename))
            btn.pack(fill="x", pady=2, padx=10)

    def load_entry(self, filename):
        """Decrypts content and updates metadata/UI."""
        content = manager.read_entry(filename)
        
        if content and " Error" in content:
            messagebox.showerror("Error", content)
            return

        # Fetch Metadata
        filepath = os.path.join(manager.DATA_DIR, filename)
        if os.path.exists(filepath):
            timestamp = os.path.getmtime(filepath)
            date_str = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        else:
            date_str = "Unknown"

        # Update UI
        self.current_filename = filename
        self.entry_title.configure(text=f"{filename}   (Last Saved: {date_str})")
        
        self.text_area.delete("0.0", "end")
        self.text_area.insert("0.0", content)

    def save_current_entry(self):
        if not self.current_filename:
            return 
        
        new_text = self.text_area.get("0.0", "end")
        success = manager.save_entry(self.current_filename, new_text)
        
        if success:
            self.save_btn.configure(text=" Saved!", fg_color="green")
            self.after(2000, lambda: self.save_btn.configure(text=" Save Changes", fg_color="#2CC985"))
        else:
            self.save_btn.configure(text=" Error", fg_color="red")

    def add_entry_dialog(self):
        title_dialog = ctk.CTkInputDialog(text="Enter Diary Title:", title="New Entry")
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
        current_time = datetime.datetime.now().strftime("%Y-%m-%d\n%H:%M:%S")
        self.clock_label.configure(text=current_time)
        self.after(1000, self.update_clock)   

    def delete_current_entry(self):
        if not self.current_filename: 
            return

        confirm = messagebox.askyesno("Delete Entry", f"Are you sure you want to delete {self.current_filename}?") 
        
        if confirm:
            manager.delete_entry(self.current_filename)
            
            # Reset UI
            self.text_area.delete("0.0", "end")
            self.entry_title.configure(text="Select an entry...")
            self.current_filename = None 
            
            self.load_file_list()
            
            # Visual Feedback
            self.delete_btn.configure(text="Deleted!")
            self.after(1000, lambda: self.delete_btn.configure(text=" Delete"))   

    def filter_list(self, event=None):
        query = self.search_entry.get().lower() 
        self.load_file_list(query)    

def start_main_app():
    app = DiaryApp()
    app.mainloop()

if __name__ == "__main__":
    login_screen = LoginApp()
    login_screen.mainloop()