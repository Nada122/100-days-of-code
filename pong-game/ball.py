from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(1, 1)
        self.color('white')
        self.penup()
        self.y_move = 10
        self.x_move = 10
        self.sleep = 0.1

    def move(self):
        x = self.xcor()+self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1
        self.sleep *= 0.8

    def reset(self):
        self.goto(0, 0)
        self.sleep = 0.1

