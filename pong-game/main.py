import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('pong ')
paddle_one = Paddle((360, 0))
paddle_two = Paddle((-370, 0))
ball = Ball()
score = Score()
screen.listen()
screen.onkeypress(paddle_one.go_up, 'Up')
screen.onkeypress(paddle_one.go_down, 'Down')
screen.onkeypress(paddle_two.go_up, 'w')
screen.onkeypress(paddle_two.go_down, 's')
screen.tracer(0)
game_on = True
while game_on:
    screen.update()
    time.sleep(ball.sleep)
    ball.move()
    if ball.ycor() <= -300 or ball.ycor() >= 300:
        ball.bounce()
    if ball.distance(paddle_one) < 50 and ball.xcor() > 330 or ball.distance(paddle_two) < 50 and ball.xcor() < -340:
        ball.hit()
    if ball.distance(paddle_one) > 50 and ball.xcor() > 410:
        ball.reset()
        paddle_one.reset((360, 0))
        paddle_two.reset((-370, 0))
        score.add_point_2()
        ball.hit()

    if ball.distance(paddle_two) > 50 and ball.xcor() < -410:
        ball.reset()
        paddle_one.reset((360, 0))
        paddle_two.reset((-370, 0))
        score.add_point_1()
        ball.hit()






screen.exitonclick()
