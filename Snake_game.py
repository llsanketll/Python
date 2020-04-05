# Snake Game
import turtle
import time
import random

delay: float = 0.1

# Window Setup
wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.bgcolor("black")
wn.tracer(0)
wn.title("Snake Sanket")

# Snake Head
snake = turtle.Turtle()
snake.shape("square")
snake.penup()
snake.color("white")
snake.direction = "stop"
snake.goto(0, 0)
snake.speed(0)

# Snake Food
food = turtle.Turtle()
food.shape("circle")
food.penup()
food.speed(0)
food.color("red")
food.goto(0, 100)

segments = []
# Score
points = 0
high_score = 0
# Score pen
score = turtle.Turtle()
score.penup()
score.hideturtle()
score.color("white")
score.speed(0)
score.goto(0, 260)
score.write(f"Score : {points}\t\tHigh Score : {high_score}", align="center", font=("Arial", 24, "normal"))

# Snake Movement
def snake_up():
    if snake.direction != "down":
        snake.direction = "up"


def snake_down():
    if snake.direction != "up":
        snake.direction = "down"


def snake_right():
    if snake.direction != "left":
        snake.direction = "right"


def snake_left():
    if snake.direction != "right":
        snake.direction = "left"


def move():
    if snake.direction == "up":
        snake.sety(snake.ycor() + 20)
    if snake.direction == "right":
        snake.setx(snake.xcor() + 20)
    if snake.direction == "left":
        snake.setx(snake.xcor() - 20)
    if snake.direction == "down":
        snake.sety(snake.ycor() - 20)


# Key Mapping

wn.listen()
wn.onkeypress(snake_up, "Up")
wn.onkeypress(snake_down, "Down")
wn.onkeypress(snake_right, "Right")
wn.onkeypress(snake_left, "Left")

# Main Game Loop
while True:
    wn.update()

    time.sleep(delay)

    # Border Checking
    # For y-axis
    if snake.ycor() > 280 or snake.ycor() < -280:
        snake.direction = "stop"
        time.sleep(1)
        snake.goto(0, 0)
        points = 0
        score.clear()
        score.write(f"Score : {points}\t\tHigh Score : {high_score}", align="center", font=("Arial", 20, "normal"))

        # Hiding the segment
        for segment in segments:
            segment.goto(1000, 1000)
        # Clearing the segments
        segments.clear()
    # For x-axis
    if snake.xcor() > 280 or snake.xcor() < -280:
        snake.direction = "stop"
        time.sleep(1)
        snake.goto(0, 0)
        points = 0
        score.clear()
        score.write(f"Score : {points}\t\tHigh Score : {high_score}", align="center", font=("Arial", 20, "normal"))

        # Hiding the segment
        for segment in segments:
            segment.goto(1000, 1000)
        # Clearing the segments
        segments.clear()

    # Check for collision for food

    if snake.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))

        # Add a segment

        new_segments = turtle.Turtle()
        new_segments.speed(0)
        new_segments.penup()
        new_segments.shape("square")
        new_segments.color("grey")
        segments.append(new_segments)

        # Increasing the score

        points += 1
        if points > high_score:
            high_score = points

    # Moving the segment

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 with head

    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)
    move()
    # Collision with snake body
    for segment in segments:
        if snake.distance(segment) < 20:
            snake.direction = "stop"
            time.sleep(1)
            snake.goto(0, 0)
            points = 0
            score.clear()
            score.write(f"Score : {points}\t\tHigh Score : {high_score}", align="center", font=("Arial", 20, "normal"))

            # Hiding the segment
            for index in segments :
                index.goto(1000, 1000)
            segments.clear()

    # Displaying the Score
    if points > 0:
        score.clear()
        score.write(f"Score : {points}\t\tHigh Score : {high_score}", align="center", font=("Arial", 20, "normal"))

wn.mainloop()
