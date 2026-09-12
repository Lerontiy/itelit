from tkinter import *

a=int(input("Введіть число a: "))
b=int(input("Введіть число b: "))
c=int(input("Введіть число c: "))

def clickFunc(self):
    max=a
    if b>max:
        max=b
    if c>max:
        max=c
    print("Серед чисел",a,",",b,"та",c,"найбільше є",max,)

root = Tk()
root.title("Знаходження максимального числа")
root.geometry("400x300+300+250")
but=Button(root,text="Обислити")
but.bind("<Button>",clickFunc)
but.pack()
root.mainloop()
