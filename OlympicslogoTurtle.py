# Author: Sendy 
import turtle
import sys

# Function to draw a single ring with the specified color and position
def draw_rings(color, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(60)

# Draw the Olympic rings logo
def main():
    turtle.speed(8)
    turtle.width(8)
    draw_rings("blue", -120, 0)
    draw_rings("black", 0, 0)
    draw_rings("red", 120, 0)
    draw_rings("yellow", -60, -50)
    draw_rings("green", 60, -50)
    turtle.hideturtle()

    # Tambahkan teks "Olympics Logo by Sendy"
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.write("Olympics Logo by Sendy", align="center", font=("Arial", 12, "normal"))

    # Menunggu sampai pengguna menekan tombol "q" dan "x" untuk keluar
    turtle.onkeypress(sys.exit, "q")
    turtle.onkeypress(sys.exit, "x")

    turtle.done()

if __name__ == "__main__":
    main()
