from tkinter import *
def but():
    micto=entry.get()
    if micto=="Київ":
        lab["fg"]="green"
        lab["text"]="Вірно"
    elif micto=="":
        lab["fg"]="blue"
        lab["text"]="Треба ввести назву міста"
    else:
        lab["fg"]="red"
        lab["text"]="Спробуй ще"
    entry.delete(0,END)
root = Tk()
root.title("Назвіть столицю України")
root.geometry("400x300+300+250")
root.config()
lab=Label(root,text="Столиця України?",fg="black")
lab.pack()
entry=Entry(root,text="123")
entry.pack()
but=Button(root,text="Перевір",command=but)
but.pack()
root.mainloop()
