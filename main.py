import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "w")
screen.onkeypress(player.go_down, "s")

loop_count = 0
loop_divider = 6
cars = []
move_increment = 10

game_is_on = True
while game_is_on:

    loop_count += 1
    if loop_count % loop_divider == 0:
        cars.append(CarManager(move_increment))
    for car in cars:
        car.drive()

    for car in cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.crossed_road()
        move_increment *= 1.1
        scoreboard.level_up()
        if scoreboard.level >= 15:
            loop_divider = 1
        elif scoreboard.level >= 10:
            loop_divider = 2
        elif scoreboard.level >= 5:
            loop_divider = 3

    time.sleep(0.08)
    screen.update()

screen.exitonclick()
