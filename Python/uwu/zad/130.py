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

x1 = my_set[0]
x2 = my_set[2]
x3 = my_set[4]
y1 = my_set[1]
y2 = my_set[3]
y3 = my_set[5]

if (x2-x1)*(x3-x1)+(y2-y1)*(y3-y1) == 0:
    print(f"{x2+x3-x1} {y2+y3-y1}")
elif (x2-x1)*(x3-x2)+(y2-y1)*(y3-y2) == 0:
    print(f"{x1+x3-x2} {y1+y3-y2}")
elif (x3-x1)*(x3-x2)+(y3-y1)*(y3-y2)==0:
    print(f"{x1+x2-x3} {y1+y2-y3}")


    
