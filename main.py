import tkinter as tk
app = tk.Tk()
app.title("Hello World!")
app.geometry("300x200")
label = tk.Label(app, text="Hello World!")
label.pack(pady=20)
button = tk.Button(app, text="Click Me!", command=lambda: label.config(text="Button Clicked!"))
button.pack(pady=10)
tk.mainloop()
