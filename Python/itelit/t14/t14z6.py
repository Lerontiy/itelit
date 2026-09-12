from tkinter import *

def vyb1():
    lab1["text"]="Червоний"
    lab1["bg"]="red"
    frame1["bg"]="red"

def vyb2():
    lab1["text"]="Синій"
    lab1["bg"]="blue"
    frame1["bg"]="blue"

def vyb3():
    lab2["text"]="Завершено!"

root=Tk()
root.title("Вікно з Фреймами")
root.geometry("300x400+300+250")


frame1=Frame(root,bg="blue",bd="40")
frame2=Frame(root,bg="green",bd="40")
frame1.pack()
frame2.pack()


but1=Button(frame1,text="Червоний",width="20",command=vyb1)
but1.pack()
but2=Button(frame1,text="Синій",width="20",command=vyb2)
but2.pack()

lab1=Label(frame1,text="Синій",bg="blue",fg="yellow",font="Arial 12 bold")
lab1.pack()


but3=Button(frame2,text="Завершити роботу",width="20",command=vyb3)
but3.pack()

lab2=Label(frame2,text="Робота",bg="green",fg="yellow",font="Arial 12 bold")
lab2.pack()



def vyb4():
    lab3["text"]="Червоний"
    lab3["bg"]="red"
    frame3["bg"]="red"

def vyb5():
    lab3["text"]="Синій"
    lab3["bg"]="blue"
    frame3["bg"]="blue"

def vyb6():
    lab4["text"]="Завершено!"

root1=Tk()
root1.title("Вікно з Фреймами1")
root1.geometry("300x400+300+250")


frame3=Frame(root1,bg="blue",bd="40")
frame4=Frame(root1,bg="green",bd="40")
frame3.pack()
frame4.pack()


but4=Button(frame3,text="Червоний",width="20",command=vyb4)
but4.pack()
but5=Button(frame3,text="Синій",width="20",command=vyb5)
but5.pack()

lab3=Label(frame3,text="Синій",bg="blue",fg="yellow",font="Arial 12 bold")
lab3.pack()


but6=Button(frame4,text="Завершити роботу",width="20",command=vyb6)
but6.pack()

lab4=Label(frame4,text="Робота",bg="green",fg="yellow",font="Arial 12 bold")
lab4.pack()

root.mainloop()
root1.mainloop()









































