def prybutok(*a):
    s=0
    n=0
    for i in a:
        s+=i
        n+=1
    return s,s/n
summa1, ser1=prybutok(9,11,18)
summa2, ser2=prybutok(9,11,18)
print("Тернопільська область:")
print("Загальний прибуток =",summa1,"млн. грн. Середнє=",round(ser1,2))
print("Львівська область:")
print("Загальний прибуток =",summa2,"млн. грн. Середнє=",round(ser2,2))
if ser1>ser2:
    print("Тернопільська область працює краще")
if ser2>ser1:
    print("Львівська область працює краще")
if ser2==ser1:
    print("Області працюють однаково")
