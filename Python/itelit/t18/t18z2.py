from tkinter import *
root = Tk()
root.title("Вікно полотна")

c = Canvas(root, width=200, height=200, bg='white')
c.pack()

#сонечко
c.create_oval((150, 20), (180, 50), fill='orange', outline='orange')

#дім
c.create_line((100, 180), (100, 50), width=100, fill='lightblue', arrow=LAST, arrowshape=[50, 50, 20])

#трава
step_grass = -40
while step_grass < 200:
    c.create_arc((step_grass, 400), (step_grass+40, 170), width=2, start=160, extent=-70, style=ARC, outline='green')
    step_grass += 10

root.mainloop()
