from tkinter import*
from random import randint
ss=[]
i=0
f="ss"+str(i)
ss.append(f)
ss[0]=Tk()
w1=ss[0].winfo_screenwidth()
q1=ss[0].winfo_screenheight()
w=randint(0,w1-300)
q=randint(0,q1-300)
ss[0].geometry("300x300+{}+{}".format(w,q))
ss[0].overrideredirect(1)
def pups():
    global ss,i
    i+=1
    f="ss"+str(i)
    ss.append(f)
    ss[-1]=Tk()
    w=randint(0,w1-300)
    q=randint(0,q1-300)
    ss[-1].geometry("300x300+{}+{}".format(w,q))
    ss[-1].overrideredirect(1)
    b=Button(ss[-1],text="ok",command=pups)
    b.place(x=125,y=125)
    ss[0].destroy()
    ss.pop(0)
b=Button(ss[0],text="ok",command=pups)
b.place(x=125,y=125)
ss[0].mainloop()