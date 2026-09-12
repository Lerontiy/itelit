from tkinter import *
from tkinter.ttk import Button, Entry
from tkinter.messagebox import *
import math

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Калькулятор на Ttk бібліотеки Tkinter")

        #Style().configure("TButton",padding=(0,5,0,5),font='serif 10')

        self.columnconfigure(0,pad=3)
        self.columnconfigure(1,pad=3)
        self.columnconfigure(2,pad=3)
        self.columnconfigure(3,pad=3)

        self.rowconfigure(0,pad=3)
        self.rowconfigure(1,pad=3)
        self.rowconfigure(2,pad=3)
        self.rowconfigure(3,pad=3)
        self.rowconfigure(4,pad=3)

        self.entry = Entry(self)
        self.entry.bind("<KeyPress>",self.clearEdit)
        self.entry.grid(row=0, columnspan=4, sticky=W+E)

        self.cls = Button(self, text="Очистити")
        self.cls.bind("<Button-1>",self.clearFunc)
        self.cls.grid(row=1, column=0)

        self.bck = Button(self, text="Видалити")
        self.bck.bind("<Button-1>",self.delFunc)
        self.bck.grid(row=1, column=1)

        self.kor = Button(self, text="Корінь")
        self.kor.bind("<Button-1>",self.korFunc)
        self.kor.grid(row=1, column=2)

        self.clo = Button(self, text="Закрити")
        self.clo.bind("<Button-1>",self.exitFunc)
        self.clo.grid(row=1, column=3)

        self.sev = Button(self, text="7")
        self.sev.bind("<Button-1>",lambda event:self.addFunc("7"))
        self.sev.grid(row=2, column=0)

        self.eig = Button(self, text="8")
        self.eig.bind("<Button-1>",lambda event:self.addFunc("8"))
        self.eig.grid(row=2, column=1)

        self.nin = Button(self, text="9")
        self.nin.bind("<Button-1>",lambda event:self.addFunc("9"))
        self.nin.grid(row=2, column=2)

        self.div = Button(self, text="/")
        self.div.bind("<Button-1>",lambda event:self.calcFunc("/"))
        self.div.grid(row=2, column=3)

        self.fou = Button(self, text="4")
        self.fou.bind("<Button-1>",lambda event:self.addFunc("4"))
        self.fou.grid(row=3, column=0)

        self.fiv = Button(self, text="5")
        self.fiv.bind("<Button-1>",lambda event:self.addFunc("5"))
        self.fiv.grid(row=3, column=1)

        self.six = Button(self, text="6")
        self.six.bind("<Button-1>",lambda event:self.addFunc("6"))
        self.six.grid(row=3, column=2)

        self.mul = Button(self, text="*")
        self.mul.bind("<Button-1>",lambda event:self.calcFunc("*"))
        self.mul.grid(row=3, column=3)

        self.one = Button(self, text="1")
        self.one.bind("<Button-1>",lambda event:self.addFunc("1"))
        self.one.grid(row=4, column=0)

        self.two = Button(self, text="2")
        self.two.bind("<Button-1>",lambda event:self.addFunc("2"))
        self.two.grid(row=4, column=1)

        self.thr = Button(self, text="3")
        self.thr.bind("<Button-1>",lambda event:self.addFunc("3"))
        self.thr.grid(row=4, column=2)

        self.mns = Button(self, text="-")
        self.mns.bind("<Button-1>",lambda event:self.calcFunc("-"))
        self.mns.grid(row=4, column=3)

        self.zer = Button(self, text="0")
        self.zer.bind("<Button-1>",lambda event:self.addFunc("0"))
        self.zer.grid(row=5, column=0)

        self.dot = Button(self, text=".")
        self.dot.bind("<Button-1>",lambda event:self.addFunc("."))
        self.dot.grid(row=5, column=1)

        self.equ = Button(self, text="=")
        self.equ.bind("<Button-1>",self.rezFunc)
        self.equ.grid(row=5, column=2)

        self.pls = Button(self, text="+")
        self.pls.bind("<Button-1>",lambda event:self.calcFunc("+"))
        self.pls.grid(row=5, column=3)

        self.pack()
        
    def is_digit(self,string):
        if string.isdigit():
            return True
        else:
            try:
                float(string)
                return True
            except ValueError:
                return False

    def clearEdit(self,n):
        self.entry.delete(0,END)
    
    def clearFunc(self,n):
        self.entry.delete(0,END)

    def exitFunc(self,n):
        if askyesno("EXIT", "Завершити роботу?"):
            self.master.destroy()
        
    def addFunc(self,num):
        if num == ".":
            s=list(self.entry.get())
            if s.count(".")==0:
                self.entry.insert(END,num)
        else:
             self.entry.insert(END,num)

    def delFunc(self,n):
        s=list(self.entry.get())
        if len(s)>0:
            del s[len(s)-1]
        self.entry.delete(0,END)
        for i in s:
            self.entry.insert(END,i)

    def korFunc(self,n):
        tn=self.entry.get()
        if tn!="" and self.is_digit(tn):
            s=float(self.entry.get())
            if s>=0:
                s=math.sqrt(s)
                self.entry.delete(0,END)
                self.entry.insert(END,s)
    
    def calcFunc(self,op):
        global n1,oper
        oper=op
        tn1=self.entry.get()
        if tn1!="" and self.is_digit(tn1):
            n1=float(self.entry.get())
            self.entry.delete(0,END)

    def rezFunc(self,n):
        global n1
        tn2=self.entry.get()
        if tn2!="" and self.is_digit(tn2):
            n2=float(self.entry.get())
            if oper=="+":
                r=n1+n2
                self.entry.delete(0,END)
                self.entry.insert(END,r)
            if oper=="-":
                r=n1-n2
                self.entry.delete(0,END)
                self.entry.insert(END,r)
            if oper=="*":
                r=n1*n2
                self.entry.delete(0,END)
                self.entry.insert(END,r)
            if oper=="/":
                if n2>0:
                    r=n1/n2
                    self.entry.delete(0,END)
                    self.entry.insert(END,r)
                else:
                    r=0
            self.n1=r

def main():
    root = Tk()
    app=Example()
    root.mainloop()

if __name__ == "__main__":
    main()












