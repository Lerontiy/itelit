class rozklad:
    less10=["Інформатика","Математика","Фізика","Хімія","Фізкультура","Алгебра"]
    less11=["Геометрія","Історія","Хімія","Правознавство","Алгебра","Інформатика","Фізкультура"]
    
    def zmina(self, urok):
        temp=self.less10[urok]
        print(temp)
        self.less10[urok]=self.less11[urok]
        self.less11[urok]=temp
        
predmet10=rozklad()
predmet11=rozklad()
#print less10
print("Предмети до заміни в 10 класі")
nom=1
for i in predmet10.less10:
    print(nom,").",i)
    nom+=1
#print less11
print("Предмети до заміни в 11 класі")
nom=1
for i in predmet11.less11:
    print(nom,").",i)
    nom+=1
print("==============================")
    
n=int(input("Введіть номер уроку для заміни "))
if n>len(predmet10.less10) or n<=0:
    print("Такого уроку немає")
else:
    predmet10.zmina(n-1)
#Виведення розкладу уроків після заміни
#print less10
print("Предмети після заміни в 10 класі")
nom=1
for i in predmet10.less10:
    print(nom,").",i)
    nom+=1
#print less11
print("Предмети після заміни в 11 класі")
nom=1
for i in predmet11.less11:
    print(nom,").",i)
    nom+=1










    
