from turtle import *
from random import randint
bgcolor("black")

h=1
shape("turtle")

while h<400:
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    colormode(255)
    pencolor(r,g,b)
    forward(5+h)
    right(90.99)
    h=h+1
exitonclick()   