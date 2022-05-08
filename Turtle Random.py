import turtle, random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(800,800)

winheight = 350

turd1 = Turtle('turtle')
turd2 = Turtle('turtle')
turd3 = Turtle('turtle')
turd4 = Turtle('turtle')
turd5 = Turtle('turtle')
turd6 = Turtle('turtle')
turd7 = Turtle('turtle')

turds = [turd1, turd2, turd3, turd4, turd5, turd6, turd7]

turd1.color('blue')
turd2.color('yellow')
turd3.color('green')
turd4.color('pink')
turd5.color('orange')
turd6.color('purple')
turd7.color('aqua')

for turd in turds:
    turd.pu()
    turd.lt(90)

turd1.setpos(-250, -300)
turd2.setpos(-250+(500/6), -300)
turd3.setpos(-250+2*(500/6), -300)
turd4.setpos(-250+3*(500/6), -300)
turd5.setpos(-250+4*(500/6), -300)
turd6.setpos(-250+5*(500/6), -300)
turd7.setpos(-250+6*(500/6), -300)

for turd in turds:
    turd.pd()

def move():
    for turd in turds:
        distance = random.randint(1, 50)
        turd.forward(distance)
        print(turd, turd.position())
        if turd.ycor() >= winheight:
            print(turd.color().upper(), ' has won!')
            return
    move()

move()

screen.mainloop()