from tkinter import *

def stan():
    vyb1=var1.get()
    vyb2=var2.get()
    vyb3=var3.get()
    spys=[vyb1,vyb2,vyb3]
    listb.delete(0,2)
    for i in spys:
        listb.insert(END,i)
        
root=Tk()
root.title("Робота з прапорцями та списками")
root.geometry("300x400+300+250")
var1=StringVar()
var2=StringVar()
var3=StringVar()

prap1=Checkbutton(root,text="Перший",variable=var1,
                  onvalue="Перший - ON",offvalue="Перший - OFF")#
prap2=Checkbutton(root,text="Другий",variable=var2,
                  onvalue="Другий - ON",offvalue="Другий - OFF")#
prap3=Checkbutton(root,text="Третій",variable=var3,
                  onvalue="Третій - ON",offvalue="Третій - OFF")#

prap1.deselect()
prap2.deselect()
prap3.deselect()
prap1.pack()
prap2.pack()
prap3.pack()


listb=Listbox(root,bg="yellow",height="5")
listb.pack()


but=Button(root,text="Стан прапорців",command=stan)
but.pack()

root.mainloop()










