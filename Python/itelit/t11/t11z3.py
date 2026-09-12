class work:
    def __init__(self,a1,a2,a3):
        self.func(a1,a2,a3)
    def func(self,a1,a2,a3):
      print("Середнє арифметичне чисел",a1,a2,a3,"=",
            round((a1+a2+a3)/3))

a=int(input("Введіть 1 число :  "))
b=int(input("Введіть 2 число :  "))
c=int(input("Введіть 3 число :  "))
wyraz=work(a,b,c)

