from tkinter import *

def red(self):
    label["text"]="Червоний"
    ent.delete(0,END)
    ent.insert(END,"#ff0000")
def orange(self):
    label["text"]="Оранжевий"
    ent.delete(0,END)
    ent.insert(END,"#ff7d00")
def yellow(self):
    label["text"]="Жовтий"
    ent.delete(0,END)
    ent.insert(END,"#ffff00 ")
def green(self):
    label["text"]="Зелений"
    ent.delete(0,END)
    ent.insert(END,"#00ff00")
def lightBlue(self):
    label["text"]="Голубий"
    ent.delete(0,END)
    ent.insert(END,"#007dff ")
def blue(self):
    label["text"]="Синій"
    ent.delete(0,END)
    ent.insert(END,"#0000ff")
def perple(self):
    label["text"]="Фіолетовий"
    ent.delete(0,END)
    ent.insert(END,"#7d00ff ")
 

root=Tk()
root.title("Створення мітки")
root.geometry("100x250+300+250")

label=Label(root)
label.pack()

ent=Entry(root,justify=CENTER)
ent.pack()

but1 = Button(root,bg="#ff0000",width="50")
but1.bind("<Button>",red)
but1.pack()

but2 = Button(root,bg="#ff7d00",width="50",)
but2.bind("<Button>",orange)
but2.pack()

but3 = Button(root,bg="#ffff00",width="50",)
but3.bind("<Button>",yellow)
but3.pack()

but4 = Button(root,bg="#00ff00",width="50")
but4.bind("<Button>",green)
but4.pack()

but5 = Button(root,bg="#007dff",width="50")
but5.bind("<Button>",lightBlue)
but5.pack()

but6 = Button(root,bg="#0000ff",width="50")
but6.bind("<Button>",blue)
but6.pack()

but7 = Button(root,bg="#7d00ff",width="50")
but7.bind("<Button>",perple)
but7.pack()

root.mainloop()
