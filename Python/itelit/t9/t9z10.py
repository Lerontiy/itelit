def sum(a,b):
    if a==b:
        s=a
    else:
        s=sum(a,b-1)+b
    return s

a=int(input("Ведіть a: "))
b=int(input("Ведіть b: "))
if a<=b:
    print("Сума чисел від ",a," до ",b," = ",sum(a,b))
else:
    print("Error")
