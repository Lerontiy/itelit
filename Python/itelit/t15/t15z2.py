from tkinter import *
def hover(self):
    lab["font"]="Arial 30"
    lab["text"]="Наведення на мітку"
def nonhover(self):
    lab["font"]="Arial 20"
    lab["text"]="Відведення з мітки"
def b1(self):
    lab["bg"]="red"
    lab["text"]="Клацнули мишкою"
def nonb1(self):
    lab["bg"]="white"
    lab["text"]="Кнопку миші не натиснуто"
root = Tk()
root.title("Події мишки")
root.geometry("500x70+300+250")
root.config(bg="white")
lab=Label(root,text="Працюємо мишкою",font="Arial 20",
          bg="white")
lab.place(x=10,y=10)
lab.bind("<Enter>",hover)
lab.bind("<Leave>",nonhover)
lab.bind("<Button-1>",b1)
lab.bind("<ButtonRelease-1>",nonb1)
root.mainloop()
