class mas:
    def __init__(self,m,v):
        self.v=v
        self.m=m
        self.calk()
    def calk(self):
        s=0
        for i in self.m:
            s+=i
        sa=s/self.v
        print("Середнє арифметичне масиву",self.v,"чисел:\n",self.m,"=",sa)
