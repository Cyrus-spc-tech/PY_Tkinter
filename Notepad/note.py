import tkinter as tk
import os

root= tk.Tk()
root.config(bg="",padx=10,pady=10)
root.geometry("600x400")

root.title("Notepad")
root.iconbitmap(r"d:\REPO\PY_Tkinter\Notepad\note.ico")

#scrollbar
notepad = tk.Scrollbar(root)
notepad.pack(side=tk.RIGHT, fill=tk.Y)

#menu
notepadmenu=tk.Menu(root)
root.config(menu=notepadmenu)


root.mainloop()