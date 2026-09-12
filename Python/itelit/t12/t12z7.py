a=input("Введіть a: ")
b=input("Введіть b: ")
try:
    a=int(a)
    b=int(b)
    print("Сума чисел",a,"та",b,"=",a+b)
except ValueError:
    a=str(a)
    b=str(b)
    print("Конкатенція",a,"та",b,"=",a+b)
