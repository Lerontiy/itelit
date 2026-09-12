from tkinter import *

zanyat=[]
#можно поставить hod="nolik" и первым будут ходить нолики
hod="krestik"

def gameFun(kvadrat):
    global zanyat,hod,d
    if kvadrat not in zanyat:
        if hod=="krestik":
            d[kvadrat]["text"]="X"
            d[kvadrat]["bg"]="red"
            hod="nolik"
        elif hod=="nolik":
            d[kvadrat]["text"]="O"
            d[kvadrat]["bg"]="blue"
            hod="krestik"
        zanyat.append(kvadrat)
    else:
        pass
    
    if len(zanyat)>=5:
        #3 red
        if but5["bg"]=="red":
            if but1["bg"]=="red" and but9["bg"]=="red":
                pobeda("red")
            elif but2["bg"]=="red" and but8["bg"]=="red":
                pobeda("red")
            elif but3["bg"]=="red" and but7["bg"]=="red":
                pobeda("red")
            elif but4["bg"]=="red" and but6["bg"]=="red":
                pobeda("red")
        elif but1["bg"]=="red":
            if but2["bg"]=="red" and but3["bg"]=="red":
                pobeda("red")
            elif but4["bg"]=="red" and but7["bg"]=="red":
                pobeda("red")
        elif but9["bg"]=="red":
            if but6["bg"]=="red" and but3["bg"]=="red":
                pobeda("red")
            elif but8["bg"]=="red" and but7["bg"]=="red":
                pobeda("red")
        #3 blue
        if but5["bg"]=="blue":
            if but1["bg"]=="blue" and but9["bg"]=="blue":
                pobeda("blue")
            elif but2["bg"]=="blue" and but8["bg"]=="blue":
                pobeda("blue")
            elif but3["bg"]=="blue" and but7["bg"]=="blue":
                pobeda("blue")
            elif but4["bg"]=="blue" and but6["bg"]=="blue":
                pobeda("blue")
        elif but1["bg"]=="blue":
            if but2["bg"]=="blue" and but3["bg"]=="blue":
                pobeda("blue")
            elif but4["bg"]=="blue" and but7["bg"]=="blue":
                pobeda("blue")
        elif but9["bg"]=="blue":
            if but6["bg"]=="blue" and but3["bg"]=="blue":
                pobeda("blue")
            elif but8["bg"]=="blue" and but7["bg"]=="blue":
                pobeda("blue")
            
def pobeda(pobeda):
    but1.destroy()
    but2.destroy()
    but3.destroy()
    
    but4.destroy()
    but5.destroy()
    but6.destroy()
    
    but7.destroy()
    but8.destroy()
    but9.destroy()
    if pobeda=="red":
        lab1=Label(win,text="Хрестики перемогли!",fg="red",bg="white",font="20")
    elif pobeda=="blue":
        lab1=Label(win,text="Нулі перемогли!",fg="blue",bg="white",font="20")
    lab1.place(x="55",y="100")
    
win=Tk()
win.config(bg="white",padx=1,pady=1)
win.geometry("280x294+500+500")

but1=Button(win,width="10",height="4",bg="yellow",command=lambda: gameFun("1"))
but2=Button(win,width="10",height="4",bg="yellow",command=lambda: gameFun("2"))
but3=Button(win,width="10",height="4",bg="yellow",command=lambda: gameFun("3"))

but4=Button(win,width="10",height="4",bg="yellow",command=lambda: gameFun("4"))
but5=Button(win,width="10",height="4",bg="yellow",command=lambda: gameFun("5"))
but6=Button(win,width="10",height="4",bg="yellow",command=lambda: gameFun("6"))

but7=Button(win,width="10",height="4",bg="yellow",command=lambda: gameFun("7"))
but8=Button(win,width="10",height="4",bg="yellow",command=lambda: gameFun("8"))
but9=Button(win,width="10",height="4",bg="yellow",command=lambda: gameFun("9"))

d={"1": but1, "2": but2, "3": but3, "4": but4, "5": but5, "6": but6, "7": but7, "8": but8, "9": but9}

but1.grid(row=0,column=0,padx=1,pady=1)
but2.grid(row=0,column=1,padx=1,pady=1)
but3.grid(row=0,column=2,padx=1,pady=1)

but4.grid(row=1,column=0,padx=1,pady=1)
but5.grid(row=1,column=1,padx=1,pady=1)
but6.grid(row=1,column=2,padx=1,pady=1)

but7.grid(row=2,column=0,padx=1,pady=1)
but8.grid(row=2,column=1,padx=1,pady=1)
but9.grid(row=2,column=2,padx=1,pady=1)
#ошибка в конце норма
