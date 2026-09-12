from tkinter import *
import random

def clickFuncVV(self):
    global a
    global b
    a=int(input("Введіть число a: "))
    print("Число a введено!")
    print("Натисніть кнопку Згенерувати!")
    but2.pack()

def clickFuncZGN(self):
    global a
    global b
    b=random.randint(1,10)
    print("Генерація числа від 1 до 10...")
    print("Число b =",b)
    print("Натисніть кнопку Обчислити!")
    but3.pack()
    
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

but2=Button(root,text="Згенерувати")
but2.bind("<Button>",clickFuncZGN)

but3=Button(root,text="Обислити")
but3.bind("<Button>",clickFuncOBC)
root.mainloop()



