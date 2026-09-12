from tkinter import *
def click():
    label.pack()
    
root = Tk()
root.title("Створення мітки")
root.geometry("400x100+300+250")

but=Button(root,text="Створити мітку", command=click)
but.pack()

label = Label(root,text="Мітка створена!",
              font="Arial 12 bold", fg="#c41e3a")

root.mainloop()
