from turtle import *

#Background
bgcolor('gold')

#Screen
shape('turtle')
tracer(1)

up()
goto(0,0)
down()

for i in range(2):
    fd(150)
    rt(90)
    fd(80)
    rt(90)

#Bendera Indonesia = Merah
color('red')
speed(20)
for i in range(20):
    fd(150)
    rt(90)
    fd(1)
    rt(90)
    fd(150)
    lt(90)
    fd(1)
    lt(90)

#Bendera Indonesia = Putih
color('white')
for i in range(20):
    fd(150)
    rt(90)
    fd(1)
    rt(90)
    fd(150)
    lt(90)
    fd(1)
    lt(90)

#Teks Indonesia
up()
goto(0,0)
colors = ('white')
write('Indonesia', font=('Arial', 20, 'bold'))

#Execute Turtle
fd(150)
exitonclick()