from tkinter import *
root = Tk()
root.title("Розмінник")
root.geometry("450x320")

#полотно
canvas=Canvas(root,width=620,height="320",bg="silver")
#1 лаб
lab1=Label(root,text="Введіть суму грошей:")
lab1.place(x=0,y=20)
#рядок
entry=Entry(root)
entry.place(x=150,y=20)

#обчислення та виведення результату
def roz(entry):
    try:
        b=float(entry)//50
        c=float(entry)%50
        d=float(c)//20
        e=float(c)%20
        f=float(e)//5
        g=float(e)%5
        h=float(g)//2
        i=float(g)%2

        #По 50
        labPo50=Label(root,text="Кількість купюр по 50 ="+str(int(b)))
        labPo50.place(x=150,y=80)

        #По 20
        labPo20=Label(root,text="Кількість купюр по 20 ="+str(int(d)))
        labPo20.place(x=150,y=110)

        #По 5
        labPo5=Label(root,text="Кількість купюр по 5 ="+str(int(f)))
        labPo5.place(x=150,y=140)

        #По 2
        labPo2=Label(root,text="Кількість купюр по 2 ="+str(int(h)))
        labPo2.place(x=150,y=170)

        #Остача
        labOst=Label(root,text="Остача ="+str(float(i)))
        labOst.place(x=150,y=200)
    except:
        #2 лаб
        lab2=Label(root,text="Будь ласка, введіть число.")
        lab2.place(x=300,y=20)
        

        

btn=Button(root,text="Розміняти",bg="grey")
btn.bind("<Button-1>",lambda event:roz(entry.get()))
btn.place(x=180,y=50)

canvas.pack()
root.mainloop()

