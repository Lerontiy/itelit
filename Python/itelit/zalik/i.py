from tkinter import *
from tkinter.ttk import Button, Entry

import math

#def delFunc(self):
#    s=list(entry.get())
#    if len(s)>0:
        

def clsFunc():
    entry.delete(0,END)
def bckFunc():
    b=entry.get()
    b=b[len(b)-1]
    entry.delete(0,END)
    entry.insert(END,b)
def cloFunc():
    if ask("Exit","Завершити роботу?"):
        root.destroy()
def equFunc():
    result = eval(entry.get())
    entry.delete(0,END)
    entry.insert(END, str(result))

def plsFunc():
    entry.insert(END,"+")
def mnsFunc():
    entry.insert(END,"-")
def divFunc():
    entry.insert(END,"/")
def mulFunc():
    entry.insert(END,"*")

def oneFunc():
    entry.insert(END,"1")
def twoFunc():
    entry.insert(END,"2")
def thrFunc():
    entry.insert(END,"3")
def fouFunc():
    entry.insert(END,"4")
def fivFunc():
    entry.insert(END,"5")
def sixFunc():
    entry.insert(END,"6")
def sevFunc():
    entry.insert(END,"7")
def eigFunc():
    entry.insert(END,"8")
def ninFunc():
    entry.insert(END,"9")
def zerFunc():
    entry.insert(END,"0")

def dotFunc():
    if num==".":
        s=list(entry.get())
        if s.count(".")==0:
            entry.insert(END,num)
        else:
            entry.insert(END,".")
def lblFunc():
    result = math.sqrt(int(entry.get()))
    entry.delete(0,END)
    entry.insert(END,str(result))

root = Tk()
root.title("Калькулятор на Ttk бібліотеки Tkinter")

entry = Entry(root)
entry.grid(row=0, columnspan=4, sticky=W+E)
cls = Button(root, text="Очистити",command=clsFunc)
cls.grid(row=1, column=0)
bck = Button(root, text="Видалити",command=bckFunc)
bck.grid(row=1, column=1)
lbl = Button(root, text="Корінь",command=lblFunc)
lbl.grid(row=1, column=2)
clo = Button(root, text="Закрити",command=cloFunc)
clo.grid(row=1, column=3)
sev = Button(root, text="7",command=sevFunc)
sev.grid(row=2, column=0)
eig = Button(root, text="8",command=eigFunc)
eig.grid(row=2, column=1)
nin = Button(root, text="9",command=ninFunc)
nin.grid(row=2, column=2)
div = Button(root, text="/",command=divFunc)
div.grid(row=2, column=3)
fou = Button(root, text="4",command=fouFunc)
fou.grid(row=3, column=0)
fiv = Button(root, text="5",command=fivFunc)
fiv.grid(row=3, column=1)
six = Button(root, text="6",command=sixFunc)
six.grid(row=3, column=2)
mul = Button(root, text="*",command=mulFunc)
mul.grid(row=3, column=3)
one = Button(root, text="1",command=oneFunc)
one.grid(row=4, column=0)
two = Button(root, text="2",command=twoFunc)
two.grid(row=4, column=1)
thr = Button(root, text="3",command=thrFunc)
thr.grid(row=4, column=2)
mns = Button(root, text="-",command=mnsFunc)
mns.grid(row=4, column=3)
zer = Button(root, text="0",command=zerFunc)
zer.grid(row=5, column=0)
dot = Button(root, text=".",command=dotFunc)
dot.grid(row=5, column=1)
equ = Button(root, text="=",command=equFunc)
equ.grid(row=5, column=2)
pls = Button(root, text="+",command=plsFunc)
pls.grid(row=5, column=3)
root.mainloop()
