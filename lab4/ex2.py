import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 10
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

# score = 0
# balls = []
# squares = []
# N = 0
game_time = 5

def new_ball(screen, balls):
    '''рисует новый кружочек '''
    x = float(randint(100, 300))
    y = float(randint(100, 300))
    r = float(randint(10, 100))
    v_x = float(randint(-10, 10)) * 5
    v_y = float(randint(-10, 10)) * 5
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    balls.append([x, y, v_x, v_y, r, color, 20])

def new_square(screen, squares):
    '''рисует новый квадратик '''
    x = float(randint(100, 300))
    y = float(randint(100, 300))
    a = float(randint(10, 100))
    v_x = float(randint(-10, 10)) * 10
    v_y = float(randint(-10, 10)) * 10
    color = COLORS[randint(0, 5)]
    rect(screen, color, (x - a / 2, y - a / 2, a, a))
    squares.append([x, y, v_x, v_y, a, color, 100])


def ball(screen, n, balls):
    circle(screen, balls[n][5], (balls[n][0], balls[n][1]), balls[n][4])

def square(screen, n, squares):
    a_n = squares[n][4]
    rect(screen, squares[n][5], (squares[n][0] - a_n / 2, squares[n][1] - a_n / 2, a_n, a_n))

def del_ball(n, balls):
    balls.pop(n)

def del_square(n, squares):
    squares.pop(n)


def trance_ball_n(screen, n, balls, time, side, del_balls):
    x_n = balls[n][0] + balls[n][2] * time
    y_n = balls[n][1] + balls[n][3] * time

    r_n = balls[n][4]

    if x_n <= r_n:
        balls[n][0] = 2 * r_n - x_n
        balls[n][2] = - balls[n][2]
    elif x_n >= (side - r_n):
        balls[n][0] = 2 * (side - r_n) - x_n
        balls[n][2] = - balls[n][2]
    else:
        balls[n][0] = x_n

    if y_n <= r_n:
        balls[n][1] = 2 * r_n - y_n
        balls[n][3] = - balls[n][3]
    elif y_n >= (side - r_n):
        balls[n][1] = 2 * (side - r_n) - y_n
        balls[n][3] = - balls[n][3]
    else:
        balls[n][1] = y_n

    if balls[n][6] == 0:
        del_balls.append(n)
    else:
        balls[n][6] -= 1
        ball(screen, n, balls)

def trance_square_n(screen, n, squares, time, side, del_squares):
    x_n = squares[n][0] + squares[n][2] * time
    y_n = squares[n][1] + squares[n][3] * time

    a_n = squares[n][4]

    if x_n <= a_n / 2:
        squares[n][0] = 2 * a_n / 2 - x_n
        squares[n][2] = - squares[n][2]
    elif x_n >= (side - a_n / 2):
        squares[n][0] = 2 * (side - a_n / 2) - x_n
        squares[n][2] = - squares[n][2]
    else:
        squares[n][0] = x_n

    if y_n <= a_n / 2:
        squares[n][1] = 2 * a_n / 2 - y_n
        squares[n][3] = - squares[n][3]
    elif y_n >= (side - a_n / 2):
        squares[n][1] = 2 * (side - a_n / 2) - y_n
        squares[n][3] = - squares[n][3]
    else:
        squares[n][1] = y_n

    if squares[n][6] == 0:
        del_squares.append(n)
    else:
        squares[n][6] -= 1
        square(screen, n, squares)


def new_score(score, x_m, y_m, balls, squares):
    '''
    если мышкой попал по кружочку, то твои очки увеличиваются на 1
    если мышкой попал по квадратику, то твои очки увеличиваются на 10

    '''
    for n in range(len(balls) - 1, -1, -1):
        print()
        if balls[n][4]**2 >= ((balls[n][0] - x_m)**2 + (balls[n][1] - y_m)**2):
            print("Попал")
            del_ball(n, balls)
            return score + 1

    for n in range(len(squares) - 1, -1, -1):
        print()
        if (squares[n][4] / 2 >= (abs(squares[n][0] - x_m))) and (squares[n][4] / 2 >= abs(squares[n][1] - y_m)):
            print("Попал")
            del_square(n, squares)
            return score + 10

    print("Промах")
    return score


def trance(screen, balls, squares, time, side):
    del_balls = []
    # print(balls)
    N_b = len(balls)
    for n in range(N_b):
        trance_ball_n(screen, n, balls, time, side, del_balls)
    for n in del_balls:
        del_ball(n, balls)

    del_squares = []
    N_sq = len(squares)
    for n in range(N_sq):
        trance_square_n(screen, n, squares, time, side, del_squares)
    for n in del_squares:
        del_square(n, squares)


