from tkinter import *
import time
import tkinter as tk
from tkinter import messagebox as msg
import random


# Assigning global variables
speed = 9
lap = 0
lap1 = 0
xvalue = 0
yvalue = 0
new = False

# Creating canvas
tk = Tk()
canvas = Canvas(tk,width = 900, height = 700,bg = '#262728',)
tk.title('RaceCarGame')
canvas.pack()

#Methods

def gamble(donut):
    global speed
    a = random.randint(0,1)
    if a == 0:
        speed += 2
    if a == 1:
        speed -= 2
    

def startt():
    tingy = msg.askyesno('Donut Game','Race the donut, if you win you get to eat it, but there is a chance while playing you will turn into a donut. Press t to gamble for higher speed!'
                         ' Would you like to play?')
    if tingy == True:
        tk.after(3500,automove)
    if tingy == False:
        exit()

def getwinner():
    global lap,lap1,speed,new,lap11
    bbox = canvas.bbox(cop)
    x1,y1,x2,y2= bbox[0],bbox[1],bbox[2],bbox[3]
    result = canvas.find_overlapping(x1,y1,x2,y2)
    if 5 in result:
        lap += 1
    if lap == 28:
        lap1=28
        thingy = msg.askyesno('Winner','You Won! Would you like to play again?')
        if thingy == True:
            new = True
            speed = 9
            lap = 0
            canvas.coords(cop,422,115)
            canvas.coords(donut,422,26)
            automove()
        elif thingy == False:
            exit()


def getwinner1():
    global lap,lap1,speed,new,lap11
    bbox = canvas.bbox(donut)
    x1,y1,x2,y2= bbox[0],bbox[1],bbox[2],bbox[3]
    result = canvas.find_overlapping(x1,y1,x2,y2) 
    if 5 in result:
        lap1 += 1
    if lap1 == 28:
        thingy = msg.askyesno('Loser','You Lost! Would you like to play again?')
        if thingy == True:
            new = True
            speed = 9
            lap = 0
            lap1= 0
            canvas.coords(cop,422,115)
            canvas.coords(donut,422,26)
            tk.after(1500,automove)
        elif thingy == False:
            exit()


def automove():
    global lap1,new,lap11
    bbox = canvas.coords(donut)
    x1,y1 = bbox[0],bbox[1]
    if lap1 >27:
        if new == True:
            lap1=0
            tk.after(1500,automove)
            return
        if new == False:
            return
    elif lap1 < 28:
        new = False
        if x1<875 and y1<31:
            canvas.move(3,6,0)
            tk.after(77,automove)
            getwinner1()
        if x1>875 and y1<675:
            canvas.move(donut,0,6)
            tk.after(77,automove)
            getwinner1()
        if x1>25 and y1>665:
            canvas.move(donut,-6,0)
            tk.after(77,automove)
            getwinner1()
        if x1<25 and y1<675:
            canvas.move(donut,0,-6)
            tk.after(77,automove)
            getwinner1()


def crashMessage():
    msg.showinfo("Crash!", "You crashed!")



def checkCollision():
    global speed
    bbox = canvas.bbox(cop)
    x1,y1,x2,y2= bbox[0],bbox[1],bbox[2],bbox[3]
    result = canvas.find_overlapping(x1,y1,x2,y2)
    print (canvas.bbox(cop))
    print (result)
    
    if 1 in result :
        crashMessage()
        speed -= 1
        tk.mainloop()
    if 2 in result:
        crashMessage()
        speed -= 1
        tk.mainloop()
    if 3 in result:
        crashMessage()
        speed -= 1
        tk.mainloop()
    getwinner()


def moveobject(event):
    global speed
    bbox = canvas.coords(cop)
    x1,y1 = bbox[0],bbox[1]
    if speed == 0:
        canvas.itemconfig(cop,image=donut1)
        msg.showinfo("Crash!", "You are now a donut!")
        exit()
    if event.keysym == 'w':
        if y1>25:
            canvas.move(cop,0,-speed)
            checkCollision()
        canvas.itemconfig(cop,image = cop4)
    elif event.keysym == 's':
        if y1<700:
            canvas.move(cop,0,speed)
            checkCollision()
        canvas.itemconfig(cop,image = cop2)
    elif event.keysym == 'a':
        if x1>0:
            canvas.move(cop,-speed,0)
            checkCollision()
        canvas.itemconfig(cop,image = cop3)
    elif event.keysym == 'd':
        if x1<880:
            canvas.move(cop,speed,0)
            checkCollision()
        canvas.itemconfig(cop,image = cop1)
      


sprinkles1= PhotoImage(file='middle.png')
cop1 = PhotoImage(file='Copr.png')
cop2 = PhotoImage(file='Copd.png')
cop3 = PhotoImage(file='Copl.png')
cop4 = PhotoImage(file='copu.png')
donut1 = PhotoImage(file='donut.png')
middle = PhotoImage(file='middle.png')


canvas.create_rectangle(70, 70, 830, 638, dash=(3,5), width = 4, outline="yellow")
canvas.create_rectangle(140,150,760,570,fill = 'green')
donut = canvas.create_image(422,26,image=donut1)
cop = canvas.create_image(422,115,image=cop1)
canvas.create_rectangle(450,0,450,150,dash=(3,5),width=5,outline='white')#5
centerr = canvas.create_image(450,360,image=middle)

#tk.after(1500,automove)#turn this off after fixing start


canvas.bind_all('<KeyPress-w>',moveobject)
canvas.bind_all('<KeyPress-s>',moveobject)
canvas.bind_all('<KeyPress-a>',moveobject)
canvas.bind_all('<KeyPress-d>',moveobject)
canvas.bind_all('<KeyPress-t>',gamble)

startt()

tk.mainloop()