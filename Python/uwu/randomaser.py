from datetime import *
max_num = 0
min_num = 0
stop_code = 0
try:
    min_num = int(input('Min: '))
    max_num = int(input('Max: '))
except:
    stop_code = 1

if stop_code == 0:
    if max_num <= min_num:
        max_num = min_num + 1
    amo_rep = str(datetime.today())[11:]
    amo_rep = amo_rep.replace(":", "")
    amo_rep = amo_rep.replace(".", "")
    while amo_rep.startswith('0'):
        amo_rep = amo_rep[1:]
    amo_rep = int(amo_rep)
    print(amo_rep)

    if int(amo_rep) < max_num:
        amo_rep = str(amo_rep)
        fir_amo_rep = amo_rep
        while int(amo_rep) < max_num:
            amo_rep += fir_amo_rep
            print(amo_rep)
        amo_rep = int(amo_rep)
        del fir_amo_rep

    res_num = min_num
    for i in range(min_num, amo_rep):
        if res_num == max_num:
            res_num = min_num
        else:
            res_num += 1
    print(f'Rand({min_num}, {max_num}): {res_num}')
else:
    print('Error')
