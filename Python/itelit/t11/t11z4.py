class chusla:
    def __init__(self,a1=4,a2=5):
        self.p1=a1
        self.p2=a2
        self.func(a1,a2)
    def func(self,a1,a2):
        self.p3=a1*a2
chuslo1=chusla()
chuslo2=chusla(7,8)
chuslo3=chusla(a2=9)
print("Добуток чисел : ",chuslo1.p1,"*",chuslo1.p2," = ",chuslo1.p3)
print("Добуток чисел : ",chuslo2.p1,"*",chuslo2.p2," = ",chuslo2.p3)
print("Добуток чисел : ",chuslo3.p1,"*",chuslo3.p2," = ",chuslo3.p3)
