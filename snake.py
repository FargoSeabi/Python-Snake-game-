# Imports
import turtle
import time
import random

# Global variables
delay = 0.1

# Scores
score = 0
high_score = 0

# Set up screen
wn = turtle.Screen()
wn.title("Snake  Game")
wn.bgcolor('white')
wn.setup(width=600, height=600)
wn.tracer(0)  # Corrected: 'wn.tracker' to 'wn.tracer'

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)  # Corrected: 'head.got' to 'head.goto'
head.direction = "stop"  # Corrected: "stop" to "Stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Scoreboards
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0, 260)
sc.write("Score: 0 High Score: 0", align="center", font=("ds-digital", 24, "normal"))

# Functions
def go_up():
    if head.direction != "Down":  # Corrected: "down" to "Down"
        head.direction = "Up"  # Corrected: "up" to "Up"

def go_down():
    if head.direction != "Up":
        head.direction = "Down"

def go_left():
    if head.direction != "Right":
        head.direction = "Left"

def go_right():
    if head.direction != "Left":
        head.direction = "Right"

def move():
    if head.direction == "Up":  # Corrected: "!=" to "=="
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "Down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "Left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "Right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main loop
while True:
    wn.update()

    # Check collisions with border area
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments of the body
        for segment in segments:
            segment.goto(1000, 1000)  # Out of range
            segment.clear()

        # Reset score
        score = 0

        # Reset delay
        delay = 0.1

        sc.clear()
        sc.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))

    # Check collisions with food
    if head.distance(food) < 20:
        # Move the food to a random place
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a new segment to the head
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten delay
        delay -= 0.001

        # Increase the score
        score += 10 

        if score > high_score:
            high_score = score

        sc.clear()
        sc.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))

    # Move the segments in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check collision with body
    for segment in segments:
        if head.distance(segment) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"

            # Hide segments
            for segment in segments:
                segment.goto(1000, 1000)
                segment.clear()

            score = 0
            delay = 0.1

            # Update the score
            sc.clear()
            sc.write("Score: {} High Score: {}".format(score, high_score), align="center",
                     font=("ds-digital", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
