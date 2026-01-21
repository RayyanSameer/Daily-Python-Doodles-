import customtkinter as ctk


ctk.set_appearance_mode("dark")  # 
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"


class DiaryApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("Cloud Diary v2.0")
        self.geometry("600x500")

        # A "Hello" Label
        self.label = ctk.CTkLabel(self, text="Welcome to the Vault", font=("Arial", 24))
        self.label.pack(pady=50)

        # A Test Button
        self.button = ctk.CTkButton(self, text="Click Me", command=self.button_callback)
        self.button.pack(pady=20)

    def button_callback(self):
        print("Button clicked!")
        self.label.configure(text="System Secure ")


if __name__ == "__main__":
    app = DiaryApp()
    app.mainloop()