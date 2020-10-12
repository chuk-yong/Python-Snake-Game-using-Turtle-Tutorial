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

turtle.Screen().exitonclick()