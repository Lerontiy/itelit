from tkinter import *

def stan():
    vyb=var.get()
    country=["Польща","Словаччина","Угорщина","Румунія","Молдова","Росія","Білорусь"]
    spys=[vyb]
    listb.delete(0,1)
    for i in spys:
        listb.insert(END,country[i-1])
        
root=Tk()
root.title("Робота з прапорцями та списками")
root.geometry("300x400+300+250")
var=IntVar()

radio1=Radiobutton(root,text="Польща",variable=var,value=1)
radio2=Radiobutton(root,text="Словаччина",variable=var,value=2)
radio3=Radiobutton(root,text="Угорщина",variable=var,value=3)
radio4=Radiobutton(root,text="Румунія",variable=var,value=4)
radio5=Radiobutton(root,text="Молдова",variable=var,value=5)
radio6=Radiobutton(root,text="Росія",variable=var,value=6)
radio7=Radiobutton(root,text="Білорусь",variable=var,value=7)

radio1.pack(anchor=W)
radio2.pack(anchor=W)
radio3.pack(anchor=W)
radio4.pack(anchor=W)
radio5.pack(anchor=W)
radio6.pack(anchor=W)
radio7.pack(anchor=W)


listb=Listbox(root,bg="yellow",height="5")
listb.pack()


but=Button(root,text="Стан прапорців",command=stan)
but.pack()

root.mainloop()










