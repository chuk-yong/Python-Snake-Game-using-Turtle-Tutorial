import turtle
import time
import random

delay = 0.1

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
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup() # do not draw line
food.goto(0,150)

# Functions for moving snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Functions for direction
def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"

# keyboard binding
scr.listen()
scr.onkeypress(go_up, "Up")
scr.onkeypress(go_down,"Down")
scr.onkeypress(go_left,"Left")
scr.onkeypress(go_right,"Right")

# Game loop
while True:
    scr.update()
    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)
    move()
    time.sleep(delay)

scr.mainloop()

# turtle.Screen().exitonclick()