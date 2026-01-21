import tkinter as tk 

#Making a window 

window = tk.Tk()


window.geometry("800x500")
window.title("My first GUI")

#Widgets 

#Widgets are placed on a layout system , such as a pack or a grid .

label = tk.Label(window, text="Basic Window", font=("Helvetica", 20))
label.pack(padx=20,pady=20)

textbox = tk.Text(window, height="8", font=16)



textbox.pack()

def on_click_button():
    button.config(text= "Warned Ya !")



button = tk.Button(window, text="Click Me!", font=("Arial", 12), command=on_click_button) 
button.pack(padx=10, pady=10)


buttonframe = tk.Frame(window)

buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)



btn1 = tk.Button(buttonframe, text="1", font=("Arial", 19))
btn1.grid(row=0, column=0, sticky="news", padx=5, pady=5) # columnconfigure(0, weight=1)
buttonframe.grid_rowconfigure(0, weight=1)

btn2 = tk.Button(buttonframe, text="2", font=("Arial", 19))
btn2.grid(row=0, column=1, sticky="news", padx=5, pady=5) # columnconfigure(0, weight=1)
buttonframe.grid_rowconfigure(0, weight=1)

btn3 = tk.Button(buttonframe, text="3", font=("Arial", 19))
btn3.grid(row=0, column=2, sticky="news", padx=5, pady=5) # columnconfigure(0, weight=1)
buttonframe.grid_rowconfigure(0, weight=1)


btn4 = tk.Button(buttonframe, text="4", font=("Arial", 19))
btn4.grid(row=2, column=0, sticky="news", padx=5, pady=5) # columnconfigure(0, weight=1)
buttonframe.grid_rowconfigure(0, weight=1)

btn5 = tk.Button(buttonframe, text="5", font=("Arial", 19))
btn5.grid(row=2, column=1, sticky="news", padx=5, pady=5) # columnconfigure(0, weight=1)
buttonframe.grid_rowconfigure(0, weight=1)

btn6 = tk.Button(buttonframe, text="6", font=("Arial", 19))
btn6.grid(row=2, column=2, sticky="news", padx=5, pady=5) # columnconfigure(0, weight=1)
buttonframe.grid_rowconfigure(0, weight=1)

buttonframe.pack(fill='x')








window.mainloop()