# k_b = -100
# k_sq = 30
# k_t = 0
# game_time_i = game_time

# f1 = pygame.font.Font(None, 36)
# text1 = f1.render('score', 20, (250, 250, 250))
# screen.blit(text1, (10, 50))

# f2 = pygame.font.Font(None, 36)
# text2 = f2.render('time: {}'.format(game_time_i), 20, (250, 250, 250))
# screen.blit(text2, (5, 20))

k_g = 0
k_g_0 = 1


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    print(':)')

    if k_g == 0:

        print(':(')

        f0 = pygame.font.Font(None, 36)
        text0 = f0.render('start', 5, (250, 250, 250))
        screen.blit(text0, (10, 10))

        f0 = pygame.font.Font(None, 36)
        text0 = f0.render('write name and push start or enter :)', 5, (250, 250, 250))
        screen.blit(text0, (10, 35))

        name = ''

        pygame.display.update()

        while k_g_0 == 1:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                    k_g_0 = 0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x_m, y_m = event.pos
                    if (25 >= (30 - x_m)) and (15 >= abs(10 - y_m)):
                        k_g_0 = 0
                        k_g_1 = 1
                        k_g = 1
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        k_g_0 = 0
                        k_g_1 = 1
                        k_g = 1
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        name += event.unicode
                        f0 = pygame.font.Font(None, 36)
                        text0 = f0.render(name, 5, (250, 250, 250))
                        screen.blit(text0, (10, 60))

                        pygame.display.update()



        screen.fill(BLACK)

        pygame.display.update()


    elif k_g == 1:

        score = 0
        balls = []
        squares = []

        k_b = -100
        k_sq = 30
        k_t = 0
        game_time_i = game_time

        f1 = pygame.font.Font(None, 36)
        text1 = f1.render('score', 20, (250, 250, 250))
        screen.blit(text1, (10, 50))

        f2 = pygame.font.Font(None, 36)
        text2 = f2.render('time: {}'.format(game_time_i), 20, (250, 250, 250))
        screen.blit(text2, (5, 20))

        while k_g_1 == 1:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                    k_g_1 == 0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x_m, y_m = event.pos
                    score = new_score(score, x_m, y_m, balls, squares)
                    print("score --- {}".format(score))


            trance(screen, balls, squares, time, side)

            if (k_b == 30) or (len(balls) == 0):
                new_ball(screen, balls)
                k_b = 0
            k_b += 1

            if (k_sq == 30) or (len(squares) == 0):
                new_square(screen, squares)
                k_sq = 0
            k_sq += 1

            f1 = pygame.font.Font(None, 36)
            text1 = f1.render('score: {}'.format(score), 20, (250, 250, 250))
            screen.blit(text1, (5, 5))

            f2 = pygame.font.Font(None, 36)
            text2 = f2.render('time: {}'.format(game_time_i), 20, (250, 250, 250))
            screen.blit(text2, (5, 30))

            if k_t != FPS:
                k_t += 1
            else:
                game_time_i -= 1
                k_t = 0

            pygame.display.update()

            screen.fill(BLACK)

            if game_time_i == 0:
                k_g_1 = 0
                k_g_2 = 1

        print(';)')
        k_g = 2


    elif k_g == 2:

        out = open('C:/Users/Xiaomi/1sem/lab4/list.txt', 'a')
        out.write(name + ' --- ' + str(score) + '\n')
        out.close()

        while k_g_2 == 1:
            clock.tick(FPS)

            f3 = pygame.font.Font(None, 36)
            text3 = f3.render('GAME OVER', 20, (250, 250, 250))
            screen.blit(text3, (5, 5))

            f4 = pygame.font.Font(None, 36)
            text4 = f4.render('your score: {}'.format(score), 20, (250, 250, 250))
            screen.blit(text4, (5, 30))

            f5 = pygame.font.Font(None, 36)
            text5 = f5.render('start again', 20, (250, 250, 250))
            screen.blit(text5, (5, 55))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                    k_g_2 = 0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x_m, y_m = event.pos
                    if (25 >= (30 - x_m)) and (15 >= abs(60 - y_m)):
                        k_g_2 = 0
                        k_g = 1
                        k_g_1 = 1

                        print('\')')

            pygame.display.update()


        screen.fill(BLACK)

        pygame.display.update()



pygame.quit()