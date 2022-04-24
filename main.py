from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

scoreboard = Scoreboard()

screen = Screen()
screen.listen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
new_ball = Ball()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    new_ball.move()

    # Detects collision with wall
    if new_ball.ycor() > 280 or new_ball.ycor() < -280:
        # needs to bounce
        new_ball.bounce_y()

    # Detects collision with paddles
    if new_ball.distance(r_paddle) < 50 and new_ball.xcor() > 330 or new_ball.distance(l_paddle) < 50 and new_ball.xcor() < -330:
        new_ball.bounce_x()

    # Detects out of right
    if new_ball.xcor() > 340:
        new_ball.home()
        new_ball.bounce_x()
        scoreboard.l_point()

    # Detects out of bound on left
    if new_ball.xcor() < -340:
        new_ball.home()
        new_ball.bounce_x()
        scoreboard.r_point()


screen.exitonclick()