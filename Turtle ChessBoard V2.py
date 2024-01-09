import turtle as tur

tur.penup()
tur.goto(-200, -200)
tur.pendown()
tur.speed()

# Create a square in cheesbox for black and white
def square(x):
    for a in range(4):
        tur.forward(x)
        tur.left(90)

size = 50
initPos = tur.pos()
for i in range(8):
    tur.penup()
    tur.goto(initPos+(0,size*i))
    tur.pendown()
    tur.seth(0)
    for j in range(8):
        color = 'black' if (i+j)%2 else 'white'
        tur.begin_fill()
        tur.fillcolor(color)
        square(size)
        tur.end_fill()
        tur.forward(size)

# Create the square for outline chessbox
tur.penup()
tur.goto(initPos)
tur.pendown()
tur.color('yellow')
tur.width(20)
tur.speed(0)
for b in range(4):
    tur.forward(size*8)
    tur.left(90)
tur.width(2)
tur.color('black')
for b in range(4):
    tur.forward(size*8)
    tur.left(90)
tur.hideturtle()

# Add text 
tur.penup()
tur.goto(-180, -250)  # Adjust position as needed
tur.pendown()
tur.write("Chessboard design Ver 2 by Sendy", align="left", font=("Arial", 12))

tur.done()