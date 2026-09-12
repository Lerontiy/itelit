from tkinter import *
text_kalk=""
r=0
a=int(input("a = "))
#if r=1
def click_plus():
    print(a,"+",b,"=",a+b)
    r+=1
    
def click_minus():
    print("Віднімання")
    a=int(input("Введіть число a: "))
    b=int(input("Введіть число b: "))
    print(a,"-",b,"=",a-b)
    
def click_mnozh():
    print("Множення")
    a=int(input("Введіть число a: "))
    b=int(input("Введіть число b: "))
    print(a,"*",b,"=",a*b)
    
def click_dil():
    print("Ділення")
    a=int(input("Введіть число a: "))
    b=int(input("Введіть число b: "))
    print(a,"/",b,"=",a/b)


root = Tk()
root.title("Калькублятор")
root.geometry("300x400+200+150")
root.config(bd=5)

but1=Button(root,text="+", width="5", command=click_plus).place(x=200,y=300)

but2=Button(root,text="-", width="5",command=click_minus).place(x=200,y=260)

but3=Button(root,text="*", width="5",command=click_mnozh).place(x=200,y=220)

but4=Button(root,text="/", width="5",command=click_dil).place(x=200,y=180)




label=Label(root,text=text_kalk).place(x=200,y=130)


