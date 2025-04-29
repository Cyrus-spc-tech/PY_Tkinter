import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime

root= tk.Tk()
root.config(bg="",padx=10,pady=10)
root.geometry("600x400")

root.title("Notepad")
root.iconbitmap(r"d:\REPO\PY_Tkinter\Notepad\note.ico")

#function
def cmdTimeDate():     
    now = datetime.now()
    label = tk.messagebox.showinfo("Time/Date", now.strftime("Date : %Y-%m-%d \n Time : %H:%M:%S"))
def helpm():     
    label = messagebox.showinfo("About Notepad", "Notepad by - \n Cyrus-spc-tech")

#scrollbar
notepad = tk.Scrollbar(root)
notepad.pack(side=tk.RIGHT, fill=tk.Y)









#menu
notepadMenu = tk.Menu(root)
root.configure(menu=notepadMenu)
#file menu
fileMenu = tk.Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='File', menu = fileMenu)

#adding options in file menu
fileMenu.add_command(label='New')
fileMenu.add_command(label='Open...')
fileMenu.add_command(label='Save')
fileMenu.add_command(label='Save As...')
fileMenu.add_separator()
fileMenu.add_command(label='Exit')

#edit menu
editmenu=tk.Menu(notepadMenu, tearoff=False)
notepadMenu.add_cascade(label='Edit', menu=editmenu)
#adding options in edit menu
editmenu.add_command(label='Undo')
editmenu.add_command(label='Redo')
editmenu.add_separator()
editmenu.add_command(label='Cut')
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')
editmenu.add_command(label='Delete')
editmenu.add_separator()
editmenu.add_command(label='Select All')
editmenu.add_command(label='Time/Date' , command=cmdTimeDate)

#help menu
help=tk.Menu(notepadMenu, tearoff=False)
notepadMenu.add_cascade(label='About', menu=help)
#adding options in help menu
help.add_command(label='About Notepad', command=helpm)






root.mainloop()