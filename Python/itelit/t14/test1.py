from tkinter import *
root = Tk()
root.title("Вікно з дочірніми вікнами")
root.geometry("300x300+300+250")
top=Toplevel(root,relief=SUNKEN,width="300",height="100",bd="2",bg="green")
top.title("Перше додаткове вікно")
bottom=Toplevel(root,relief=SUNKEN,width="300",height="100",bd="2",bg="yellow")
bottom.title("Друге додаткове вікно")
mainloop()
