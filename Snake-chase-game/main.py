from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.title("Not your Average Snake-Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_off = False
while not is_game_off:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 285 or snake.head.ycor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() < -285:
        scoreboard.high_score()
        snake.reset()
    for part in snake.parts[1:]:
        if part == snake.head:
            pass
        elif snake.head.distance(part) < 10:
            scoreboard.high_score()
            snake.reset()

screen.exitonclick()
