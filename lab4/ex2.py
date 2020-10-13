import pygame
from pygame.draw import *
from random import randint
pygame.init()

# кол-во кадров в секнуду
FPS = 50
# время одного кадра
time = 1 / FPS
# сторона экрана
side = 500
# создание экрана
screen = pygame.display.set_mode((side, side))

# цвета
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (250, 250, 250)
# цвета шариков
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball(screen, balls):
    '''
    создаёт и рисует новый кружочек 

    screen - экран
    balls - массив кружочков

    '''
    # рандомные координаты центра, радиус, скорость и цвет
    x = float(randint(100, 300))
    y = float(randint(100, 300))
    r = float(randint(10, 50))
    v_x = float(randint(-10, 10)) * 5
    v_y = float(randint(-10, 10)) * 5
    color = COLORS[randint(0, 5)]
    # рисование нового кружочков
    circle(screen, color, (x, y), r)
    # запись в массив нового кружочка(последнее число в массиве -  время жизни)
    balls.append([x, y, v_x, v_y, r, color, 5 * FPS])

def new_square(screen, squares):
    '''
    создаёт и рисует новый квадратик 

    screen - экран
    squares - массив квадратиков

    '''
    # рандомные координаты центра, длинна стороны, скорость и цвет
    x = float(randint(100, 300))
    y = float(randint(100, 300))
    a = float(randint(10, 100))
    v_x = float(randint(-10, 10)) * 10
    v_y = float(randint(-10, 10)) * 10
    color = COLORS[randint(0, 5)]
    # рисование нового квадратика
    rect(screen, color, (x - a / 2, y - a / 2, a, a))
    # запись в массив нового квадратика(последнее число в массиве -  время жизни)
    squares.append([x, y, v_x, v_y, a, color, 6 * FPS])


def ball(screen, n, balls):
    '''
    рисование n кружочка

    screen - экран
    n - номер кружочка, который рисуем
    balls - массив кружочков

    '''
    circle(screen, balls[n][5], (balls[n][0], balls[n][1]), balls[n][4])

def square(screen, n, squares):
    '''
    рисование n квадратика

    screen - экран
    n - номер квадратика, который рисуем
    squares - массив квадратиков

    '''
    a_n = squares[n][4]
    rect(screen, squares[n][5], (squares[n][0] - a_n / 2, squares[n][1] - a_n / 2, a_n, a_n))

def del_ball(n, balls):
    '''
    удаление n кружочка

    n - номер кружочка, который рисуем
    balls - массив кружочков

    '''
    balls.pop(n)

def del_square(n, squares):
    '''
    удаление n квадратика

    n - номер квадратика, который рисуем
    squares - массив квадратиков

    '''
    squares.pop(n)


def trance_ball_n(screen, n, balls, time, side, del_balls):
    '''
    перемещение n кружочка за time

    screen - экран
    n - номер кружочка, который рисуем
    balls - массив кружочков
    time - время одного кадра
    side - сторона экрана
    del_balls - функция удаления кружочков

    '''
    # изменение координат
    # (balls[n][0], balls[n][1] - координаты в предыдущий момент)
    # (balls[n][2] и balls[n][3] - скорости)
    x_n = balls[n][0] + balls[n][2] * time
    y_n = balls[n][1] + balls[n][3] * time
    # радиус
    r_n = balls[n][4]

    # реализация откскока от стенки по оси x
    if x_n <= r_n:
        balls[n][0] = 2 * r_n - x_n
        balls[n][2] = - balls[n][2]
    elif x_n >= (side - r_n):
        balls[n][0] = 2 * (side - r_n) - x_n
        balls[n][2] = - balls[n][2]
    else:
        # если нет отскока
        balls[n][0] = x_n

    # реализация откскока от стенки по оси y
    if y_n <= r_n:
        balls[n][1] = 2 * r_n - y_n
        balls[n][3] = - balls[n][3]
    elif y_n >= (side - r_n):
        balls[n][1] = 2 * (side - r_n) - y_n
        balls[n][3] = - balls[n][3]
    else:
        # если нет отскока
        balls[n][1] = y_n

    # проверка времени жизни
    if balls[n][6] == 0:
        # время закончилось, шарик записывается в массив на удаление
        del_balls.append(n)
    else:
        # частица жива
        balls[n][6] -= 1
        # рисование частицы
        ball(screen, n, balls)

