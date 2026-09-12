from tkinter import *
from tkinter.messagebox import *


def func1():
    pass


def exit_func():
    if askyesno("Exit", "Закрити головне вікно?"):
        root.destroy()


root = Tk()

m = Menu(root)
root.config(menu=m)

root.title('Створення меню програми')
root.geometry('400x200')

m1 = Menu(m)
m.add_cascade(label="File", menu=m1)
m1.add_command(label="Open", command=func1)
m1.add_command(label="Exit", command=exit_func)

m2 = Menu(m)
m.add_cascade(label="Edit", menu=m2)

root.mainloop()
