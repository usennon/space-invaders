from turtle import Turtle
from shoot import Shoot


class AlienManager:
    aliens = []

    def __init__(self):
        self.aliens_generate()

    def aliens_generate(self):
        x = -150
        y = 240
        for i in range(5):
            aliens_row = []
            for j in range(11):
                alien = Alien()
                alien.goto(x=x, y=y)
                aliens_row.append(alien)
                x += 30
            self.aliens.append(aliens_row)
            x = -150
            y -= 30


class Alien(Turtle):
    shoots = []

    def __init__(self):
        super(Alien, self).__init__()
        self.shape('square')
        self.shapesize(0.7, 0.7)
        self.penup()
        self.color('green')

    def shoot(self):
        new_shoot = Shoot()
        new_shoot.goto(x=self.xcor(), y=self.ycor() - 10)
        self.shoots.append(new_shoot)


class UFO(Turtle):
    def __init__(self):
        super(UFO, self).__init__()
        self.shape('square')
        self.shapesize(0.7, 2)
        self.goto(x=-280, y=260)
        self.penup()
        self.color('red')
