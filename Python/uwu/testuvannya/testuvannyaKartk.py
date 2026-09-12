from tkinter import *

def submitFunc():
    if var.get()==1:
        kart['file'] = "kot1.png"
    if var.get()==2:
        kart['file'] = "kot2.png"
    if var.get()==3:
        kart['file'] = "kot3.png"
    if var.get()==4:
        kart['file'] = "kot4.png"
    
root = Tk()
root.geometry("300x340")

var = IntVar()
var.set(0)

lab1 = Label(root, text="Обери пору року", font="Arial, 14")

radioZima = Radiobutton(root, variable=var, value=1, text="Зима", command=submitFunc)
radioVesna = Radiobutton(root, variable=var, value=2, text="Весна", command=submitFunc)
radioLito = Radiobutton(root, variable=var, value=3, text="Літо", command=submitFunc)
radioOsin = Radiobutton(root, variable=var, value=4, text="Осінь", command=submitFunc)

kart = PhotoImage()
labPhoto = Label(root, width=200, height=200)
labPhoto.image = kart
labPhoto['image'] = labPhoto.image

lab1.pack(anchor=W)
radioZima.pack(anchor=W)
radioVesna.pack(anchor=W)
radioLito.pack(anchor=W)
radioOsin.pack(anchor=W)
labPhoto.pack(anchor=W)



