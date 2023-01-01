import turtle
import time

jam_count = 0
menit_count = 0
second_count = 0


t = turtle.Turtle()
t.pencolor("White")
s = turtle.Screen()
s.title("StopWatch by Send")
s.bgcolor("Black")
t.hideturtle()
t.speed(0)

def layout(jam_count, menit_count, second_count):
    t.clear()
    t.penup()
    t.pensize(3)
    t.goto(-120, 100)
    t.pencolor("White")
    t.write("STOP WATCH BY SEND", font=25)
    t.goto(-100, 40)
    t.pendown()
    for i in range(2):
        t.forward(140)
        t.right(90)
        t.forward(55)
        t.right(90)
    t.penup()
    t.pencolor("White")
    t.goto(-70, 25)
    t.write("hh")
    t.goto(-70, 0)
    t.pendown()
    t.write(jam_count, font=25)
    t.penup()
    t.goto(-45, 0)
    t.pendown()
    t.write(":", font=25)
    t.penup()
    t.goto(-35, 25)
    t.write("mm")
    t.goto(-35, 0)
    t.pendown()

    t.write(menit_count, font=25)
    t.penup()
    t.goto(-5,0)
    t.pendown()
    t.write(":", font=25)
    t.penup()
    t.goto(5, 25)
    t.write("ss")
    t.goto(5, 0)
    t.pendown()
    t.write(second_count, font=25)

def seconds(second_count, menit_count, jam_count):
    while True:
        second_count +=1
        time.sleep(1)
        t.undo()
        t.write(second_count, font=25)
        if second_count >=60:
            menit_count += 1
            second_count = 0
            layout(jam_count, menit_count, second_count)
        if menit_count >=60:
            jam_count += 1
            menit_count = 0
            layout(jam_count, menit_count, second_count)


layout(jam_count, menit_count, second_count)
seconds(jam_count, menit_count, second_count)
turtle.done()