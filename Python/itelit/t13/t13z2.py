from tkinter import *
import random

def clickFunc(self):
    a=random.randint(1,10)
    b=random.randint(1,10)
    print(a,"+",b,"=",a+b)
    print(a,"-",b,"=",a-b)
    print(a,"*",b,"=",a*b)
    print(a,"/",b,"=",a/b)

root = Tk()
root.title("Операції над випадковими числами")
root.geometry("400x300+300+250")
but=Button(root,text="Обислити")
but.bind("<Button>",clickFunc)
but.pack()
root.mainloop()
