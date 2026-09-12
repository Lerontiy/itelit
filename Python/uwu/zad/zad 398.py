gos = int(input())+1
cou = 0
kus = 0
def cykl():
    global kus, cou
    if kus==0:
        cou+= 1
        kus+= 2
    for i in range(-kus, 0):
        i = -i
        if kus+i <= gos:
            kus+= i
            cou+= 1
            cykl()
cykl()
print(cou)
