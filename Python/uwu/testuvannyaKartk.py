from tkinter import *


def submitFunc():
    if var.get()==1:
        lab2["text"] = "Правильно"
        lab2["fg"] = "green"
    else:
        lab2["text"] = "Не правильно"
        lab2["fg"] = "red"
    lab2.pack()


root = Tk()
root.geometry("300x200")

var = IntVar()
var.set(0)

lab1 = Label(root, text="Обери пору року", font="Arial, 14")

radioZima = Radiobutton(root, variable=var, value=1, text="Зима", command=submitFunc)
radioVesna = Radiobutton(root, variable=var, value=2, text="Весна", command=submitFunc)
radioLito = Radiobutton(root, variable=var, value=3, text="Літо", command=submitFunc)
radioOsin = Radiobutton(root, variable=var, value=4, text="Осінь", command=submitFunc)

kart = PhotoImage(root, file = http://surl.li/buroc)

lab1.pack(anchor=W)
radioZima.pack(anchor=W)
radioVesna.pack(anchor=W)
radioLito.pack(anchor=W)
radioOsin.pack(anchor=W)

root.mainloop()
