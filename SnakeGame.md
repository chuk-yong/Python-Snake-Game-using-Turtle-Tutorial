## Python Snake Game Using Turtle

This is a step-by-step guide to how I code this project by following the examples on: https://www.edureka.co/blog/python-turtle-module/ and this youtube tutorial: https://www.youtube.com/watch?v=BP7KMlbvtOo&list=PLlEgNdBJEO-n8k9SR49AshB9j7b5Iw7hZ&index=1

# Table of content:
1. [Setup the canvas](#canvas)
2. [Setup Head of Snake](#headofSnake)
3. [Moving the Snake](#moveSnake)
4. [Add Delay](#delay)
5. [Movement Control](#controlSnake)
6. [Food and Collision detection](#food&collision)
7. [Adding Snake body/segments](#segment)
8. [Border Collision](#borderCollision)
9. [Body Collision](#bodyCollision)
10. [Final. Score](#score)


<a name='canvas'></a>
## 1. Setting up the canvas
import Turle and then create the screen object.  
```
# Setup the screen
scr = turtle.Screen()
scr.bgcolor("#33cccc")
scr.setup(600,600)
scr.title("Snake Game")
```
If you run this, you will find the screen pops up and quickly closes. Add this line ``` turtle.Screen().exitonclick() ``` so that you can close it by clicking anywhere inside the screen.

Running snake01.py, this is what you will get:

![Canvas](./SnakeScreen-01.png)

<a name='headofSnake'></a>
## 2. Set up the head of the snake
```
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black"
```

Running snake02.py will show a small square in the middle of the canvas.  This is the head of our snake.

![Snake Head](./SnakeScreen-02.png)

<a name='moveSnake'></a>
## 3. Move the snake
I am going to define a function for this:
```
def move():
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
```
For now, I just want to test if this works.  There are 2 lines we need to add under # Snake Head.  First is:
```
head.penup()
```
We do not want to draw a line while the snake is moving.  Turtle is essentially a program to animate drawing.  By default, you will see a line when you move an object from one position to another. By calling the method penup(), we ask Turtle to 'lift' up the pen so that it will not follow the snake movement with a pen line.

Second being:
```
head.direction = "right"
```
We set the initial direction of the snake to go right.  So that the function mov() will be activated and set the snake to move 20 pixel to the right.

Now we do the fun part, adding a 'loop'. By looping, we create a sense of motion much like playing a film strip.
```
# Game loop
while True:
    scr.update()
    move()

scr.mainloop()
```
If you run snake03.py, you will see the snake run off the screen to the right.
![Snake Running to the right](./snakeScreen-03.png)

It's not very interesting but it shows that the code is running.

<a name='delay'></a>
## 4. Adding delay
Our snake is running too fast!  Let's add a little bit of delay or else our game would be unplayable.
```
import time
delay = 0.1
```
The time function let us accomplish that.  We will set our delay to 0.1s.

```
time.sleep(delay)
```
Add it to our game loop will slow each loop or "frame" by the delay we specified.

Now if you run snake04.py, you should see the small black square, representing the head of the snake, moving to the right and out of the canvas.

<a name='controlSnake'></a>
## 5. Moving the snake
Not that we understand the basic of how Turtle draw objects and redraw frames. We will start to assemble the control of movement.

Let's add a function called move():
```
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
```
To set head.direction, we define these four functions:
```
# Functions for direction
def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"
```
Now, to sense which direction to set, we will use Turtle's listen() method to listen for key press.  I am using the arrow keys, so:
```
# keyboard binding
scr.listen()
scr.onkeypress(go_up, "Up")
scr.onkeypress(go_down,"Down")
scr.onkeypress(go_left,"Left")
scr.onkeypress(go_right,"Right")
```
Remember to set head.direction = "stop". Else the snake will immediately move when you start the program.

Running snake05.py, you should be able to control the snake by moving the arrow keys.

<a name='food&collision'></a>
## 6. Adding Food and collision detection
To add Food, simply create another Turtle object:
```
# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup() # do not draw line
food.goto(0,150)
```
This will add Food, represented by a red circle 150 pixels on top of our snake.  You can change the position later.  

Now, to detect if they are close to each other, we can use the method in Turtle 's distance().
```
if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)
```
Here, once we detected that the snake head's distance to the food is less than 20 pixel, we will randomly generate a new co-ordinate and place the food there.  This will create an illusion that the snake ate the food and new food pops up immediately and randomly on the canvas.

We need to use the functions in random library, so add this to the beginning of the code:
```
import random
```
Run snake06.py and move your snake towards the food.  The food will 'disappear' and reappear somewhere else.

<a name='segment'></a>
## 7. Add snake segments and move
When the snake eats the food, its body will gain a segment.

Since we do not know how many segments we need to add, it is best to use a list.  This list will store the positions of the snake's body. 
```
seg = []
```
Next we use a function to add the segments.  Each segment is an Turtle object, it is square and grey in colour.
```
def add_seg():
    new_seg = turtle.Turtle()
    new_seg.speed(0)
    new_seg.shape("square")
    new_seg.color("grey")
    new_seg.penup()
    seg.append(new_seg)
```
For movement, here's something to think about.

If we move the head first and then each segment, you will see a gap.  So it is better to move the segments from last to first and then move the head.  As if the back is pushing the front.  Just like how a real snake would move.

First we have to find how many segments in the list using len(), then move the last segment to to previous segment.
Also, the very first item in seg will have to move to occupy the current position of the head.
``` 
def move_seg():
    for i in range(len(seg)-1, 0, -1):
        x = seg[i-1].xcor()
        y = seg[i-1].ycor()
        seg[i].goto(x,y)
    # move seg 0
    if len(seg) > 0:
        x = head.xcor()
        y = head.ycor()
        seg[0].goto(x,y) 
```
Check out the effect by running snake07.py

<a name='borderCollision'></a>
## 8. Collison with border
It's time now to deal with how the game would end -- if the snake hits the border or it collides with it self.

Start with border first.  

All we have to do is to check if the head of the snake hit the sides: either x or y co-ordinates hitting + or - 290.

```
    if head.xcor() >290 or head.xcor() <-290 or head.ycor() >290 or head.ycor() <-290:
```
Once detected, we would add a pause, then send the snake back to starting position.
```
time.sleep(1)
head.goto(0,0)
head.direction = "stop"
```
Do run snake08.py and check if it works.

<a name='bodyCollision'></a>
## 9. Collison with body
How do we check if the snake head hits its own body? 
We check if the head's position is near any part of its body by calculating their distance apart.
```
for s in seg:
        if s.distance(head) < 20:
```
If that happens, we would do the same thing as we hit the border: reset the snake.  Rather than writing the same lines, let's put them in a function call endSnake().
```
def endSnake():
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop"
```
If you had run snake08.py, you would notice something weird when the game restarts.  There's a grey box in the middle.  That's the remians of the snake's body/segments from previous gameplay.

I have tried to reset/clear screen but all the commands don't seem to do much.  So I had to follow other's advise and send the body/segments out of the canvas.
```
for s in seg:
    s.goto(1000,1000)
seg.clear()
```
seg.clear() sets the segment count back to zero.

Also, you would have notice that the food had been starting at the same spot north of the head.  We now send it to a random co-ordinate.
```
x = random.randint(-290, 290)
y = random.randint(-290, 290)
food.goto(x,y)
```
Try it out with snake09.py!

<a name='score'></a>
## 10. Finally - Adding score board
Now that the movement part is complete, we will add the finishing touch - the score board.

As you would have guessed it, the score board is just another Turtle object. One that we could write on.
```
 Initialise score
score = 0
high_score = 0

board = turtle.Turtle()
board.speed(0)
board.shape("square")
board.color("white")
board.penup()
board.hideturtle()
board.goto(0,260)
board.write("Score: {} High Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))
```
We will use a function to update the score.

Everytime the snake eats the food, we will increase the score by 10 and checks if we need to update the high score.

```
def updateScore():
    global score, high_score
    score += 10
    if score > high_score:
        high_score = score
    board.clear()
    board.write("Score: {} High Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))

```
Since we need to use the ***score*** and ***high_score*** variables in the funtion above ,we have to declare it as global to use it in the function.

Add this line under the game loop where we check for collision with food:
```
updateScore()
```
Lastly, we have to reset the board after the game ends. So, in the endGame() function, call updateScore() with a score of -10.  It will reset the score back to zero and refresh the board.

```
    score = -10
    updateScore()
```
That's it! Our snake game is now complete: snake10.py

