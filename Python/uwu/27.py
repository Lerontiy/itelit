from tkinter import*
from random import randint
ss=Tk()
ss.geometry("600x600")

q=[10,10,10,10,10]
w=[10,10,10,10,10]
r=10
t=0
zx1=randint(0,59)
zx2=randint(0,59)
s=0

b1=Button(ss,bg="#000fff")
b1.place(x=q[0],y=w[0],width=10,height=10)
b2=Button(ss,bg="#000fff")
b2.place(x=q[1],y=w[1],width=10,height=10)
b3=Button(ss,bg="#000fff")
b3.place(x=q[2],y=w[2],width=10,height=10)
b4=Button(ss,bg="#000fff")
b4.place(x=q[3],y=w[3],width=10,height=10)
b5=Button(ss,bg="#000fff")
b5.place(x=q[4],y=w[4],width=10,height=10)
zx=Button(ss,bg="#fff000")
zx.place(x=zx1*10,y=zx2*10,width=10,height=10)
l=Label(ss,text=s,font="Arial, 16")
l.place(x=560,y=10)

def go():
    global q,w,r,t,zx1,zx2,s
    for i in range(4,0,-1):
        q[i]=q[i-1]
        w[i]=w[i-1]
    q[0]+=r
    w[0]+=t
    b1.place(x=q[0],y=w[0],width=10,height=10)
    b2.place(x=q[1],y=w[1],width=10,height=10)
    b3.place(x=q[2],y=w[2],width=10,height=10)
    b4.place(x=q[3],y=w[3],width=10,height=10)
    b5.place(x=q[4],y=w[4],width=10,height=10)
    ss.after(100,go)
    if q[0]==zx1*10 and w[0]==zx2*10:
        zx1=randint(0,59)
        zx2=randint(0,59) 
        zx.place(x=zx1*10,y=zx2*10,width=10,height=10)
        s+=1
        l['text']=s
def move(ev):
    global r,t
    if ev.keysym=='Left':
        r=-10
        t=0
    elif ev.keysym=='Right':
        r=10
        t=0
    elif ev.keysym=='Up':
        r=0
        t=-10
    elif ev.keysym=='Down':
        r=0
        t=10

b1.bind_all("<KeyPress-Left>",move)
b1.bind_all("<KeyPress-Right>",move)
b1.bind_all("<KeyPress-Up>",move)
b1.bind_all("<KeyPress-Down>",move)

go()
ss.mainloop()