def trance_square_n(screen, n, squares, time, side, del_squares):
    '''
    перемещение n квадратика за time

    screen - экран
    n - номер квадратика, который рисуем
    squares - массив квадратиков
    time - время одного кадра
    side - сторона экрана
    del_square - функция удаления квадратика

    '''
    # изменение координат
    # (squares[n][0], squares[n][1] - координаты в предыдущий момент)
    # (squares[n][2] и squares[n][3] - скорости)
    # (движение не по прямой. (1 + 0.3 * randint(-10, 10)) - отвечает за это)
    x_n = squares[n][0] + squares[n][2] * (1 + 0.3 * randint(-10, 10)) * time
    y_n = squares[n][1] + squares[n][3] * (1 + 0.1 * randint(-10, 10)) * time
    # сторона квадратика
    a_n = squares[n][4]

    # реализация откскока от стенки по оси x
    if x_n <= a_n / 2:
        squares[n][0] = 2 * a_n / 2 - x_n
        squares[n][2] = - squares[n][2]
    elif x_n >= (side - a_n / 2):
        squares[n][0] = 2 * (side - a_n / 2) - x_n
        squares[n][2] = - squares[n][2]
    else:
        # если нет отскока
        squares[n][0] = x_n

    # реализация откскока от стенки по оси y
    if y_n <= a_n / 2:
        squares[n][1] = 2 * a_n / 2 - y_n
        squares[n][3] = - squares[n][3]
    elif y_n >= (side - a_n / 2):
        squares[n][1] = 2 * (side - a_n / 2) - y_n
        squares[n][3] = - squares[n][3]
    else:
        # если нет отскока
        squares[n][1] = y_n

    # проверка времени жизни
    if squares[n][6] == 0:
        # время закончилось, шарик записывается в массив на удаление
        del_squares.append(n)
    else:
        # частица жива
        squares[n][6] -= 1
        # рисование частицы
        square(screen, n, squares)

def trance(screen, balls, squares, time, side):
    '''
    перемещение всех частиц за time

    screen - экран
    balls - массив кружочков
    squares - массив квадратиков
    time - время одного кадра
    side - сторона экрана

    '''
    # массив, в который записываем кружочки, которые умерли
    del_balls = []
    N_b = len(balls)
    # перемещаем каждый кружочек
    for n in range(N_b):
        trance_ball_n(screen, n, balls, time, side, del_balls)
    # удаляем умершие кружочки
    for n in del_balls:
        del_ball(n, balls)

    # массив, в который записываем квадратики, которые умерли
    del_squares = []
    N_sq = len(squares)
    # перемещаем каждый квадратик
    for n in range(N_sq):
        trance_square_n(screen, n, squares, time, side, del_squares)
    # удаляем умершие квадратики
    for n in del_squares:
        del_square(n, squares)

def new_score(score, x_m, y_m, balls, squares):
    '''
    если мышкой попал по кружочку, то твои очки увеличиваются на 1
    если мышкой попал по квадратику, то твои очки увеличиваются на 10

    score - счет игрока
    x_m, y_m - координаты мышки
    balls - массив кружочков
    squares - массив квадратиков

    '''
    # проходим по всем кружочкам, если мышка в области кружочка, то увеличиваем счёт на 1
    for n in range(len(balls) - 1, -1, -1):
        if balls[n][4]**2 >= ((balls[n][0] - x_m)**2 + (balls[n][1] - y_m)**2):
            # на всяций случай выводим в командную строку
            print("Попал")
            # удаляем кружочек
            del_ball(n, balls)
            return score + 1

    # проходим по всем квадратикам, если мышка в области квадратика, то увеличиваем счёт на 10
    for n in range(len(squares) - 1, -1, -1):
        if (squares[n][4] / 2 >= (abs(squares[n][0] - x_m))) and (squares[n][4] / 2 >= abs(squares[n][1] - y_m)):
            # на всяций случай выводим в командную строку
            print("Попал")
            # удаляем квадратик
            del_square(n, squares)
            return score + 10

    # если не попал, счёт остаётся неизменным
    print("Промах")
    return score

