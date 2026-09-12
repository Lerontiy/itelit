class dil:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        try:
            self.res=a/b
        except ZeroDivisionError:
            print("Ділення на нуль!")
        else:
            print("Результат ділення числа ",self.a," на число ", self.b," = ",self.res)
        finally:
            print("Програма коректно завершила свою роботу")

a=int(input("Введіть ділене a: "))
b=int(input("Введіть ділене b: "))
obj=dil(a,b)
