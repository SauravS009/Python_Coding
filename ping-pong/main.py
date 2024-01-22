from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Ping-Pong")
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")
ball = Ball()
scoreboard = Scoreboard()
is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.ball_move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.xcor() == 330 and ball.distance(paddle1) < 63) or (ball.xcor() == -330 and ball.distance(paddle2) < 63):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_update()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_update()

screen.exitonclick()
