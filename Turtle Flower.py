from turtle import *
 
def fleur():
    for I in range(300):
        circle(190-I,90)
        left(90)
        circle(190-I,90)
        left(18)
        speed(10)

fleur()
mainloop(20)
