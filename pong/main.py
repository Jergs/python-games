from turtle import *

paddle_dy = 40


# Get paddles for playing
def get_paddle(speed_val, shape_val, color_val, is_left) -> Turtle:
    paddle = Turtle()
    paddle.speed(speed_val)
    paddle.shape(shape_val)
    paddle.color(color_val)
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    if is_left:
        paddle.goto(-350, 0)
    else:
        paddle.goto(350, 0)
    return paddle


# Get ball for playing
def get_ball(speed_val, shape_val, color_val):
    ball_paddle = Turtle()
    ball_paddle.speed(speed_val)
    ball_paddle.shape(shape_val)
    ball_paddle.color(color_val)
    ball_paddle.penup()
    ball_paddle.goto(0, 0)

    # Ball movement
    ball_paddle.dx = 0.1
    ball_paddle.dy = - 0.1
    return ball_paddle


# Move left paddle up
def left_paddle_up():
    y = paddle_left.ycor()
    paddle_left.sety(y + paddle_dy)


# Move left paddle down
def left_paddle_down():
    y = paddle_left.ycor()
    paddle_left.sety(y - paddle_dy)


# Move left paddle up
def right_paddle_up():
    y = paddle_right.ycor()
    paddle_right.sety(y + paddle_dy)


# Move left paddle down
def right_paddle_down():
    y = paddle_right.ycor()
    paddle_right.sety(y - paddle_dy)


# Window managing
win = Screen()
win.title("Pong game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddles
paddle_left = get_paddle(0, "square", "white", True)
paddle_right = get_paddle(0, "square", "white", False)
ball = get_ball(0, "square", "white")

# Scoring
score_a = 0
score_b = 0

pen = Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

# Keyboard listeners
win.listen()
win.onkeypress(left_paddle_up, "w")
win.onkeypress(left_paddle_down, "s")
win.onkeypress(right_paddle_up, "Up")
win.onkeypress(right_paddle_down, "Down")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < - 290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.dx *= -1

    if ball.xcor() < - 390:
        ball.goto(0, 0)
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.dx *= -1

    if (340 < ball.xcor() < 350) and (
            paddle_right.ycor() + 40 > ball.ycor() > paddle_right.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (- 340 > ball.xcor() > - 350) and (
            paddle_left.ycor() + 40 > ball.ycor() > paddle_left.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
