znam = int(input())
cou = 0
my_set = set()
for z in range(2,znam+1):
    for e in range(1,z):
        if e/z not in my_set:   
            cou+=1
            my_set.add(e/z)
print(cou)
