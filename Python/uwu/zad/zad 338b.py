znam = int(input())
my_set = set()
for z in range(2,znam+1):
    for e in range(1,z):
        my_set.add(e/z)
print(len(my_set))
