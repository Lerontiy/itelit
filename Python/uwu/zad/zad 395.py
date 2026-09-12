int(input())
my_input = input()
my_set = []
buffer = ""
for i in my_input:
    if i==" ":
        my_set.append(int(buffer))
        buffer = ""
    else:
        buffer+=i
my_set.append(int(buffer))

clear_set = []
for i in my_set:
    my_cou = 0
    for e in my_set:
        my_cou+=1
        if i%e==0 and i!=e:
            break
        elif my_cou==len(my_set):
            clear_set.append(i)

eazy_set = ""
for i in clear_set:
    eazy_set+= str(i)
    eazy_set+= " "
print(eazy_set)
       
