from tkinter import *
from random import *

y1 = 100
y2 = 100
xShar = 300
yShar = 100
up = [1, -1]
bobX1 = choice(up)
bobY1 = choice(up)
score1 = 0
score2 = 0

def move1(ev1):
    global y1
    if ev1.keysym == "w" and y1 > 0:
        y1-= up[0]*10
    if ev1.keysym == "s" and y1 < 250:
        y1+= up[0]*10
    player1.place(x= 0, y= y1, height= 50)
    
def move2(ev2):
    global y2
    if ev2.keysym == "Up" and y2 > 0:
        y2-= up[0]*10
    if ev2.keysym == "Down" and y2 < 250:
        y2+= up[0]*10
    player2.place(x= 590, y= y2, height= 50)

root = Tk()
root.geometry("600x300")
lab = Label(root, bg= "green")
lab.place(x= 0, y= 0, width= 600, height= 300)


player1 = Button(root, bg= "#fff000")
player1.place(x= 0, y= y1, height= 50)
player1.bind_all("<KeyPress-w>", move1)
player1.bind_all("<KeyPress-s>", move1)

player2 = Button(root, bg= "#fff000")
player2.place(x= 590, y= y2, height= 50)
player2.bind_all("<KeyPress-Up>", move2)
player2.bind_all("<KeyPress-Down>", move2)

shar = Button(root, bg= "#fff000")
shar.place(x= xShar, y= yShar, height= 10, width= 10)

lab1 = Label(text = score1, bg = "green")
lab1.place(x= 20, y= 10)

lab2 = Label(text = score2, bg = "green")
lab2.place(x= 570, y= 10)

def go():
    global xShar, yShar, bobX1, bobY1, y1, y2, score1, score2
    xShar+= bobX1
    yShar+= bobY1
    
    if yShar in range(y2,y2 + 50) and xShar in range (580, 590):
        bobX1 = -up[0]
    elif yShar in range(y1,y1 + 50) and xShar in range (0, 10):
        bobX1 = up[0]
    
    if yShar == 0:
        bobY1 = up[0]
    elif yShar == 290:
        bobY1 = -up[0]
    
    if xShar > 590 or xShar < 0:
        if xShar > 590:
            score1+= 1
            lab1["text"] = score1
        elif xShar < 10:
            score2+= 1
            lab2["text"] = score2
        xShar = 300
        yShar = 100
    shar.place(x= xShar, y= yShar, height= 10, width= 10)
    root.after(10,go)
go()

root.mainloop()