from turtle import Turtle


class Shoot(Turtle):
    def __init__(self):
        super(Shoot, self).__init__()
        self.penup()
        self.shape('square')
        self.setheading(90)
        self.shapesize(0.5, 0.7)
        self.color('white')

    def move(self, alien=False):
        if not alien:
            self.goto(x=self.xcor(), y=self.ycor() + 10)
        else:
            self.goto(x=self.xcor(), y=self.ycor() - 3)

