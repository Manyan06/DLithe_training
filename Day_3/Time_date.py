from tkinter import *
from time import strftime
root = Tk()
root.title("Date and Time")
date = Label(root, font=("Arial",16))
date.pack()
time = Label(root, font=("Arial",30))
time.pack()
def update():
  date.config(text=strftime("%A, %d %B %Y"))
  time.config(text=strftime("%I: %M: %S %p"))
  root.after(1000, update)
update()
root.mainloop()