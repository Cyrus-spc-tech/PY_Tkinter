import tkinter as tk  
window = tk.Tk()
window.title("CAnvas ")
window.geometry("800x800")
# window.configure(bg="black")  

# canvas=tk.Canvas(window, width=400, height=400, bg="black")
label = tk.Label(window, text="Hello There !! ", font=("Monospace", 20), bg="black", fg="white")
label.pack()


button = tk.Button(window, text="Click Me!", font=("Monospace", 20), bg="red", fg="white")
button.pack(pady=10)

# Start the GUI
window.mainloop()