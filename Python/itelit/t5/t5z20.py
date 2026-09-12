chlen=5
i=0
sum=0
while chlen>1:
    chlen=chlen*0.5
    print(f"Наступний член прогресії = {chlen}")
    i=i+1
    sum=sum+chlen
print(f"Кількість = {i}")
print(f"Сума визначених членів прогресії = {sum}")
