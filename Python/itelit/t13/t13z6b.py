from tkinter import *
import random

def click_plus():
    print("Додавання")
    a=int(input("Введіть число a: "))
    b=int(input("Введіть число b: "))
    print(a,"+",b,"=",a+b)
    print()
    
def click_minus():
    print("Віднімання")
    a=int(input("Введіть число a: "))
    b=int(input("Введіть число b: "))
    print(a,"-",b,"=",a-b)
    print()
    
def click_mnozh():
    print("Множення")
    a=int(input("Введіть число a: "))
    b=int(input("Введіть число b: "))
    print(a,"*",b,"=",a*b)
    print()
    
def click_dil():
    print("Ділення")
    a=int(input("Введіть число a: "))
    b=int(input("Введіть число b: "))
    print(a,"/",b,"=",a/b)
    print()
    
root = Tk()
root.title("Математичні операції")
root.geometry("400x300+300+250")
root.config(bg= "red", relief=RAISED, bd=10)

but1=Button(root, text="+", width="10", bg="blue",
           font="12", fg="white",command=click_plus).place(x=15,y=15)

but2=Button(root,text="-", width="10", bg="blue",
           font="12", fg="white",command=click_minus).place(x=15,y=55)

but3=Button(root,text="*", width="10", bg="blue",
           font="12", fg="white",command=click_mnozh).place(x=15,y=95)

but4=Button(root,text="/", width="10", bg="blue",
           font="12", fg="white",command=click_dil).place(x=15,y=135)

