from turtle import *

speed(3)
hideturtle()
width(4)
bgcolor('white')

def rel_pos(x,y):
    penup()
    goto(pos()+(x,y))
    pendown()

def draw_roof():
    width(8)
    begin_fill()
    fillcolor("grey")
    seth(180)
    forward(200)
    seth(-120)
    forward(100)
    seth(0)
    forward(200)
    end_fill()
    seth(60)
    forward(100)
    seth(-60)
    forward(100)
    width(4)
    seth(180)
    forward(100)

def draw_walls(color):
    fillcolor('green')
    begin_fill()
    seth(-90)
    forward(120)
    seth(180)
    forward(200)
    seth(90)
    forward(120)
    seth(0)
    forward(300)
    seth(-90)
    forward(120)
    seth(180)
    forward(100)
    end_fill()

def draw_door():
    color('brown')
    width(5)
    forward(80)
    begin_fill()
    fillcolor('orange')
    seth(90)
    forward(80)
    seth(180)
    forward(40)
    seth(-90)
    forward(80)
    end_fill()
    rel_pos(25,40)
    width(4)
    circle(5)

def draw_windows():
    begin_fill()
    color('darkblue')
    fillcolor('#336699')
    seth(-90)
    width(5)
    forward(15)
    seth(180)
    forward(30)
    seth(90)
    forward(30)
    seth(0)
    forward(30)
    seth(-90)
    forward(15)
    end_fill()
    width(2)
    seth(180)
    forward(30)
    backward(15)
    seth(90)
    forward(15)
    backward(30)

def draw_text():
    speed(5)
    color('black')
    write('House Design by Sendy' , font=('Arial', 20, 'bold'))

def draw_house():    
    draw_roof()
    draw_walls(color)
    draw_door()
    rel_pos(-50, 0)
    draw_windows()
    rel_pos(135, 15)
    draw_windows()
    rel_pos(105, 25)
    draw_windows()
    rel_pos(-250,250)
    draw_text()
    done()

draw_house()