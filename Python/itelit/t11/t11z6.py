class work():
    def __init__(self,a1="one",a2="two"):
        self.p1=a1
        self.p2=a2
job1=work("three","four")
print("1 об'єкт значення:",job1.p1,job1.p2)
job2=work("three")
print("2 об'єкт значення:",job2.p1,job2.p2)
job3=work()
print("3 об'єкт значення:",job3.p1,job3.p2)



