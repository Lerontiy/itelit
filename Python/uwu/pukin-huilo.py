from tkinter import *
from random import *


def hoverFun(self):
    root.geometry(f'300x300+{randint(100,win_width-400)}+{randint(100,win_height-400)}')


def yesFun():
    butYes.destroy()
    butNo.destroy()
    labMain["text"]="Слава Україні"

root = Tk()
win_height = root.winfo_screenheight()
win_width = root.winfo_screenwidth()
root.geometry(f'300x300+{randint(100,win_width-400)}+{randint(100,win_height-400)}')
root.config(padx=10,pady=10,bg="white")
#root.overrideredirect(1)

labMain = Label(root,text="Путин хуйло?",width="20",bg="white",font="Calibri 15")
butYes = Button(root,text="Конечно",width="10",bg="lightgray",command=yesFun)
butNo = Button(root,text="Нет",width="10",bg="lightgray")

#labMain.grid(row="0",column="0",columnspan="2",padx=10,pady=40)
#butYes.grid(row="1",column="0")
#butNo.grid(row="1",column="1")
labMain.pack(anchor="center")
butYes.place(x=30,y=100)
butNo.place(x=170,y=100)
butNo.bind("<Enter>",hoverFun)

root.mainloop()