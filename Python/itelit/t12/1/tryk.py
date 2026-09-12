import math
class pl:
    def __init__(self,a,b,c):
        self.stor_a=a
        self.stor_b=b
        self.stor_c=c
        self.calk()
    def calk(self):
        p=(self.stor_a+self.stor_b+self.stor_c)/2
        s=math.sqrt(p*(p-self.stor_a)*(p-self.stor_b)*(p-self.stor_c))
        print("При сторонах a=",self.stor_a," b=",self.stor_b," та c=",self.stor_c,", площа =",s)
