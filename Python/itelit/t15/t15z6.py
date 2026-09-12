from tkinter import *
def entry1(self):
    m=int(entry.get())
    if m==1111 or m==2222 or m==3333:
        entry.destroy()
        lab1.destroy()
        #but1
        but1=Button(root,text="Баланс",fg="black",bg="red",
                   command=but1Fun,font="Arial 20")
        but1.grid(row=0,column=0,columnspan=2,padx=100)
        if m==1111:
            lab2["text"]="На вашому рахунку: 1111грн"
            lab3["text"]="Останнє поступлення: 111грн"
        if m==2222:
            lab2["text"]="На вашому рахунку: 2222грн"
            lab3["text"]="Останнє поступлення: 222грн"
        if m==3333:
            lab2["text"]="На вашому рахунку: 3333грн"
            lab3["text"]="Останнє поступлення: 333грн"
    else:
        entry.destroy()
        lab1.config(text="PIN-код неправильний!")
        lab1.grid(rowspan="2")
def but1Fun():
    lab2.grid(row=1,column=0,columnspan=2)
    lab3.grid(row=2,column=0,columnspan=2)
root = Tk()
root.title("Моделювання роботи банкомата")
root.config(bd=5)
#root.geometry("400x100+300+250")

#рядок
entry=Entry(root,bg="yellow",fg="black",font="Arial 20"
            ,width=15)
entry.grid(row=0,column=1,padx=15,pady=15)
entry.bind("<Return>",entry1)
#1 лаб
lab1=Label(root,bg="red",fg="black",text="PIN-код",
           font="Arial 20")
lab1.grid(row=0,column=0,padx=15,pady=15)
#2 лаб
lab2=Label(root,bg="yellow",fg="black",text="На вашому рахунку:",
            font="Arial 20",width=24)
#3 лаб
lab3=Label(root,bg="yellow",fg="black",text="Останнє поступлення:",
            font="Arial 20",width=24)
root.mainloop()

