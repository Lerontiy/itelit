from tkinter import *
import random

def click_plus(a):
    print("Додавання")
    a=int(input("Введіть число a: "))
    b=int(input("Введіть число b: "))
    print(a,"+",b,"=",a+b)
    print()
    
def click_minus(b):
    print("Віднімання")
    a=int(input("Введіть число a: "))
    b=int(input("Введіть число b: "))
    print(a,"-",b,"=",a-b)
    print()
    
def click_mnozh(c):
    print("Множення")
    a=int(input("Введіть число a: "))
    b=int(input("Введіть число b: "))
    print(a,"*",b,"=",a*b)
    print()
    
def click_dil(d):
    print("Ділення")
    a=int(input("Введіть число a: "))
    b=int(input("Введіть число b: "))
    print(a,"/",b,"=",a/b)
    print()
    
root = Tk()
root.title("Математичні операції")
root.geometry("400x300+300+250")

but1=Button(root,text="+",width=15)
but1.bind("<Button>",click_plus)
but1.pack()

but2=Button(root,text="-",width=15)
but2.bind("<Button>",click_minus)
but2.pack()

but3=Button(root,text="*",width=15)
but3.bind("<Button>",click_mnozh)
but3.pack()

but4=Button(root,text="/",width=15)
but4.bind("<Button>",click_dil)
but4.pack()

