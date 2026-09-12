some_input = input()
while not str(len(some_input)**0.5).endswith(".0"):
    some_input+= some_input[-1]
l = int(len(some_input))
l_side = int(len(some_input)**0.5)

ind = 0
new_input = ""
for i in range(1, l+1):
    new_input+= some_input[ind]
    ind+= l_side
    if ind >= l:
        ind-= l-1

print(new_input)

