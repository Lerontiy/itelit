import random
class add:
    def __init__(self,mas):
        self.p=mas
        self.calculate()
    def calculate(self):
        self.rez=sum(self.p)
        print(self.rez)

class multi:
    def __init__(self,mas):
        self.p=mas
        self.calculate()
    def calculate(self):
        d=1
        for i in self.p:
            d*=i
            self.rez=d
        print(self.rez)
a=[]
for i in range(1,5):
    a.append(random.randint(1,10))
p=a[0]
k=a[len(a)-1]
print("Список випадкових чисел: ",a)
print("1 число:",p)
print("Останнє число:",k)
if p>=k:
    print("Сумма чисел = ",end="")
    summ=add(a)
else:
    print("Добуток чисел = ",end="")
    dob=multi(a)









    
