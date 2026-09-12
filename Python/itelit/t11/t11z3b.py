class work:
    def __init__(self,a1,a2,a3):
        self.p1=a1
        self.p2=a2
        self.p3=a3
        self.func(a1,a2,a3)
    def func(self,a1,a2,a3):
      self.p4=(a1+a2+a3)/3
a=int(input("Введіть 1 число :  "))
b=int(input("Введіть 2 число :  "))
c=int(input("Введіть 3 число :  "))
wyraz=work(a,b,c)
print("Середнє арифметичне чисел",
      wyraz.p1,wyraz.p2,wyraz.p3,"=",round(wyraz.p4))

