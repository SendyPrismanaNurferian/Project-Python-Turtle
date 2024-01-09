# Turtle Game using the package 'turtle'! by Sendy-2023
# Importing relevant modules and packages to develop the game
import turtle
import random # Python has a built-in module to make random numbers, and we make to random the position of the player winner.
import time
from tkinter import messagebox # to pop up a message box who is the winner of the game

# setting up the game screen and the name of the game
def display_title():
    title_pen = turtle.Turtle()
    title_pen.color('black')
    title_pen.penup()
    title_pen.hideturtle()
    title_pen.goto(0, 50)
    title_pen.write("Turtle Race Game by Sendy", align="center", font=("Arial", 24, "bold"))
    title_pen.goto(0, 0)
    title_pen.write("Who's the WINNER?", align="center", font=("Arial", 16, "normal"))
# Setting up a nice screen for our game!
screen = turtle.Screen()
screen.bgcolor('green')
screen.title("Turtle Race Game")
display_title()

# We want two players in this game and the idea is that whoever and gets to the other side wins!

# We want two players and we can make names to the all players in this game
def get_player_names():
    player_one_name = turtle.textinput("Player One", "Enter Player One's Name:") # player one name
    player_two_name = turtle.textinput("Player Two", "Enter Player Two's Name:") # player two name
    return player_one_name, player_two_name # this is class of name the players to get the players winner names

# this function to draw the finish line
def draw_finish_line():
    finish_line = turtle.Turtle()
    finish_line.penup()
    finish_line.goto(300, 250)
    finish_line.pendown()
    finish_line.color('black')
    finish_line.goto(300, -250)
    finish_line.write('Finish!', align='center', font=('Arial', 16, 'normal'))

# This is the values for the die roll function
die = [1, 2, 3, 4, 5, 6]

# let's create the game!!
def start_race(player_one_name, player_two_name):
    draw_finish_line()
    # player one
    player_one_label = turtle.Turtle()
    player_one_label.color('black')
    player_one_label.penup()
    player_one_label.hideturtle()
    player_one_label.goto(-300, 250)
    player_one_label.write(f"{player_one_name}", align="center", font=("Arial", 10, "normal"))
    player_one = turtle.Turtle()
    player_one.color('red')
    player_one.shape('turtle')
    player_one.penup()
    player_one.goto(-300, 200)
    player_one.pendown()
    # player two
    player_two_label = turtle.Turtle()
    player_two_label.color('black')
    player_two_label.penup()
    player_two_label.hideturtle()
    player_two_label.goto(-300, -250)
    player_two_label.write(f"{player_two_name}", align="center", font=("Arial", 10, "normal"))
    player_two = player_one.clone()
    player_two.color('blue')
    player_two.penup()
    player_two.goto(-300, -200)
    player_two.pendown()
# This is function to make the players to move
    while True:
        if player_one.xcor() >= 300:
            messagebox.showinfo("Winner!", f"{player_one_name} Wins the Race!")
            break
        elif player_two.xcor() >= 300:
            messagebox.showinfo("Winner!", f"{player_two_name} Wins the Race!")
            break
        else:
            die_roll = random.choice(die)
            player_one.forward(30 * die_roll)
            time.sleep(1)
            die_roll2 = random.choice(die)
            player_two.forward(30 * die_roll2)
            time.sleep(1)
# # This is the main function to run the game
# player_one_name, player_two_name = get_player_names()
# start_race(player_one_name, player_two_name)
# # This keeps track of the turtle drawing on the screen
# turtle.done()
def ask_play_again():
    response = messagebox.askquestion("Play Again", "Do you want to play again?")
    return response == 'yes'

# Function to reset the screen and set up for a new game
def reset_screen():
    turtle.resetscreen()  # Reset the screen and clear all drawings
    screen.bgcolor('white')  # Reset the background color
    display_title()  # Redraw the title

# Main function to run the game
def run_game():
    while True:
        player_one_name, player_two_name = get_player_names()
        reset_screen()  # Reset the screen before starting a new game
        start_race(player_one_name, player_two_name)

        response = messagebox.askquestion("Play Again", "Do you want to play again?")
        if response.lower(True) == 'no':
            break

run_game()
turtle.done()