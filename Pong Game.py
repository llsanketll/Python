import turtle

# Window Setup
wn = turtle.Screen()
wn.setup(width = 600, height = 600)
wn.bgcolor("Black")
wn.tracer(0)
wn.title("Pong Game")

#Pong Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.shape("Square")
paddle_1.color("white")
paddle_1.penup()
paddle_1.speed(0)
paddle_1.goto(550, 300)

#Windows Update
while True:
    wn.update()
