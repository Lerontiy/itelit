from tkinter import *
from tkinter.filedialog import *
import fileinput


def open_func():
    opn = askopenfilename()
    for i in fileinput.input(opn):
        tex.insert(END, i)


def save_func():
    sav = asksaveasfilename()
    lat = tex.get(1.0, END)
    nk = open(sav, "w")
    nk.write(lat)
    nk.close()


root = Tk()
root.title('Створення вікна для відкриття файлів')
root.geometry('400x200')

but1 = Button(root, text='Відкрити файл', command=open_func)
but1.pack()

but2 = Button(root, text='Записати у файл', command=save_func)
but2.pack()

tex = Text(root, width=50, height=20)
tex.pack()

root.mainloop()
