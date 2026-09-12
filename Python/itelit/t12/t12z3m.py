import math
class kr:
    def __init__(self,a,b,h):
        self.trapa=a
        self.trapb=b
        self.traph=h
        self.calk()
    def calk(self):
        S=((self.trapa+self.trapb)/2)*self.traph
        print("Площа трапеції з основами",self.trapa,"та",self.trapb,"і висотою",self.traph,"=",S)
