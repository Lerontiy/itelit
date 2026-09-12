from tkinter import *
from tkinter.ttk import Button, Entry
import math
from tkinter.messagebox import *

def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

def clearEdit(self):
    entry.delete(0,END)
    
def clearFunc(self):
    entry.delete(0,END)

def exitFunc(self):
    if askyesno("EXIT", "Завершити роботу?"):
        root.destroy()
        
def addFunc(event,num):
    if num == ".":
        s=list(entry.get())
        if s.count(".")==0:
            entry.insert(END,num)
    else:
        entry.insert(END,num)

def delFunc(self):
    s=list(entry.get())
    if len(s)>0:
        del s[len(s)-1]
    entry.delete(0,END)
    for i in s:
        entry.insert(END,i)

def korFunc(self):
    tn=entry.get()
    if tn!="" and is_digit(tn):
        s=float(entry.get())
        if s>=0:
            s=math.sqrt(s)
            entry.delete(0,END)
            entry.insert(END,s)

def calcFunc(event,op):
    global n1,oper
    oper=op
    tn1=entry.get()
    if tn1!="" and is_digit(tn1):
        n1=float(entry.get())
        entry.delete(0,END)

def rezFunc(self):
    global n1
    tn2=entry.get()
    if tn2!="" and is_digit(tn2):
        n2=float(entry.get())
        if oper=="+":
            r=n1+n2
            entry.delete(0,END)
            entry.insert(END,r)
        if oper=="-":
            r=n1-n2
            entry.delete(0,END)
            entry.insert(END,r)
        if oper=="*":
            r=n1*n2
            entry.delete(0,END)
            entry.insert(END,r)
        if oper=="/":
            if n2>0:
                r=n1/n2
                entry.delete(0,END)
                entry.insert(END,r)
            else:
                r=0
        n1=r



root = Tk()
root.title("Калькулятор на Ttk бібліотеки Tkinter")

entry = Entry(root)
entry.bind("<KeyPress>",clearEdit)
entry.grid(row=0, columnspan=4, sticky=W+E)

cls = Button(root, text="Очистити")
cls.bind("<Button-1>",clearFunc)
cls.grid(row=1, column=0)

bck = Button(root, text="Видалити")
bck.bind("<Button-1>",delFunc)
bck.grid(row=1, column=1)

kor = Button(root, text="Корінь")
kor.bind("<Button-1>",korFunc)
kor.grid(row=1, column=2)

clo = Button(root, text="Закрити")
clo.bind("<Button-1>",exitFunc)
clo.grid(row=1, column=3)

sev = Button(root, text="7")
sev.bind("<Button-1>",lambda event,n="7": addFunc(event,n))
sev.grid(row=2, column=0)

eig = Button(root, text="8")
eig.bind("<Button-1>",lambda event,n="8": addFunc(event,n))
eig.grid(row=2, column=1)

nin = Button(root, text="9")
nin.bind("<Button-1>",lambda event,n="9": addFunc(event,n))
nin.grid(row=2, column=2)

div = Button(root, text="/")
div.bind("<Button-1>",lambda event,n="/": calcFunc(event,n))
div.grid(row=2, column=3)

fou = Button(root, text="4")
fou.bind("<Button-1>",lambda event,n="4": addFunc(event,n))
fou.grid(row=3, column=0)

fiv = Button(root, text="5")
fiv.bind("<Button-1>",lambda event,n="5": addFunc(event,n))
fiv.grid(row=3, column=1)

six = Button(root, text="6")
six.bind("<Button-1>",lambda event,n="6": addFunc(event,n))
six.grid(row=3, column=2)

mul = Button(root, text="*")
mul.bind("<Button-1>",lambda event,n="*": calcFunc(event,n))
mul.grid(row=3, column=3)

one = Button(root, text="1")
one.bind("<Button-1>",lambda event,n="1": addFunc(event,n))
one.grid(row=4, column=0)

two = Button(root, text="2")
two.bind("<Button-1>",lambda event,n="2": addFunc(event,n))
two.grid(row=4, column=1)

thr = Button(root, text="3")
thr.bind("<Button-1>",lambda event,n="3": addFunc(event,n))
thr.grid(row=4, column=2)

mns = Button(root, text="-")
mns.bind("<Button-1>",lambda event,n="-": calcFunc(event,n))
mns.grid(row=4, column=3)

zer = Button(root, text="0")
zer.bind("<Button-1>",lambda event,n="0": addFunc(event,n))
zer.grid(row=5, column=0)

dot = Button(root, text=".")
dot.bind("<Button-1>",lambda event,n=".": addFunc(event,n))
dot.grid(row=5, column=1)

equ = Button(root, text="=")
equ.bind("<Button-1>",rezFunc)
equ.grid(row=5, column=2)

pls = Button(root, text="+")
pls.bind("<Button-1>",lambda event,n="+": calcFunc(event,n))
pls.grid(row=5, column=3)

root.mainloop()












