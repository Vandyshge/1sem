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
squares = []
N = 0


def new_square(screen, squares):
    '''рисует новый шарик '''
    x = float(randint(100, 300))
    y = float(randint(100, 300))
    a = float(randint(10, 100))
    v_x = float(randint(-10, 10)) * 5
    v_y = float(randint(-10, 10)) * 5
    color = COLORS[randint(0, 5)]
    rect(screen, color, (x - a / 2, y - a / 2, a, a))
    squares.append([x, y, v_x, v_y, a, color, 20])


def square(screen, n, squares):
    a_n = squares[n][4]
    rect(screen, squares[n][5], (squares[n][0] - a / 2, squares[n][1] - a / 2, a, a))


def new_score(score, x_m, y_m, squares):
    '''если мышкой попал по шарику, то твои очки увеличиваются на 1'''
    for n in range(len(squares) - 1, -1, -1):
        # print('3 ---', n)
        print()
        if squares[n][4]**2 >= ((squares[n][0] - x_m)**2 + (squares[n][1] - y_m)**2):
            print("Попал")
            del_square(n, squares)
            return score + 1
    print("Промах")
    return score

def del_square(n, squares):
    squares.pop(n)


def trance_n(screen, n, squares, time, side, del_squares):
    # print('1 ---', squares[n][:4])
    x_n = squares[n][0] + squares[n][2] * time
    y_n = squares[n][1] + squares[n][3] * time
    # print('2 ---', x_n, y_n)

    r_n = squares[n][4]

    if x_n <= r_n:
        squares[n][0] = 2 * r_n - x_n
        squares[n][2] = - squares[n][2]
    elif x_n >= (side - r_n):
        squares[n][0] = 2 * (side - r_n) - x_n
        squares[n][2] = - squares[n][2]
    else:
        squares[n][0] = x_n

    if y_n <= r_n:
        squares[n][1] = 2 * r_n - y_n
        squares[n][3] = - squares[n][3]
    elif y_n >= (side - r_n):
        squares[n][1] = 2 * (side - r_n) - y_n
        squares[n][3] = - squares[n][3]
    else:
        squares[n][1] = y_n

    if squares[n][6] == 0:
        del_squares.append(n)
    else:
        squares[n][6] -= 1
        square(screen, n, squares)

    # print('3 ---', squares[n])
    # print()


def trance(screen, squares, time, side):
    del_squares = []
    # print(squares)
    N = len(squares)
    for n in range(N):
        trance_i(screen, n, squares, time, side, del_squares)
    for n in del_squares:
        del_square(n, squares)


k = 20

new_square(screen, squares)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    #     elif event.type == pygame.MOUSEBUTTONDOWN:
    #         x_m, y_m = event.pos
    #         score = new_score(score, x_m, y_m, balls)
    #         print("score --- {}".format(score))


    # trance(screen, balls, time, side)
    # if (k == 20) or (len(balls) == 0):
    #     new_ball(screen, balls)
    #     k = 0
    # k += 1
    # pygame.display.update()

    # screen.fill(BLACK)

pygame.quit()