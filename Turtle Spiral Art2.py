import turtle

list1 = ['red', 'green', 'purple', 'orange', 'blue']
t=turtle
turtle.bgcolor('black')

for x in range(200):
    t.color(list1[x%5])
    t.pensize(x/20+1)
    t.forward(x)
    t.left(59)

t.hideturtle()