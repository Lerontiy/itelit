class rozklad:
    less=["Інформатика","Математика","Фізика","Хімія","Фізкультура","Алгебра",]
    def alert(self, urok):
        print(self.less[urok])
predmet=rozklad()
nom=1
for i in predmet.less:
    print(nom,").",i)
    nom+=1
n=int(input("Введіть номер уроку "))
if n>len(predmet.less) or n<=0:
    print("Такого уроку немає")
else:
    predmet.alert(n-1)
