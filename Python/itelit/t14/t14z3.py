from tkinter import *

def add(self):
    tex.insert(END,ent.get()+"\n")
    ent.delete('0', END)
    
def clear(self):
    tex.delete('1.0', END)

root=Tk()
root.title("Робота з текстовими полями")
root.geometry("100x250+300+250")

ent=Entry(root)
ent.pack()

but1 = Button(root,text="Додати")
but1.bind("<Button>",add)
but1.pack()

but2 = Button(root,text="Очистити")
but2.bind("<Button>",clear)
but2.pack()

tex=Text(root)
tex.pack()
