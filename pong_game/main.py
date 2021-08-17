from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
score = Scoreboard()

screen.listen()

screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")

screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # Collision with wall
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce_y()

    # Collision with right and left paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        ball.move_speed *= 0.9

    # Checking If the ball collides with the left or right wall
    if ball.xcor() > 380:
        ball.reset()
        score.l_point()
        ball.move_speed = 0.1
    if ball.xcor() < -390:
        ball.reset()
        score.r_point()
        ball.move_speed = 0.1

screen.exitonclick()
