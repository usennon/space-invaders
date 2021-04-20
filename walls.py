from turtle import Turtle


class Walls:
    wall_parts = []

    def __init__(self):
        self.create_walls()

    def create_walls(self):
        y_cor = -170
        x_cor = -180
        for i in range(4):
            for j in range(6):
                wall_part = Turtle(shape='square')
                wall_part.shapesize(0.3, 3)
                wall_part.penup()
                wall_part.color('white')
                wall_part.goto(x=x_cor, y=y_cor)
                y_cor += 10
                self.wall_parts.append(wall_part)
            y_cor = -170
            x_cor += 120

    def reset_walls(self):
        for wall in self.wall_parts:
            wall.reset()
            self.wall_parts.remove(wall)