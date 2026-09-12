my_set = []
for j in range(2):
    my_input = input()
    buffer = ""
    my_inputs = []
    for i in my_input:
        if i==" ":
            my_set.append(int(buffer))
            buffer = ""
        else:
            buffer+=i
    my_set.append(int(buffer))
    
minus_list = []
for i in range(int(len(my_set) / 2)):
    minus_list.append( my_set[i+3] - my_set[i] )

pop = 0
for i in range(1, 4):
    if str(minus_list[-i])[0] == "-":
        minus_list[-i] += 60
        pop = 1
    if pop == 1:
        if (i == 2 or i == 3) and my_set[-i + 1] < my_set[-i - 2]:
            minus_list[-i] -= 1

eazy_set = ""
for i in minus_list:
    eazy_set+= str(i)
    eazy_set+= " "
    
print(eazy_set)
       
    
