a=[1,2,3,5,8,13,21,34,55,89]

ser=(sum(a))/len(a)
print("Середнє значення елементів списку:",ser)

one_ch=[]
if a[0]<ser:
    one_ch.append(a[0])
if a[1]<ser:
    one_ch.append(a[1])
if a[2]<ser:
    one_ch.append(a[2])
if a[3]<ser:
    one_ch.append(a[3])
if a[4]<ser:
    one_ch.append(a[4])
if a[5]<ser:
    one_ch.append(a[5])
if a[6]<ser:
    one_ch.append(a[6])
print("Перша частина елементів списку:",one_ch)

two_ch=[]
if a[7]>ser:
    two_ch.append(a[7])
if a[8]>ser:
    two_ch.append(a[8])
if a[9]>ser:
    two_ch.append(a[9])
print("Друга частина елементів списку:",two_ch)

one_ch.sort(reverse=True)
two_ch.sort(reverse=True)
a=one_ch+two_ch
print("Результуючий список:",a)
