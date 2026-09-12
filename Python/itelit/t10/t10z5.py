import random
class money:
    w=["орел","решка"]
    def wybir(self, n):
        print("Виграш",self.w[n])
q=money()
wyg=random.randint(0,1)
q.wybir(wyg)
