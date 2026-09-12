from tkinter import *
root = Tk()
root.title('Створення меню програми')
root.geometry('400x200')


def func1(self):
    pass

def func2(self):
    pass

def func3(self):
    pass

def func4(self):
    pass

def func5(self):
    pass


m = Menu(root)

root.config(menu=m)

m1 = Menu(m)
m.add_cascade(label= "File", menu=m1)
m1.add_command(label="New", command=func1)
m1.add_command(label="Open", command=func2)
m1.add_command(label="Close", command=func3)

m2 = Menu(m)
m.add_cascade(label= "Help", menu=m2)
m2.add_command(label="About", command=func4)
m2.add_command(label="Exit", command=func5)

root.mainloop()
