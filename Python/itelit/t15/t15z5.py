from tkinter import *
def entry1(self):
    m=int(entry.get())
    if m==1234:
        entry.destroy()
        lab1.destroy()
        #but1
        but1=Button(root,text="Баланс",fg="black",bg="red",
                   command=but,font="Arial 20")
        but1.grid(row=0,column=0,columnspan=2,padx=100)
def but():
    lab2.grid(row=1,column=0,columnspan=2)
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
           font="Arial 20",width=7)
lab1.grid(row=0,column=0,padx=15,pady=15)
#2 лаб
lab2=Label(root,bg="yellow",fg="black",text="На вашому рахунку: 1000грн",
            font="Arial 20")
root.mainloop()

