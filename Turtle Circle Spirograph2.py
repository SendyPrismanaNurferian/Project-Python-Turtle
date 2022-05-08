import turtle

turtle.bgcolor('black')
turtle.speed()
turtle.pensize(2)
turtle.pencolor("white")

def drawcircle(radius):
    for i in range(10):
        turtle.circle(radius)
        radius=radius-4

def drawdesign():
    for i in range(101):
        drawcircle(150)
        turtle.right(36)

drawdesign()
turtle.done()

