from tkinter import *

root = Tk()

c_w = 1280
c_h = 720
c = Canvas(root, width=c_w, height=c_h, bg='white')
c.pack()

ball = c.create_oval((0, 0), (50, 50), fill='green')
step_ball_x = 1
step_ball_y = 1


def motion():
    global step_ball_x, step_ball_y, c_w, c_h

    c.move(ball, step_ball_x, step_ball_y)
    if c.coords(ball)[2] >= c_w or c.coords(ball)[2] <= 50:
        step_ball_x *= -1
    if c.coords(ball)[3] >= c_h or c.coords(ball)[3] <= 50:
        step_ball_y *= -1

    c.create_line([c.coords(ball)[2]-21, c.coords(ball)[3]-21, c.coords(ball)[2]-20, c.coords(ball)[3]-20], fill='red')

    root.after(5, motion)


motion()

root.mainloop()
