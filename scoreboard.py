from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, player=None):
        super(ScoreBoard, self).__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.game_score = 0
        self.hps = player.hit_points
        self.score_update()

    def score_update(self):
        self.goto(x=100, y=240)
        self.write(self.game_score, font=('Courier', 40, 'normal'))
        self.goto(x=-200, y=-280)
        self.write(self.hps, font=('Courier', 40, 'normal'))

    def score_increase(self, points):
        self.game_score += points
        self.clear()
        self.score_update()

    def hp_decrease(self):
        self.hps -= 1
        self.clear()
        self.score_update()