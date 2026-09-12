import tkinter as tk
import random

colors = ['red', 'orange', 'yellow', 'green', 'lightblue', 'blue', 'purple']
created_balls = set()

tags_set = set()
for i in range(10):
    tags_set.add(str(i)+'b')

cou_del_balls = 0
c_w = c_h = 400
step_ball_x = step_ball_y = 1


class F:
    def __init__(self):
        pass


def go():
    global cou_del_balls
    if len(created_balls) < 10:
        for t in tags_set:
            if t not in created_balls:
                x = random.randint(50, 300)
                y = random.randint(50, 300)
                canvas.create_oval(x, y, x+50, y+50, fill=random.choice(colors), tags=t)
                print(canvas.create_oval(x, y, x+50, y+50, fill=random.choice(colors), tags=t))
                created_balls.add(t)
                root.title(f'Кульок на полі: {len(created_balls)}        Макс: {len(tags_set)}')
                canvas.tag_bind(t, '<Button-1>', lambda e=t: del_func(e, t))

                root.after(100, go)
                break
    else:
        root.title(f'Гра завершена. Ваш рахунок: {cou_del_balls}')


def del_func(event, tag):
    global cou_del_balls
    canvas.delete(tag)
    created_balls.remove(tag)
    root.title(f'Кульок на полі: {len(created_balls)}        Макс: {len(tags_set)}')
    cou_del_balls += 1


def motion():
    global c_w, c_h, created_balls, step_ball_x, step_ball_y

    for i in created_balls:
        canvas.move(i, step_ball_x, step_ball_y)
        if canvas.coords(i)[2] >= c_w or canvas.coords(i)[2] <= 50:
            step_ball_x *= -1
        if canvas.coords(i)[3] >= c_h or canvas.coords(i)[3] <= 50:
            step_ball_y *= -1

    root.after(5, motion)


root = tk.Tk()

canvas = tk.Canvas(root, width=c_w, height=c_h, bg='white')
canvas.pack()

go()
motion()

root.mainloop()
