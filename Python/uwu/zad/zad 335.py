cou_test = int(input())
for i in range(cou_test):
    bom = 0
    rat = int(input())
    for e in range(1, rat+1):
        if rat%e==0:
            if bom==0:
                bom=1
            else:
                bom=0
    print(bom)
