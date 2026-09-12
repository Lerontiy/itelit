from tkinter import *
root = Tk()
root.title("Графіка в Python")
root.config (width=400, height=300, bg= "yellow",
             relief=RAISED, bd=10)
but=Button(root,text="Виконати", bg="blue",
           width="10", font="12", fg="white").place(x=15,y=15)
root.mainloop()