def result(name, score):
    '''
    записываем результат игрока и создаём рейтинг с учётом его результата

    name - имя игрока
    score - счёт игрока

    '''
    # записываем в массив результаты других игроков 
    out = open('C:/Users/Xiaomi/1sem/lab4/list.txt', 'r')
    people = []
    line = out.readline().strip()
    while line != '':
        line = line.split(' ')
        people.append((int(line[3]), line[1]))
        line = out.readline().strip()
    out.close()
    out = open('C:/Users/Xiaomi/1sem/lab4/list.txt', 'w')
    # добавляем результаты игрока
    people.append((score, name))
    # сортируем результаты по счёту игроков
    people = sorted(people, key=lambda x: -x[0])
    # записываем рейтинг в тот же файл
    for i in range(len(people)):
        out.write('{}. {} --- {}\n'.format(i + 1, people[i][1], people[i][0]))
    out.close()

# флажок начальной страницы
k_g = 'page_0'


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    # условия отображения страницы
    
    if k_g == 'page_0':
        # главная страница
        
        # текст страницы
        # интерактивная кнопка - 'start' - начало игры
        f0 = pygame.font.Font(None, 36)
        text0 = f0.render('start', 5, WHITE)
        screen.blit(text0, (10, 10))

        f0 = pygame.font.Font(None, 36)
        text0 = f0.render('write name and push start or enter :)', 5, WHITE)
        screen.blit(text0, (10, 35))

        # переменная для имеени игрока
        name = ''

        pygame.display.update()

        # флажок для выхода из цикла
        k_g_0 = 1

        while k_g_0 == 1:
            clock.tick(FPS)

            for event in pygame.event.get():
                # выходим из главного цикла, если был нажат крестик
                if event.type == pygame.QUIT:
                    finished = True
                    k_g_0 = 0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # реализация интерактивной кнопки - 'start'
                    x_m, y_m = event.pos
                    if (25 >= (30 - x_m)) and (15 >= abs(10 - y_m)):
                        # выходим из цикла
                        k_g_0 = 0
                        # перенаправление на 1 страницу
                        k_g = 'page_1'

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # нажатие Enter
                        # выходим из цикла
                        k_g_0 = 0
                        # перенаправление на первую страницу
                        k_g = 'page_1'

                    elif event.key == pygame.K_BACKSPACE:
                        # нажатие Backspace
                        # удаление последнего символа
                        name = name[:-1]
                        # обновление экрана(с новым именем)
                        screen.fill(BLACK)

                        f0 = pygame.font.Font(None, 36)
                        text0 = f0.render(name, 5, WHITE)
                        screen.blit(text0, (10, 60))

                    else:
                        # любая другая клавиша
                        # добавление введёного символа в имя
                        name += event.unicode
                        # обновление экрана(с новым именем)
                        screen.fill(BLACK)

                        f0 = pygame.font.Font(None, 36)
                        text0 = f0.render(name, 5, WHITE)
                        screen.blit(text0, (10, 60))

                # текст страницы(заново)
                f0 = pygame.font.Font(None, 36)
                text0 = f0.render('start', 5, WHITE)
                screen.blit(text0, (10, 10))

                f0 = pygame.font.Font(None, 36)
                text0 = f0.render('write name and push start or enter :)', 5, WHITE)
                screen.blit(text0, (10, 35))

                pygame.display.update()


        screen.fill(BLACK)

        pygame.display.update()


    elif k_g == 'page_1':
        # страница с игрой

        # начальное кол-во очков
        score = 0
        # массивы элементов
        balls = []
        squares = []

        # флажок для добавления новых кружочков(не 0, чтобы они не начали появляться сразу же)
        k_b = -1 * FPS
        # флажок для добавления новых кружочков(не 0, чтобы они не начали появляться сразу же)
        k_sq = -5 * FPS
        # флажок для отсчёта времени в игре
        k_t = 0
        # время одного раунда(в секундах)
        game_time_i = 10

        # текст страницы
        # очки
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render('score', 20, WHITE)
        screen.blit(text1, (10, 50))
        # оставшееся время
        f2 = pygame.font.Font(None, 36)
        text2 = f2.render('time: {}'.format(game_time_i), 20, WHITE)
        screen.blit(text2, (5, 20))

        # флажок для выхода из цикла
        k_g_1 = 1

        while k_g_1 == 1:
            clock.tick(FPS)

            for event in pygame.event.get():
                # выходим из главного цикла, если был нажат крестик
                if event.type == pygame.QUIT:
                    finished = True
                    k_g_1 == 0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # координаты мышки
                    x_m, y_m = event.pos
                    # обновляем счёт в зависимости от нажатия
                    score = new_score(score, x_m, y_m, balls, squares)
                    # на всякий случай выводим счёт в командную строку
                    print("score --- {}".format(score))

            # передвижение частиц
            trance(screen, balls, squares, time, side)

            # если прошло 6с или на экране нет кружочков, добавляем новый
            if (k_b == 6 * FPS) or (len(balls) == 0):
                new_ball(screen, balls)
                # флажок ставим в положение 0
                k_b = 0
            # обновляем флажок
            k_b += 1

            # если прошло 6с или на экране нет квадратиков, добавляем новый
            if (k_sq == 6 * FPS) or (len(squares) == 0):
                new_square(screen, squares)
                # флажок ставим в положение 0
                k_sq = 0
            # обновляем флажок
            k_sq += 1

            # текст страницы
            # очки
            f1 = pygame.font.Font(None, 36)
            text1 = f1.render('score: {}'.format(score), 20, WHITE)
            screen.blit(text1, (5, 5))

            # оставшееся время
            f2 = pygame.font.Font(None, 36)
            text2 = f2.render('time: {}'.format(game_time_i), 20, WHITE)
            screen.blit(text2, (5, 30))

            # обнавление времени в игре
            if k_t != FPS:
                # если 1с ещё не прошла
                k_t += 1
            else:
                # если прошла одна секунда
                game_time_i -= 1
                k_t = 0

            pygame.display.update()

            screen.fill(BLACK)

            # если время вышло, то выходим из цикла
            if game_time_i == 0:
                # выходим из цикла
                k_g_1 = 0
        
        # после окончания игры переходим на 2 страницу
        k_g = 'page_2'


    elif k_g == 'page_2':
        # стрница с результатом

        # запись результата игрока
        result(name, score)

        # флажок для выхода из цикла
        k_g_2 = 1

        while k_g_2 == 1:
            clock.tick(FPS)

            # текст страницы
            f3 = pygame.font.Font(None, 36)
            text3 = f3.render('GAME OVER', 20, WHITE)
            screen.blit(text3, (5, 5))

            f4 = pygame.font.Font(None, 36)
            text4 = f4.render('your score: {}'.format(score), 20, WHITE)
            screen.blit(text4, (5, 30))

            # интерактивны кнопки(играть заного)
            f5 = pygame.font.Font(None, 36)
            text5 = f5.render('start again', 20, WHITE)
            screen.blit(text5, (5, 55))
            # интерактивная кнопка(переход на начальную страницу)
            f6 = pygame.font.Font(None, 36)
            text6 = f6.render('new player', 20, WHITE)
            screen.blit(text6, (5, 80))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # выходим из главного цикла, если был нажат крестик
                    finished = True
                    k_g_2 = 0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # реализация интерактивных кнопках
                    # координаты мышки
                    x_m, y_m = event.pos
                    # 'start again'
                    if (25 >= (30 - x_m)) and (15 >= abs(60 - y_m)):
                        # выходим из цикла
                        k_g_2 = 0
                        k_g = 'page_1'
                    # 'new player'
                    elif (25 >= (30 - x_m)) and (15 >= abs(85 - y_m)):
                        # выходим из цикла
                        k_g_2 = 0
                        k_g = 'page_0'

            pygame.display.update()


        screen.fill(BLACK)

        pygame.display.update()



pygame.quit()