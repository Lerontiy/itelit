l = []
for i in range(4):
    l.append(input())
print(l)
maximum = l[0]
for i in l:
    if l.count(i)>l.count(maximum):
        maximum = i
print(f"{maximum}, {l.count(maximum)}")
    

