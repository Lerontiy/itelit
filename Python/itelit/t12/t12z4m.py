class mas:
    def __init__(self,m):
        self.m=m
        self.calk()
    def calk(self):
        s=0
        for i in self.m:
            s+=i
        sa=s/10
        print("Середнє арифметичне масиву чисел:\n",self.m,"=",sa)
