my_set = []
my_input = input()
buffer = ""
for i in my_input:
    if i==" ":
        my_set.append(int(buffer))
        buffer = ""
    else:
        buffer+=i
my_set.append(int(buffer))

vsog = my_set[0]
pidz = my_set[1]
povr = my_set[2]
nomr = my_set[3]

rez_pidz = pidz
rez_povr = povr

while nomr < (vsog/pidz)*(rez_pidz-1):
    rez_pidz -= 1

while nomr > (vsog/pidz)*rez_pidz - (vsog/pidz/povr)*rez_povr:
    rez_povr -= 1
rez_povr = povr - rez_povr

print(rez_pidz, rez_povr)
