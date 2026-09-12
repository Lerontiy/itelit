from tkinter import *
import random
import statistics

space_size = 25
rootWidth = 300
rootHeight = 500
now_moving = 'потом создастся'
x_coords = 'потом создастся'
y_coords = 'потом создастся'


class Figures:
    def __init__(self, *coords, fill='white', name):
        self.fill = fill
        self.name = name
        self.coords_of_facets_prot = coords
        self.coords_of_facets = list()

        self.create()

    def create(self):
        global space_size
        for i in range(0, len(self.coords_of_facets_prot), 2):
            self.coords_of_facets.append(self.coords_of_facets_prot[i] * space_size)
            self.coords_of_facets.append(self.coords_of_facets_prot[i+1] * space_size)

        self.name = canvas.create_polygon(self.coords_of_facets, fill=self.fill, outline='black')


def figures():
    global now_moving, y_coords

#   https://ravesli.com/wp-content/uploads/2019/10/7_1.png
    o = Figures(0, 0, 2, 0, 2, 2, 0, 2, 0, 0, fill='yellow', name='o')
    i = Figures(1, 0, 1, 4, 0, 4, 0, 0, fill='blue', name='i')
    s = Figures(0, 1, 1, 1, 1, 0, 3, 0, 3, 1, 2, 1, 2, 2, 0, 2, 0, 1, fill='red', name='s')
    z = Figures(0, 0, 2, 0, 2, 1, 3, 1, 3, 2, 1, 2, 1, 1, 0, 1, 0, 0, fill='green', name='z')
    l = Figures(0, 0, 1, 0, 1, 2, 2, 2, 2, 3, 0, 3, 0, 0, fill='orange', name='l')
    j = Figures(1, 0, 2, 0, 2, 3, 0, 3, 0, 2, 1, 2, 1, 0, fill='pink', name='j')
    t = Figures(0, 0, 3, 0, 3, 1, 2, 1, 2, 2, 1, 2, 1, 1, 0, 1, 0, 0, fill='purple', name='t')

    d = [o.name, i.name, s.name, z.name, l.name, j.name, t.name]
    for i in d:
        canvas.move(i, 1000, 0)
    now_moving = random.choice(d)
    canvas.move(now_moving, -925, 0)

    del d, o, i, s, z, l, j, t

    move()


def x_y_coords():
    global y_coords, x_coords, now_moving

    x_coords = set()
    y_coords = set()

    for i in range(0, len(canvas.coords(now_moving)), 2):
        x_coords.add(canvas.coords(now_moving)[i])
        y_coords.add(canvas.coords(now_moving)[i+1])


def move():
    global space_size, rootHeight, now_moving, y_coords

    x_y_coords()

    if max(y_coords) < rootHeight:
        canvas.move(now_moving, 0, space_size)
        root.after(1000, move)
    else:
        figures()


def else_move(event):
    global space_size, now_moving, x_coords, rootWidth, l_wall, r_wall

    x_y_coords()

    if event.keysym == 'Left' and min(x_coords) > (canvas.coords(l_wall)[0] + space_size):
        canvas.move(now_moving, -space_size, 0)
    elif event.keysym == 'Right' and max(x_coords) < (canvas.coords(r_wall)[2] - space_size):
        canvas.move(now_moving, space_size, 0)
    elif event.keysym == 'Up':
        up_move()


def up_move(event):
    global now_moving, x_coords, y_coords

    x_y_coords()

    xs = round(statistics.mean(x_coords))
    ys = round(statistics.mean(y_coords))
    while xs % 25 != 0:
        xs += 1
    while ys % 25 != 0:
        ys += 1
    coords_of_coords = list()
    new_coords_of_coords = list()
    new_coords = canvas.coords(now_moving)
    for i in range(0, len(canvas.coords(now_moving)), 2):
        coords_of_coords.append(canvas.coords(now_moving)[i] - xs)
        coords_of_coords.append(canvas.coords(now_moving)[i+1] - ys)

        new_coords[i] = (new_coords[i] - coords_of_coords[i])
        new_coords[i+1] = (new_coords[i+1] - coords_of_coords[i+1])

        new_coords_of_coords.append(coords_of_coords[i+1])
        new_coords_of_coords.append(coords_of_coords[i]*-1)

        new_coords[i] = (new_coords[i] + new_coords_of_coords[i])
        new_coords[i+1] = (new_coords[i+1] + new_coords_of_coords[i+1])

    canvas.coords(now_moving, new_coords)


root = Tk()
root.config()

canvas = Canvas(root, height=rootHeight, width=rootWidth, bg="white")
canvas.pack(anchor="w")
l_wall = canvas.create_rectangle((0, 0), (space_size, rootHeight), fill="black")
r_wall = canvas.create_rectangle((rootWidth - space_size, 0), (rootWidth, rootHeight), fill="black")

root.bind('<Left>', else_move)
root.bind('<Right>', else_move)
root.bind('<Up>', up_move)

figures()

root.mainloop()
