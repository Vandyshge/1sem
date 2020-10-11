import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 5
time = 1 / FPS
side = 500
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
body = []
N = 0

def new_ball(screen, body):
    '''рисует новый шарик '''
    x = float(randint(100, 300))
    y = float(randint(100, 300))
    r = float(randint(10, 100))
    v_x = float(randint(-10, 10)) * 5
    v_y = float(randint(-10, 10)) * 5
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    body.append([x, y, v_x, v_y, r, color, 20])

def ball(screen, n, body):
    circle(screen, body[n][5], (body[n][0], body[n][1]), body[n][4])


def new_score(score, x_m, y_m, body):
    '''если мышкой попал по шарику, то твои очки увеличиваются на 1'''
    for n in range(len(body) - 1, -1, -1):
        # print('3 ---', n)
        print()
        if body[n][4]**2 >= ((body[n][0] - x_m)**2 + (body[n][1] - y_m)**2):
            print("Попал")
            del_ball(n, body)
            return score + 1
    print("Промах")
    return score

def del_ball(n, body):
    body.pop(n)


def trance_i(screen, n, body, time, side, del_balls):
    # print('1 ---', body[n][:4])
    x_i = body[n][0] + body[n][2] * time
    y_i = body[n][1] + body[n][3] * time
    # print('2 ---', x_i, y_i)

    r_i = body[n][4]

    if x_i <= r_i:
        body[n][0] = 2 * r_i - x_i
        body[n][2] = - body[n][2]
    elif x_i >= (side - r_i):
        body[n][0] = 2 * (side - r_i) - x_i
        body[n][2] = - body[n][2]
    else:
        body[n][0] = x_i

    if y_i <= r_i:
        body[n][1] = 2 * r_i - y_i
        body[n][3] = - body[n][3]
    elif y_i >= (side - r_i):
        body[n][1] = 2 * (side - r_i) - y_i
        body[n][3] = - body[n][3]
    else:
        body[n][1] = y_i

    if body[n][6] == 0:
        del_balls.append(n)
    else:
        body[n][6] -= 1
        ball(screen, n, body)

    # print('3 ---', body[n])
    # print()


def trance(screen, body, time, side):
    del_balls = []
    # print(body)
    N = len(body)
    for n in range(N):
        trance_i(screen, n, body, time, side, del_balls)
    for n in del_balls:
        del_ball(n, body)



k = 20


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
            score = new_score(score, x_m, y_m, body)
            print("score --- {}".format(score))


    trance(screen, body, time, side)
    if (k == 20) or (len(body) == 0):
        new_ball(screen, body)
        k = 0
    k += 1
    pygame.display.update()

    screen.fill(BLACK)

pygame.quit()