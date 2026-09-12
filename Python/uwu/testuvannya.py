from tkinter import *

def submitFunc():
    if var.get()==2:
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

lab1 = Label(root, text="Яка зараз пора року?", font="Arial, 14")

radioZima = Radiobutton(root, variable=var, value=1, text="Зима")
radioVesna = Radiobutton(root, variable=var, value=2, text="Весна")
radioLito = Radiobutton(root, variable=var, value=3, text="Літо")
radioOsin = Radiobutton(root, variable=var, value=4, text="Осінь")

but1 = Button(root, text="Відповісти", command=submitFunc)

lab2 = Label(root, font="Arial, 14")

lab1.pack(anchor=W)
radioZima.pack(anchor=W)
radioVesna.pack(anchor=W)
radioLito.pack(anchor=W)
radioOsin.pack(anchor=W)
but1.pack(anchor=W)
