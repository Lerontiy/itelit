def fact(n):
    f=1
    if n==0:
        f=1
    else:
        f=fact(n-1)*n
    return f

for i in range(1,10):
    print(i,"!=",fact(i))
