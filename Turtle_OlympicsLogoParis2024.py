import turtle

# Initialize the turtle
screen = turtle.Screen()
screen.title("Paris 2024 Olympics Logo")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(5)  # Fastest drawing speed
t.hideturtle()

# Function to draw a filled circle
def draw_circle(color, radius, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Function to draw the flame
def draw_flame():
    t.penup()
    t.goto(0, 200)
    t.setheading(0)
    t.pendown()
    t.color("gold")
    t.begin_fill()

    # Drawing the flame shape
    t.right(90)
    t.circle(100, 180)  # Bottom of the flame
    t.circle(50, 180)   # Top curve of the flame
    t.left(90)
    t.forward(100)
    t.end_fill()

# Function to draw the face
def draw_face():
    # Draw eyes
    t.penup()
    t.goto(-20, 130)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(7)
    t.end_fill()

    t.penup()
    t.goto(20, 130)
    t.pendown()
    t.begin_fill()
    t.circle(7)
    t.end_fill()

    # Draw mouth
    t.penup()
    t.goto(-10, 100)
    t.pendown()
    t.right(90)
    t.color("white")
    t.width(2)
    t.circle(10, 180)
    t.width(1)

# Function to draw the text "PARIS 2024"
def draw_text():
    t.speed(5)
    t.penup()
    t.goto(-165, 30)
    t.pendown()
    t.color("black")
    t.write("PARIS 2024", font=("Arial", 36, "bold"))

# Function to draw the Olympic rings
def draw_rings():
    ring_colors = ["blue", "black", "red", "yellow", "green"]
    ring_positions = [(-110, -40), (0, -40), (110, -40), (-55, -80), (55, -80)]
    
    t.width(5)

    for color, pos in zip(ring_colors, ring_positions):
        t.penup()
        t.goto(pos)
        t.pendown()
        t.color(color)
        t.circle(40)

    t.width(1)

# Tambahkan teks "Olympics Logo by Sendy"
    turtle.penup()
    turtle.goto(-50, -160)
    turtle.pendown()
    turtle.write("Paris 2024 Olympics Logo by Sendy", align="center", font=("Arial", 12, "normal"))

# Function to quit the program when 'q' is pressed
def quit_program():
    screen.bye()  # Closes the turtle graphics window

# Bind the 'q' key to the quit function
screen.listen()  # Set the window to listen for key presses
screen.onkey(quit_program, "q")  # Bind 'q' key to quit the program

# Drawing the logo step-by-step
draw_flame()
draw_face()
draw_text()
draw_rings()

# Keep the window open until closed by user or by pressing 'q'
turtle.done()
