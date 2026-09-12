from tkinter import *
def vikno_radioFunc():
    vikno_radio=Toplevel(vikno_gol,bg="green",relief=SUNKEN)
    vikno_radio.geometry("400x55+300+250")
    vikno_radio.title("Вікно радіокнопок")

    var = IntVar()
    var.set(0)
    
    radio1=Radiobutton(vikno_radio,text="Вибір 1",bg="green",fg="yellow",value=1,variable=var)
    radio1.pack(anchor=W)
    radio2=Radiobutton(vikno_radio,text="Вибір 2",bg="green",fg="yellow",value=2,variable=var)
    radio2.pack(anchor=W)
    
    vikno_radio.mainloop()

def vikno_praporFunc():
    vikno_prapor=Toplevel(vikno_gol,bg="yellow",relief=SUNKEN)
    vikno_prapor.title("Вікно радіокнопок")
    vikno_prapor.geometry("400x55+300+250")

    var1=StringVar()
    var2=StringVar()
    
    check1=Checkbutton(vikno_prapor,text="Вибір 1",bg="yellow",fg="black",variable=var1)
    check1.pack()
    check2=Checkbutton(vikno_prapor,text="Вибір 2",bg="yellow",fg="black",variable=var2)
    check2.pack()
    
    check1.deselect()
    check2.deselect()
    
    vikno_prapor.mainloop()

def vikno_mitkaFunc():
    vikno_mitka=Toplevel(vikno_gol,bg="blue",relief=SUNKEN)
    vikno_mitka.title("Вікно радіокнопок")
    vikno_mitka.geometry("400x55+300+250")
    
    mitka1=Label(vikno_mitka,text="Мітка 1",bg="blue",fg="yellow",font="Arial 12 bold")
    mitka1.pack()
    mitka2=Label(vikno_mitka,text="Мітка 2",bg="blue",fg="yellow",font="Arial 12 bold")
    mitka2.pack()
    
    vikno_mitka.mainloop()



#головне
vikno_gol=Tk()
vikno_gol.title("Вікно з дочірними вікнами")
vikno_gol.geometry("400x220+300+250")

but1=Button(vikno_gol,text="Вікно радіокнопок",width="20",command=vikno_radioFunc)
but1.pack()

but2=Button(vikno_gol,text="Вікно прапорців",width="20",command=vikno_praporFunc)
but2.pack()

but3=Button(vikno_gol,text="Вікно міток",width="20",command=vikno_mitkaFunc)
but3.pack()










