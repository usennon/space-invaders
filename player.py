from turtle import Turtle
from shoot import Shoot

MOVE_DISTANCE = 20


class Player(Turtle):

    shoots = []

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(1, 2.5)
        self.color('white')
        self.goto(x=0, y=-250)
        self.hit_points = 3

    def go_left(self):
        if self.xcor() > -280:
            self.backward(MOVE_DISTANCE)

    def go_right(self):
        if self.xcor() < 280:
            self.forward(MOVE_DISTANCE)

    def shoot(self):
        new_shoot = Shoot()
        new_shoot.goto(x=self.xcor(), y=self.ycor() + 20)
        self.shoots.append(new_shoot)

