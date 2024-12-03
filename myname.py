import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lavender")  # Light purple background
screen.title("Mily")

# Create and configure the turtle
pen = turtle.Turtle()
pen.speed(2)  # Set moderate speed for smooth animation
pen.pensize(5)
pen.color("#FF69B4")  # Hot pink color

# Position the turtle to start writing
pen.penup()
pen.goto(-100, 0)
pen.pendown()

# Configure text style
style = ("Times New Roman", 60, "bold")

# Write name with animation
name = "Mily"
for char in name:
    pen.color("#FF69B4")  # Hot pink color
    pen.write(char, font=style, move=True)
    time.sleep(0.5)  # Pause between each character
    pen.forward(10)  # Add some space between characters

# Hide the turtle and keep window open
pen.hideturtle()
screen.mainloop()
