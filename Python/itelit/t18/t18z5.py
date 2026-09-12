import tkinter as tk
import random
import time

colors = ['red', 'orange', 'yellow', 'green', 'lightblue', 'blue', 'purple']


def create_oval():
    while True:
        x = random.randint(-50, 400)
        y = random.randint(-50, 400)
        size = random.randint(1, 150)
        canvas.create_oval(x, y, x+size, y+size, tags="ball", fill=random.choice(colors))
        time.sleep(0.5)
        root.update()


root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=500, bg='white')
canvas.pack()

create_oval()
