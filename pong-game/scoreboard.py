from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('blue')
        self.paddle_one_score = 0
        self.paddle_two_score = 0
        self.goto(100, 200)
        self.write(self.paddle_one_score, align='center', font=('courier', 60, 'normal'))
        self.goto(-100, 200)
        self.write(self.paddle_two_score, align='center', font=('courier', 60, 'normal'))

    def add_point_1(self):
        self.paddle_one_score += 1
        self.clear()
        self.goto(100, 200)
        self.write(self.paddle_one_score, align='center', font=('courier', 60, 'normal'))
        self.goto(-100, 200)
        self.write(self.paddle_two_score, align='center', font=('courier', 60, 'normal'))

    def add_point_2(self):
        self.paddle_two_score += 1
        self.clear()
        self.goto(100, 200)
        self.write(self.paddle_one_score, align='center', font=('courier', 60, 'normal'))
        self.goto(-100, 200)
        self.write(self.paddle_two_score, align='center', font=('courier', 60, 'normal'))
