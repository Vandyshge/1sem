import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
side = 400
screen = pygame.display.set_mode((side, side))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
score = 0

def new_ball():
    '''рисует новый шарик '''
    x = randint(100, 300)
    y = randint(100, 300)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

    return (x, y, r)


def new_score(score, x_m, y_m, x, y, r):
    '''если мышкой попал по шарику, то твои очки увеличиваются на 1'''
    if r**2 >= ((x - x_m)**2 + (y - y_m)**2):
        print("Попал")
        return score + 1
    else:
        print("Промах")
        return score

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_m, y_m = event.pos
            score = new_score(score, x_m, y_m, x, y, r)
            print("score --- {}".format(score))

    x, y, r = new_ball()
    pygame.display.update()

    screen.fill(BLACK)

pygame.quit()