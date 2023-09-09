import tkinter as tk
import math
from tkinter import *
from tkinter import ttk
root = Tk()
choice="fill"
colour = "black"
screen = Canvas(root, width = 450, height = 400, bg = "white")
screen.pack()
screen.create_rectangle(375,50,425,100,fill = "black")
screen.create_rectangle(375,150,425,200,fill = "white",width=3)
screen.create_text(403,175,text="Change ",font=("Arial",9))
screen.create_rectangle(375,250,425,300,outline = "black",width=3)
screen.create_rectangle(375,300,425,350,outline = "black",width=3)
screen.create_text(403,325,text="Lines ",font=("Arial",9))
screen.create_rectangle(375,350,425,400,outline = "black",width=3)
screen.create_text(403,375,text="Lines off ",font=("Arial",8))
#lines
def lines(color):

    x=25
    y=25
    for i in range(0,14):
        screen.create_line(x,0,x,400,fill=color)
        x=x+25
    for i in range(0,16):
        screen.create_line(0,y,350,y,fill=color)
        y=y+25
mainloop()