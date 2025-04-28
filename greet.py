import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Name Greeter")
window.geometry("800x800")

# Function to greet the user and clear the entry
def greet():
    name = entry.get()  # Get text from the entry
    label.config(text=f"Hello, {name}!")  # Update the label
    entry.delete(0, tk.END)  # Clear the entry box

# Create a label
label = tk.Label(window, text="Enter your name:")
label.pack(pady=20)

# Create an entry box
entry = tk.Entry(window)
entry.pack(pady=20)

# Create a button
button = tk.Button(window, text="Greet Me!", command=greet)
button.pack(pady=10)

# Start the GUI
window.mainloop()

