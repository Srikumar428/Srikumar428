from turtle import *
from snake import Snake
import  time
from food import Food
from scorecard import *

screen = Screen()
screen.setup(height = 600 , width = 600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()
screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left",fun = snake.left)
screen.onkey(key = "Right",fun = snake.right)
game_is_on = True
scoreboard = Scoreboard()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collison
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset_scoreboard()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset()




screen.exitonclick()