class uchni:
    def __init__(self,a1,a2,a3=12,a4=0):
        self.p1=a1
        self.p2=a2
        self.p3=a3
        self.p4=a4
uch1=uchni("Стас....", "Сорба...",10)
uch2=uchni("Ігор....", "Кудінов.",7,5)
uch3=uchni("Соломія.", "Прокопів",9,10)
uch4=uchni("Альона..", "Іващук..",10,7)
uch5=uchni("Богдан..", "Охрімчук",11,6)

print("Ім'я     Призвище Усп. Проп.")
print(uch1.p1,uch1.p2,uch1.p3,"\t",uch1.p4)
print(uch2.p1,uch2.p2,uch2.p3,"\t",uch2.p4)
print(uch3.p1,uch3.p2,uch3.p3,"\t",uch3.p4)
print(uch4.p1,uch4.p2,uch4.p3,"\t",uch4.p4)
print(uch5.p1,uch5.p2,uch5.p3,"\t",uch5.p4)
