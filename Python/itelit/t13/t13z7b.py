from tkinter import *
class calk:
    def __init__(self):
        self.but1=Button(root, text="+", width="10", bg="blue",
           font="12", fg="white",command=self.click_plus).place(x=15,y=15)
        
        self.but2=Button(root,text="-", width="10", bg="blue",
           font="12", fg="white",command=self.click_minus).place(x=15,y=55)
        
        self.but3=Button(root,text="*", width="10", bg="blue",
           font="12", fg="white",command=self.click_mnozh).place(x=15,y=95)
        
        self.but4=Button(root,text="/", width="10", bg="blue",
           font="12", fg="white",command=self.click_dil).place(x=15,y=135)

        
    def click_plus(self):
        print("Додавання")
        a=int(input("Введіть число a: "))
        b=int(input("Введіть число b: "))
        print(a,"+",b,"=",a+b)
        print()
        
    def click_minus(self):
        print("Віднімання")
        a=int(input("Введіть число a: "))
        b=int(input("Введіть число b: "))
        print(a,"-",b,"=",a-b)
        print()
        
    def click_mnozh(self):
        print("Множення")
        a=int(input("Введіть число a: "))
        b=int(input("Введіть число b: "))
        print(a,"*",b,"=",a*b)
        print()
        
    def click_dil(self):
        print("Ділення")
        a=int(input("Введіть число a: "))
        b=int(input("Введіть число b: "))
        print(a,"/",b,"=",a/b)
        print()
    
root = Tk()
root.title("Математичні операції")
root.geometry("400x300+300+250")
root.config(bg= "red", relief=RAISED, bd=10)
obj=calk()
root.mainloop()





















