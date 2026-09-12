class chusla:
    def __init__(self,a1,a2,a3):
        self.p1=a1
        self.p2=a2
        self.p3=a3
        self.func(a1,a2,a3)
    def func(self,a1,a2,a3):
        if (a1>0 and a2>0 and a3>0) or (a1<0 and a2<0 and a3<0):
            self.p4=a1+a2+a3
        else:
            self.p4=a1*a2*a3
a=int(input("Введіть 1 число :  "))
b=int(input("Введіть 2 число :  "))
c=int(input("Введіть 3 число :  "))
wyraz=chusla(a,b,c)

print("Отриманий результат над числами",wyraz.p1,
      wyraz.p2,wyraz.p3,"=",wyraz.p4)
