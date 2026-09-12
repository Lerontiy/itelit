from tkinter import *
def leftFunc(self):
    root.title("Ліва кнопка мишки")
def rightFunc(self):
    root.title("Права кнопка мишки")
def motionFunc(self):
    root.title("Рух мишкою")
root = Tk()
root.title("Події мишки")
root.geometry("400x100+300+250")
root.bind("<Button-1>",leftFunc)
root.bind("<Button-3>",rightFunc)
root.bind("<Motion>",motionFunc)
root.mainloop()
