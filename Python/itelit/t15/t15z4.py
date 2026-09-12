from tkinter import *
def but(self):
    spys_mis=["Січень","Лютий","Березень","Квітень","Травень",
         "Червень","Липень","Серпень","Вересень","Жовтень",
         "Листопад","Грудень"]
    spys_pora=["Зима","Весна","Літо","Осінь"]
    m=int(entry.get())
    if m>0 and m<13:
        mis["text"]=spys_mis[m-1]
        if m==12 or m==1 or m==2:
            pora["text"]=spys_pora[0]
        if m==3 or m==4 or m==5:
            pora["text"]=spys_pora[1]
        if m==6 or m==7 or m==8:
            pora["text"]=spys_pora[2]
        if m==9 or m==10 or m==11:
            pora["text"]=spys_pora[3]
    else:
        mis["text"]="Повторіть"
        pora["text"]=""
    entry.delete(0,END)

root = Tk()
root.title("Визначення назви місяця та пори року")
root.geometry("400x200+300+250")

#рядок
entry=Entry(root,text="123")
entry.grid(row=0,column=0, padx=20,pady=30)
entry.bind("<Return>",but)
#1 лаб
mis=Label(root,text="Місяць",fg="black")
mis.grid(row=0,column=1, padx=20,pady=30)
#2 лаб
pora=Label(root,text="Пора року",fg="black")
pora.grid(row=0,column=2, padx=20,pady=30)

root.mainloop()

