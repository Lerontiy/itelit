from tkinter import *
#канвас
canvas = Canvas( width=600, height=600, bg="dark gray" )
#стіна
canvas.create_rectangle( (150,280), (450,501), fill="#800000", outline="black" )
#двері
canvas.create_rectangle( (350,350), (440,500), fill="dark green", outline="black" )
#ручка
canvas.create_oval( (420,430), (430,440), fill="black" )
#вікно
canvas.create_rectangle( (200,340), (270,410), fill="white", outline="black" )
#перемички
canvas.create_line( (235,340), (235,410), width=2, fill="black" )
canvas.create_line( (200,375), (270,375), width=2, fill="black" )
#дах
canvas.create_polygon( (130,285), (300,150), (470,285), fill="gray", outline="black" )
#вікно на даху
canvas.create_oval( (280,190), (320,230), fill="white" )
#перемички на даху
canvas.create_line( (280,210), (320,210), width=1, fill="black" )
canvas.create_line( (300,190), (300,230), width=1, fill="black" )

canvas.pack()
