import random
class dil:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        try:
            self.rez=a/b
        except ZeroDivisionError:
            print("Ділення на нуль!")
        else:
            print("Результат ділення числа ",self.a," на число ", self.b," = ",self.rez)
        finally:
            print("Програма коректно завершила свою роботу")
a=random.randint(0,2)
b=random.randint(0,2)
obj=dil(a,b)

