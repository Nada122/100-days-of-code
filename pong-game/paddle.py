from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def go_up(self):
        y = self.ycor() + 20
        x = self.xcor()
        self.goto(x, y)

    def go_down(self):
        y = self.ycor() - 20
        x = self.xcor()
        self.goto(x, y)

    def reset(self,position):
        self.goto(position)

