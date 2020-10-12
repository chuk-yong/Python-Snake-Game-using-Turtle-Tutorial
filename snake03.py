import turtle

# Setup the screen
scr = turtle.Screen()
scr.bgcolor("#33cccc")
scr.setup(600,600)
scr.title("Snake Game")

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup() # do not draw line
head.direction = "right"

# Functions for moving snake
def move():
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Game loop
while True:
    scr.update()
    move()

scr.mainloop()

# turtle.Screen().exitonclick()