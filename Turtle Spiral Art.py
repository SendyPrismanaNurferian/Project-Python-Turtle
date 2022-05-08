import turtle

colors = ['red', 'green', 'yellow', 'purple', 'orange', 'blue', 'grey']
t=turtle
turtle.pen()
turtle.bgcolor('black')

for y in range(200):
    t.pencolor(colors[y%6])
    t.width(y/100+1)
    t.forward(y)
    t.left(57)

t.hideturtle()