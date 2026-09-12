from tkinter import *
from tkinter.filedialog import *


def save_func():
    sav = asksaveasfilename()
    lat = tex.get(1.0, END)
    nk = open(sav, "w")
    nk.write(lat)
    nk.close()


root = Tk()
root.title('Створення вікна для запису інформації у файл')
root.geometry('400x200')

but1 = Button(root, text='Записати у файл', command=save_func)
but1.pack()

tex = Text(root, width=50, height=20)
tex.pack()

root.mainloop()
