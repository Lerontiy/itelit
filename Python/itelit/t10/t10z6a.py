class calk:
    def oper(sell,op,a,b):
        if op!="+" and op!="-" and op!="*" and op!="/":
            rez="Не вірно введена операція"
        else:
            if op=="+":
                rez=a+b
            if op=="-":
                rez=a-b
            if op=="*":
                rez=a*b
            if op=="/":
                if b>0:
                    rez=a/b
                else:
                    rez="Не можна ділити на 0"
        return rez
calk1=calk()
a=int(input("1 число: "))
b=int(input("2 число: "))
op=input("Оперант(+, -, *, /): ")
r=calk1.oper(op,a,b)
print(a,op,b,"=",r)
