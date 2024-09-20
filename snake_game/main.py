import turtle

from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sanke Game")
screen.tracer(0)

snake = Snake()

food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extand()
        scoreboard.inc_score()

    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() <= -290 or snake.head.ycor() >= 290:
        scoreboard.reset()
        snake.reset()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()
