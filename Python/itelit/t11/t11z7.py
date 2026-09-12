class work:
    def __init__(self,a3,a1="Ваша",a2="оцінка"):
        self.p1=a1
        self.p2=a2
        self.analiz(a3)
    def analiz(self,a3):
        if a3==1 or a3==2 or a3==3:
            self.p3="погана"
        if a3==4 or a3==5 or a3==6:
            self.p3="задовільна"
        if a3==7 or a3==8 or a3==9:
            self.p3="добра"
        if a3==10 or a3==11 or a3==12:
            self.p3="відмінна"
ocinka=int(input("Введіть вашу оцінку: "))
if ocinka>0 and ocinka<13:
    progress=work(ocinka)
    print(progress.p1,progress.p2,progress.p3)
else:
    print("В Україні 12ти бальна система!")

