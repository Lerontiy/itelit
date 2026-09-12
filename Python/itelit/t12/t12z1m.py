import math
class pl:
    def __init__(self,a,b):
        self.stor_a=a
        self.stor_b=b
        self.calk()
    def calk(self):
        s=math.sqrt(pow(self.stor_a,2)+pow(self.stor_b,2))
        print("При сторонах a=",self.stor_a," b=",self.stor_b,"площа =",s)
