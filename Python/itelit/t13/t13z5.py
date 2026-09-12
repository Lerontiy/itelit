from tkinter import *
import random

def clickFuncVV1(self):
    global a
    global b
    global m
    a=int(input("Введіть число a: "))
    b=int(input("Введіть число b: "))

    m=max(a,b)
    print("Максимальне число - це",m)
    print("Натисніть кнопку Ввести наступних 2 числа!")
    print()
    but2.pack()

def clickFuncVV2(self):
    global a
    global b
    global m1
    a=int(input("Введіть число a: "))
    b=int(input("Введіть число b: "))

    m1=min(a,b)
    print("Мінімальне число - це",m1)
    print("Натисніть кнопку Обчислити!")
    print()
    but3.pack()
    
def clickFuncOBC(self):
    global a
    global b
    print("Обчислення:")
    print(m1,"+",m,"=",m1+m)
    print(m1,"-",m,"=",m1-m)
    print(m1,"*",m,"=",m1*m)
    print(m1,"/",m,"=",m1/m)

root = Tk()
root.title("Операції над введеними числами")
root.geometry("400x300+300+250")

but1=Button(root,text="Ввести перших 2 числа")
but1.bind("<Button>",clickFuncVV1)
but1.pack()

but2=Button(root,text="Ввести наступних 2 числа")
but2.bind("<Button>",clickFuncVV2)

but3=Button(root,text="Обчислити")
but3.bind("<Button>",clickFuncOBC)
root.mainloop()



