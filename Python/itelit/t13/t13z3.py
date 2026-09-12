from tkinter import *
import random

def clickFuncVV(self):
    global a
    global b
    a=int(input("Введіть число a: "))
    b=int(input("Введіть число b: "))
    print("Значення чисел введено!")
    print("Натисніть кнопку обчислити!")
    but2.pack()
    
def clickFuncOBC(self):
    global a
    global b
    print("Обчислення:")
    print(a,"+",b,"=",a+b)
    print(a,"-",b,"=",a-b)
    print(a,"*",b,"=",a*b)
    print(a,"/",b,"=",a/b)

root = Tk()
root.title("Операції над введеними числами")
root.geometry("400x300+300+250")

but1=Button(root,text="Ввести числа")
but1.bind("<Button>",clickFuncVV)
but1.pack()

but2=Button(root,text="Обислити")
but2.bind("<Button>",clickFuncOBC)
root.mainloop()


