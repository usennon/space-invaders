from turtle import Screen
from time import sleep
from player import Player
from walls import Walls
from aliens import AlienManager, UFO
from scoreboard import ScoreBoard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

player = Player()
scoreboard = ScoreBoard(player=player)

walls = Walls()

aliens = AlienManager()

screen.listen()
screen.onkey(player.go_left, 'a')
screen.onkey(player.go_right, 'd')
screen.onkey(player.shoot, 'space')


def transpose(li):
    transposed_list = [[row[i] for row in li] for i in range(len(li[0]))]
    return transposed_list


alien_move_left = True
alien_move_right = False

all_aliens_list = sum(aliens.aliens, [])
transposed_aliens = transpose(aliens.aliens)
all_transposed_aliens = sum(transposed_aliens, [])
ufos = []

game_is_on = True

while game_is_on:
    sleep(0.001)
    screen.update()
    if not all_aliens_list:
        aliens = AlienManager()
        all_aliens_list = sum(aliens.aliens, [])
        transposed_aliens = transpose(aliens.aliens)
        all_transposed_aliens = sum(transposed_aliens, [])
        walls.reset_walls()
        walls.create_walls()
    for item in transposed_aliens:
        if random.randint(0, 700) == 57:
            item[-1].shoot()
    try:
        for shoot in all_aliens_list[0].shoots:
            shoot.move(alien=True)
            for wall in walls.wall_parts:
                if shoot.distance(wall) < 30:
                    wall.reset()
                    walls.wall_parts.remove(wall)
                    shoot.reset()
                    all_aliens_list[0].shoots.remove(shoot)
            if shoot.distance(player) < 30:
                shoot.reset()
                all_aliens_list[0].shoots.remove(shoot)
                scoreboard.hp_decrease()
                sleep(1)
            if shoot.ycor() > 250:
                shoot.reset()
                all_aliens_list[0].shoots.remove(shoot)
    except IndexError:
        continue
    if len(player.shoots) > 1:
        for shoot in player.shoots:
            if player.shoots.index(shoot) > 0:
                shoot.reset()
        player.shoots = [item for item in player.shoots if player.shoots.index(item) == 0]
    for shoot in player.shoots:
        shoot.move()
        if shoot.ycor() > 300:
            shoot.reset()
            player.shoots.remove(shoot)
        for wall in walls.wall_parts:
            if wall.distance(shoot) < 30:
                wall.reset()
                walls.wall_parts.remove(wall)
                shoot.reset()
                player.shoots.remove(shoot)
        for alien in all_aliens_list:
            if alien.distance(shoot) < 20:
                alien.reset()
                all_aliens_list.remove(alien)
                shoot.reset()
                scoreboard.score_increase(10)
                try:
                    player.shoots.remove(shoot)
                except ValueError:
                    pass
        for ufo in ufos:
            if ufo.distance(shoot) < 30:
                ufo.reset()
                ufos.remove(ufo)
                shoot.reset()
                player.shoots.remove(shoot)
                scoreboard.score_increase(300)
    if alien_move_left:
        for alien in all_aliens_list:
            alien.forward(1)
            if alien.xcor() >= 280:
                for alien in all_aliens_list:
                    alien.setheading(90)
                    alien.backward(5)
                    alien.setheading(0)
                    alien_move_left = False
                    alien_move_right = True
    if alien_move_right:
        for alien in all_aliens_list:
            alien.backward(1)
            if alien.xcor() <= -280:
                for alien in all_aliens_list:
                    alien.setheading(90)
                    alien.backward(10)
                    alien.setheading(0)
                    alien_move_left = True
                    alien_move_right = False
    for alien in all_aliens_list:
        if alien.ycor() <= -260:
            game_is_on = False
    if random.randint(0, 1000) == 57:
        new_ufo = UFO()
        ufos.append(new_ufo)
    try:
        for ufo in ufos:
            ufo.forward(2)
            if ufo.xcor() >= 280:
                ufo.reset()
                ufos.remove(ufo)
    except NameError:
        pass
    if scoreboard.hps == 0:
        game_is_on = False

screen.exitonclick()
