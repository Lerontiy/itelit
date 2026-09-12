int(input())
my_set = set()
my_input = input()
buffer = ""
for i in my_input:
    if i==" ":
        my_set.add(int(buffer))
        buffer = ""
    else:
        buffer+=i
my_set.add(int(buffer))
del my_input
del buffer

max_num = max(my_set)
my_set.discard(max(my_set))

non_fis = set()
cou = 0
for i in my_set:
    cou += 1
    if i%2 != 0:
        non_fis.add(i)
    if max_num%2 == 0 and len(non_fis) == 0 and cou == len(my_set):
        print(max_num)
        break
    elif cou == len(my_set):
        pop = 1
        if max_num%2 != 0:
            for j in my_set:
                pop *= j
        else:
            for j in non_fis:
                pop *= j
        print(pop*max_num)
        break

