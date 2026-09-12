def fun_10a(*a):
    s=0
    n=0
    for i in a:
        s+=i
        n+=1
    return s/n

def fun_10b(*b):
    s=0
    n=0
    for i in b:
        s+=i
        n+=1
    return s/n

sa=fun_10a(10,11,7,9,12,8)
sb=fun_10b(12,10,6,9)
print("Сер. кількість віджимань 10-А класу становить ",sa,"разів")
print("Сер. кількість віджимань 10-Б класу становить ",sb,"разів")

if sa>sb:
    print("10а - найкращий")
if sb>sa:
    print("10б - найкращий")
