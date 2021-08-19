import time
# import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=player.move_up)
screen.onkeypress(key="Down", fun=player.move_down)

game_is_on = True
loop = 0


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Collision With Car

    for car in car_manager.all_cars:
        if car.distance(player) < 10:
            game_is_on = False
            score.game_over()

    # Reaching the Finishing Line

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score.update_score()


screen.exitonclick()
