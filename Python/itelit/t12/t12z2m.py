import math
class kr:
    def __init__(self,R,r):
        self.radR=R
        self.radr=r
        self.calk()
    def calk(self):
        S=math.pi*pow(self.radR,2)
        s=math.pi*pow(self.radr,2)
        rez=S-s
        print("Площа круга =",rez)
