import random
s1=set(random.randint(1,50) for i in range(10))
print("Перша множина:",s1)
print("Довжина першої множини:",len(s1))
print()

s2=set(random.randint(1,50) for i in range(10))
print("Друга множина:",s2)
print("Довжина другої множини:",len(s2))
print()

ob=s1.union(s2)
print("Об'єднана множина:",ob)
print("Довжина о'бєднаної множини:",len(ob))
print()

per=s1&s2
print("Однакові елементи:",per)
print("Довжина перетину елементів множин:",len(per))
print()

riz=s1=s2
print("Різниця множин:",riz)
print("Довжина різниці множин:",len(riz))
