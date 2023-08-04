from tkinter import *
from tkinter.ttk import *
from time import strftime
from datetime import datetime

root = Tk()
root.title("Digital Clock")


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)

    label.after(1000, time)



label = Label(root, font=("ds-digital", 50),  background="black", foreground="cyan")
sn = datetime.now()
label.config(text=f"{sn:%A, %B %d, %Y}")
label.pack(anchor='center')
time()

root.mainloop()