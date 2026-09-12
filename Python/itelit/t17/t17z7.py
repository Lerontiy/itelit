from tkinter import *


def red_func():
    fra['bg'] = 'red'


def green_func():
    fra['bg'] = 'green'


def blue_func():
    fra['bg'] = 'blue'


def fir_size():
    fra['width'] = 500
    fra['height'] = 500


def sec_size():
    fra['width'] = 700
    fra['height'] = 400


root = Tk()

m = Menu(root)
root.config(menu=m)

root.title('Створення та робота програми з меню')
root.config(background='black')

fra = Frame(root, width=400, height=200, bg="Black")
fra.pack()

m1 = Menu(m)
m.add_cascade(label="Color", menu=m1)
m1.add_command(label="Red", command=red_func)
m1.add_command(label="Green", command=green_func)
m1.add_command(label="Blue", command=blue_func)

m2 = Menu(m)
m.add_cascade(label="Size", menu=m2)
m2.add_command(label="500x500", command=fir_size)
m2.add_command(label="700x400", command=sec_size)

root.mainloop()
