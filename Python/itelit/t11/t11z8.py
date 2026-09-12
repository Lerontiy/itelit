class tryk:
    def __init__(self,a1,a2):
        self.p1=a1
        self.p2=a2
        self.pl()
    def pl(self):
        self.p3=(self.p1*self.p2)/2
class tryk_print(tryk):
    def pr(self):
        print("Площа трикутника =",self.p3)
a=int(input("Введіть довжину 1 катету: "))
b=int(input("Введіть довжину 2 катету: "))
tr=tryk_print(a,b)
tr.pr()
    
