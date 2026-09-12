class calk:
    def plus(sell,a,b):
        return a+b
    def min(sell,a,b):
        return a-b
    def mnoz(sell,a,b):
        return a*b
    def dil(sell,a,b):
        if b>0:
            rez=a/b
        else:
            rez="Не можна ділити на 0"
        return rez
calk1=calk()
a=int(input("1 число: "))
b=int(input("2 число: "))
op=input("Оперант(+, -, *, /): ")
if op!="+" and op!="-" and op!="*" and op!="/":
    print("Не вірно введена операція")
else:
    if op=="+":
        r=calk1.plus(a,b)
    if op=="-":
        r=calk1.min(a,b)
    if op=="*":
        r=calk1.mnoz(a,b)
    if op=="/":
        r=calk1.dil(a,b)

print(a,op,b,"=",r)


