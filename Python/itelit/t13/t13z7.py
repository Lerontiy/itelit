from tkinter import *
class calk:
    def __init__(self):
        self.but1=Button(root,text="+",width=15)
        self.but1.bind("<Button>",self.click_plus)
        self.but1.pack()
        
        self.but2=Button(root,text="-",width=15)
        self.but2.bind("<Button>",self.click_minus)
        self.but2.pack()
        
        self.but3=Button(root,text="*",width=15)
        self.but3.bind("<Button>",self.click_mnozh)
        self.but3.pack()
        
        self.but4=Button(root,text="/",width=15)
        self.but4.bind("<Button>",self.click_dil)
        self.but4.pack()
        
    def click_plus(self,a):
        print("Додавання")
        a=int(input("Введіть число a: "))
        b=int(input("Введіть число b: "))
        print(a,"+",b,"=",a+b)
        print()
        
    def click_minus(self,b):
        print("Віднімання")
        a=int(input("Введіть число a: "))
        b=int(input("Введіть число b: "))
        print(a,"-",b,"=",a-b)
        print()
        
    def click_mnozh(self,c):
        print("Множення")
        a=int(input("Введіть число a: "))
        b=int(input("Введіть число b: "))
        print(a,"*",b,"=",a*b)
        print()
        
    def click_dil(self,d):
        print("Ділення")
        a=int(input("Введіть число a: "))
        b=int(input("Введіть число b: "))
        print(a,"/",b,"=",a/b)
        print()

root = Tk()
root.title("Математичні операції")
root.geometry("400x300+300+250")
obj=calk()
root.mainloop()
