int(input())
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

stop = 0
for i in range(1, 1000001):
    cou = 0
    for j in my_set:
        if i%j == 0:
            cou += 1
            if cou == len(my_set):
                print(i)
                stop = 1
                break
        else:
            break
    if i == 1000000:
        pop = 1
        for k in my_set:
            pop *= k
        print(pop)
    elif stop == 1:
        break
