class country:
    def __init__(self,a1,a2):
        self.p1=a1
        self.p2=a2
obj1=country("Україна", "Київ")
obj2=country("Польща", "Варшава")
obj3=country("Білорусь", "Мінськ")

print(obj1.p1,": столиця -",obj1.p2)
print(obj2.p1,": столиця -",obj2.p2)
print(obj3.p1,": столиця -",obj3.p2)
