from tkinter import *
from threading import Timer
import time


def light_func():
    while True:
        time.sleep(1)
        c.itemconfig(yellow_ball, fill='gray')
        c.itemconfig(red_ball, fill='red')
        time.sleep(4)
        c.itemconfig(yellow_ball, fill='yellow')
        time.sleep(2)
        c.itemconfig(red_ball, fill='gray')
        c.itemconfig(yellow_ball, fill='gray')
        c.itemconfig(green_ball, fill='green')
        time.sleep(3)
        c.itemconfig(green_ball, fill='gray')
        for i in range(2):
            time.sleep(1)
            c.itemconfig(green_ball, fill='green')
            time.sleep(1)
            c.itemconfig(green_ball, fill='gray')
        c.itemconfig(yellow_ball, fill='yellow')


root = Tk()
root.title("Світлофор")

c = Canvas(root, width=120, height=360, bg='aqua')
c.pack()

red_ball = c.create_oval((10, 10), (110, 110), fill='gray', outline='blue', width=2)
yellow_ball = c.create_oval((10, 120), (110, 220), fill='yellow', outline='blue', width=2)
green_ball = c.create_oval((10, 230), (110, 330), fill='gray', outline='blue', width=2)

t = Timer(0, light_func)
t.start()

root.mainloop()
