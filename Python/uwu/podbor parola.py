import tkinter as tk

password = list('domi14uw')
string = "qwertyuiopasdfghjklzxcvbnm1234567890-=[];/|\*+`'!@#$%^&*()"
mb_pass = list('12345678')
s = str()
can_stop = False

for q in string:
    mb_pass[0] = q
    for w in string:
        mb_pass[1] = w
        for e in string:
            mb_pass[2] = e
            for r in string:
                mb_pass[3] = r
                for t in string:
                    mb_pass[4] = t
                    for y in string:
                        mb_pass[5] = y
                        for u in string:
                            mb_pass[6] = u
                            for i in string:
                                mb_pass[7] = i
                                if mb_pass == password:
                                    print('Пароль вгадано')
                                    print(f'Ваш пароль: {s.join(mb_pass)}')
                                    can_stop = True
                                if can_stop:
                                    break
                            if can_stop:
                                break
                        if can_stop:
                            break
                    if can_stop:
                        break
                if can_stop:
                    break
            if can_stop:
                break
        if can_stop:
            break
    if can_stop:
        break
