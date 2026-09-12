def po(n,x):
    if x==0:
        return "Неможна ставить в степень 0"
    else:
        return pow(n,x)
n=int(input("Ведіть число "))
x=int(input("Ведіть степень числа "))
print(po(n,x))
