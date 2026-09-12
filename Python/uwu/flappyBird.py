from tkinter import *
from random import *
import time

w = 200
upd = 50
h = randint(10, 290)
xBar = 500

def ptashDown():
    global w, upd
    w+= 5
    Ptash.place(x= 150, y= w, width= 20, height= 20)
    root.after(upd, ptashDown)
def updateUpd():
    global upd
    upd = 3
def ptashUp(s):
    global w, upd
    upd = 50
    if s.keysym == "space":
        if w > 10:
            for i in range(5):
                w-= 8
        Ptash.place(x= 150, y= w, width= 20, height= 20)
    #root.after(1200, updateUpd)
def moveBarier():
    global xBar
    xBar-= 5
    b11.place(x= xBar, y= 0, width= 40, height= h)
    b12.place(x= xBar, y= h+100, width= 40, height= 300-h)
    root.after(50, moveBarier)
    
root = Tk()
root.geometry("600x400")

Ptash = Button(root, bg= "#fff000")
Ptash.place(x= 150, y= w, width= 20, height= 20)
Ptash['state'] = 'disabled'
Ptash.bind_all("<KeyPress-space>", ptashUp)

b11 = Button(root, bg= "#000fff")
b12 = Button(root, bg= "#000fff")
b11.place(x= 550, y= 0, width= 40, height= h)
b12.place(x= 550, y= h+100, width= 40, height= 300-h)

moveBarier()
ptashDown()

root.mainloop()






