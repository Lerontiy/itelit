from tkinter import *
from random import *
from math import *

rtg = str(round(pi, 2))
text = "0"


def doriv():
    global text, rez

    text += " "
    
    if "^" in text: 
        text = text.replace("^", "**")
        
    if "√" in text:
        digitNums = ""
        for i in text:
            if i == "√" or "√" in digitNums:
                if i == "" or i == " ":
                    text = text.replace(digitNums, f"{sqrt(int(digitNums))}")
                    digitNums = ""
                else:
                    digitNums += i
            text = text.replace(text[text.index("√")], " ")

    if "sin" in text:
        digitNums = ""
        q = 0
        for i in text:
            if i == "(" and text[q-1] == "n":
                text = text.replace(digitNums,f"sqrt({digitNums})")
                digitNums = ""
            else:
                q += 1
                digitNums += i

    if text.endswith(" / ") or text.endswith(" * "):
        text += "1"
    elif text.endswith(" + ") or text.endswith(" - "):
        text += "0"
    try:
        rez = eval(text)
    except:
        lab1["text"] = "Error"
        text = "0"
    if rez % 1 == 0:
        rez = int(rez)
    else:
        rez = round(rez, 5)
    rez = str(rez)
    text = rez
    lab1["text"] = rez


def uber():
    global text
    if text.endswith(" "):
        text = text[:len(text)-3]
    else:
        text = text[:len(text)-1]
        if text == "":
            text = "0"
    lab1["text"] = text


def ac():
    global text
    text = "0"
    lab1["text"] = text


def oper_func(oper):
    global text
    if oper not in text and not text.endswith(" "):
        text += oper
    if text.endswith(" "):
        text = text[:len(text)-3]
        text += oper
    else:
        doriv()
        text += oper
    lab1["text"] = text


def num_func(num):
    global text
    if text == "0":
        text = ""
    text += num
    if len(text) > 12:
        scal = Scale(root, orient=VERTICAL, length=300, from_=0, to=100, resolution=1)
        text += "\n"
    lab1["text"] = text


def tochka():
    global text
    if " " in text and text.count(".") < 2:
        text += "."
    if "." not in text:
        text += "."
    lab1["text"] = text


def kvad():
    global text
    if not text.endswith("^"):
        text += "^"
    lab1["text"] = text


def kor():
    global text
    if text == "0":
        text = ""
    text += "√"
    lab1["text"] = text


def sin():
    global text
    if text == "0":
        text = ""
    text += "sin("
    lab1["text"] = text


def lubof():
    colours = ["red", "orange", "yellow", "green", "light blue", "blue", "purple"]
    but_lub["bg"] = choice(colours)


root = Tk()
root.title("Калькулятор")
root.config(bg="lightgray", bd=5)
#root.geometry("280x415+250+100")

#рядок
lab1 = Label(root, text=text, bg="lightgray", fg="black", font="Calibri 25 bold")
lab1.grid(row=0, column=0, columnspan=4, padx=1, pady=5, sticky=E+S)
#(
but_lefDuzh = Button(root, text="(", command=lambda n="(": num_func(n), height=2, width=7)
but_lefDuzh.grid(row=1, column=2, padx=1, pady=1)
#)
but_righDuzh = Button(root, text=")", command=lambda n=")": num_func(n), height=2, width=7)
but_righDuzh.grid(row=1, column=3, padx=1, pady=1)
#/
but_dil = Button(root, text="/", command=lambda n=" / ": oper_func(n), height=2, width=7)
but_dil.grid(row=2, column=3, padx=1, pady=1)
#*
but_mnozh = Button(root, text="*", command=lambda n=" * ": oper_func(n), height=2, width=7)
but_mnozh.grid(row=3, column=3, padx=1, pady=1)
#-
but_minus = Button(root, text="-", command=lambda n=" - ": oper_func(n), height=2, width=7)
but_minus.grid(row=4, column=3, padx=1, pady=1)
#+
but_plus = Button(root, text="+", command=lambda n=" + ": oper_func(n), height=2, width=7)
but_plus.grid(row=5, column=3, padx=1, pady=1)
#=
but_doriv = Button(root, text="=", command=doriv, height=2, width=7)
but_doriv.grid(row=6, column=3, padx=1, pady=1)
#1
but_1 = Button(root, text="1", bg="white", command=lambda n="1": num_func(n), height=2, width=7)
but_1.grid(row=5, column=0, padx=1, pady=1)
#2
but_2 = Button(root, text="2", bg="white", command=lambda n="2": num_func(n), height=2, width=7)
but_2.grid(row=5, column=1, padx=1, pady=1)
#3
but_3 = Button(root, text="3", bg="white", command=lambda n="3": num_func(n), height=2, width=7)
but_3.grid(row=5, column=2, padx=1, pady=1)
#4
but_4 = Button(root, text="4", bg="white", command=lambda n="4": num_func(n), height=2, width=7)
but_4.grid(row=4, column=0, padx=1, pady=1)
#5
but_5 = Button(root, text="5", bg="white", command=lambda n="5": num_func(n), height=2, width=7)
but_5.grid(row=4, column=1, padx=1, pady=1)
#6
but_6 = Button(root, text="6", bg="white", command=lambda n="6": num_func(n), height=2, width=7)
but_6.grid(row=4, column=2, padx=1, pady=1)
#7
but_7 = Button(root, text="7", bg="white", command=lambda n="7": num_func(n), height=2, width=7)
but_7.grid(row=3, column=0, padx=1, pady=1)
#8
but_8 = Button(root, text="8", bg="white", command=lambda n="8": num_func(n), height=2, width=7)
but_8.grid(row=3, column=1, padx=1, pady=1)
#9
but_9 = Button(root, text="9", bg="white", command=lambda n="9": num_func(n), height=2, width=7)
but_9.grid(row=3, column=2, padx=1, pady=1)
#0
but_0 = Button(root, text="0", bg="white", command=lambda n="0": num_func(n), height=2, width=7)
but_0.grid(row=6, column=1, padx=1, pady=1)
#.
but_tochka = Button(root, text=".", bg="white", command=tochka, height=2, width=7)
but_tochka.grid(row=6, column=2, padx=1, pady=1)
#<3
but_lub = Button(root, text="<3", command=lubof, bg="#f0f0f0", height=2, width=7)
but_lub.grid(row=6, column=0, padx=1, pady=1)
#<-
but_uber = Button(root, text="<-", command=uber, height=2, width=7)
but_uber.grid(row=1, column=1, padx=1, pady=1)
#AC
but_ac = Button(root, text="AC", command=ac, height=2, width=7)
but_ac.grid(row=1, column=0, padx=1, pady=1)
#kvad
but_kvad = Button(root, text="xⁿ", command=kvad, height=2, width=7)
but_kvad.grid(row=2, column=2, padx=1, pady=1)
#kor
but_kor = Button(root, text="√", command=lambda n="√": num_func(n), height=2, width=7)
but_kor.grid(row=2, column=1, padx=1, pady=1)
#pi
but_pi = Button(root, text="π", command=lambda n=rtg: num_func(n), height=2, width=7)
but_pi.grid(row=2, column=0)

mainloop()
