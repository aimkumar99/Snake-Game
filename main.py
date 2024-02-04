from turtle import Screen
import time
from SnakeFeatures import Snake
from Food_cls import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
       food.refresh()
       snake.extend()
       scoreboard.increase_score()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        is_game_on = False
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            scoreboard.game_over()
            is_game_on = False
screen.exitonclick()
       