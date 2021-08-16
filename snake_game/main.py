from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game🐍")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkeypress(key="Up", fun=snake.up)
screen.onkeypress(key="Down", fun=snake.down)
screen.onkeypress(key="Left", fun=snake.left)
screen.onkeypress(key="Right", fun=snake.right)

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Check for Collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()

    # Detect Collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect Collision With Tail
    for segment in snake.segments[1:]:
        if snake.head.distance (segment) < 10:
            game_is_on = False
            score.game_over()
screen.exitonclick()
