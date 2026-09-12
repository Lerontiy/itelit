from tkinter import*
ss=Tk()
ss.geometry("400x400")
a=0
k11=0
k12=0
k13=0
k21=0
k22=0
k23=0
k31=0
k32=0
k33=0
x11=0
x12=0
x13=0
x21=0
x22=0
x23=0
x1=0
x2=0
o11=0
o12=0
o13=0
o21=0
o22=0
o23=0
o1=0
o2=0

def bb11():
    global a,k11,x11,x21,x1,o11,o21,o1
    if k11==0:
        a+=1
        k11+=1
        if a%2==1:
            b11['text']="X"
            b11['bg']="red"
            x11+=1
            x21+=1
            x1+=1
        else:
            b11['text']="O"
            b11['bg']="green"
            o11+=1
            o21+=1
            o1+=1
def bb12():
    global a,k12,x12,x21,o12,o21
    if k12==0:
        a+=1
        k12+=1
        if a%2==1:
            b12['text']="X"
            b12['bg']="red"
            x12+=1
            x21+=1
        else:
            b12['text']="O"
            b12['bg']="green"
            o12+=1
            o21+=1
def bb13():
    global a,k13,x13,x21,x2,o13,o21,o2
    if k13==0:
        a+=1
        k13+=1
        if a%2==1:
            b13['text']="X"
            b13['bg']="red"
            x13+=1
            x21+=1
            x2+=1
        else:
            b13['text']="O"
            b13['bg']="green"
            o13+=1
            o21+=1
            o2+=1
def bb21():
    global a,k21,x11,x22,o11,o22
    if k21==0:
        a+=1
        k21+=1
        if a%2==1:
            b21['text']="X"
            b21['bg']="red"
            x11+=1
            x22+=1
        else:
            b21['text']="O"
            b21['bg']="green"
            o11+=1
            o22+=1
def bb22():
    global a,k22,x12,x22,x1,x2,o12,o22,o1,o2
    if k22==0:
        a+=1
        k22+=1
        if a%2==1:
            b22['text']="X"
            b22['bg']="red"
            x12+=1
            x22+=1
            x1+=1
            x2+=1
        else:
            b22['text']="O"
            b22['bg']="green"
            o12+=1
            o22+=1
            o1+=1
            o2+=1
def bb23():
    global a,k23,x13,x22,o13,o22
    if k23==0:
        a+=1
        k23+=1
        if a%2==1:
            b23['text']="X"
            b23['bg']="red"
            x13+=1
            x22+=1
        else:
            b23['text']="O"
            b23['bg']="green"
            o13+=1
            o22+=1
            
def bb31():
    global a,k31,x11,x23,x2,o11,o23,o2
    if k31==0:
        a+=1
        k31+=1
        if a%2==1:
            b31['text']="X"
            b31['bg']="red"
            x11+=1
            x23+=1
            x2+=1
        else:
            b31['text']="O"
            b31['bg']="green"
            o11+=1
            o23+=1
            o2+=1
def bb32():
    global a,k32,x12,x23,o12,o23
    if k32==0:
        a+=1
        k32+=1
        if a%2==1:
            b32['text']="X"
            b32['bg']="red"
            x12+=1
            x23+=1
        else:
            b32['text']="O"
            b32['bg']="green"
            o12+=1
            o23+=1
def bb33():
    global a,k33,x13,x23,x1,o13,o23,o1
    if k33==0:
        a+=1
        k33+=1
        if a%2==1:
            b33['text']="X"
            b33['bg']="red"
            x13+=1
            x23+=1
            x1+=1
        else:
            b33['text']="O"
            b33['bg']="green"
            o13+=1
            o23+=1
            o1+=1
def perem():
    global x11,x12,x13,x21,x22,x23,x1,x2,o11,o12,o13,o21,o22,o23,o1,o2
    if x11==3 or x12==3 or x13==3 or x21==3 or x22==3 or x23==3 or x1==3 or x2==3:
        b['text']="Виграли Х"
    if o11==3 or o12==3 or o13==3 or o21==3 or o22==3 or o23==3 or o1==3 or o2==3:
        b['text']="Виграли O"

b11=Button(ss,width=10,height=4,bg="#fff000",command=bb11)
b11.place(x=50, y=50)
b12=Button(ss,width=10,height=4,bg="#fff000",command=bb12)
b12.place(x=130, y=50)
b13=Button(ss,width=10,height=4,bg="#fff000",command=bb13)
b13.place(x=210, y=50)
b21=Button(ss,width=10,height=4,bg="#fff000",command=bb21)
b21.place(x=50, y=120)
b22=Button(ss,width=10,height=4,bg="#fff000",command=bb22)
b22.place(x=130, y=120)
b23=Button(ss,width=10,height=4,bg="#fff000",command=bb23)
b23.place(x=210, y=120)
b31=Button(ss,width=10,height=4,bg="#fff000",command=bb31)
b31.place(x=50, y=190)
b32=Button(ss,width=10,height=4,bg="#fff000",command=bb32)
b32.place(x=130, y=190)
b33=Button(ss,width=10,height=4,bg="#fff000",command=bb33)
b33.place(x=210, y=190)
b=Button(ss,width=10,height=4,bg="#fff000",command=perem)
b.place(x=150, y=300)