from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
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


def about_func():
    showinfo("Програма", "Виконано успішно!")


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
m1.add_command(label="Open", command=open_func)
m1.add_command(label="Save", command=save_func)

m2 = Menu(m)
m.add_cascade(label="Help", menu=m2)
m2.add_command(label="About", command=about_func)
m2.add_command(label="Exit", command=exit_func)

tex = Text(root, width=50, height=20)
tex.pack()

root.mainloop()
