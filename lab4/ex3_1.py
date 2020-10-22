import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 50
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
WHITE = (250, 250, 250)

COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


balls = []
squares = []


class Ball():
    def __init__(self, x, y, v_x, v_y, r, color, life):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.x0 = 0
        self.y0 = 0
        self.r = r
        self.color = color
        self.life = life

    def trance(self, screen, ball, balls):
        dx = self.v_x * time
        dy = self.v_y * time
        x = self.x + dx
        y = self.y + dy

        r = self.r

        k = 0
        if self.x0 != 0 or self.y0 != 0:
            l_x = self.x0 - self.x
            l_y = self.y0 - self.y
            l = (l_x**2 + l_y**2)**0.5
            sin = l_y / l
            cos = l_x / l
            v_x, v_y = self.v_x, self.v_y
            self.v_x = v_x * (- cos ** 2 + sin ** 2) + v_y * (-2 * sin * cos)
            self.v_y = v_x * (-2 * sin * cos) + v_y * (cos ** 2 - sin ** 2)
            self.x = self.x - dx
            self.y = self.y - dy
            self.x0, self.y0 = 0, 0
            k = 1
            print("1 ---", self.x, self.y)
        else:
            for elem in balls:
                if elem != ball:
                    if (self.x + x - elem.x)**2 + (self.y + y - elem.y)**2 <= (self.r + elem.r)**2:
                        elem.x0, elem.y0 = self.x, self.y
                        l_x = elem.x - self.x
                        l_y = elem.y - self.y
                        l = (l_x**2 + l_y**2)**0.5
                        sin = l_y / l
                        cos = l_x / l
                        v_x, v_y = self.v_x, self.v_y
                        self.v_x = v_x * (- cos ** 2 + sin ** 2) + v_y * (-2 * sin * cos)
                        self.v_y = v_x * (-2 * sin * cos) + v_y * (cos ** 2 - sin ** 2)
                        self.x = self.x - dx
                        self.y = self.y - dy
                        k = 1
                        print("2 ---", self.x, self.y)
                        break
       
        if k == 0:
            if x <= r:
                self.x = 2 * r - x
                self.v_x = - self.v_x
            elif x >= (side - r):
                self.x = 2 * (side - r) - x
                self.v_x = - self.v_x
            else:
                self.x = x

            if y <= r:
                self.y = 2 * r - y
                self.v_y = - self.v_y
            elif y >= (side - r):
                self.y = 2 * (side - r) - y
                self.v_y = - self.v_y
            else:
                self.y = y

        if self.life == 0:
            self.delite(ball, balls)
        else:
            self.life -= 1
            self.ball(screen)

    def delite(self, ball, balls):
        balls.pop(balls.index(ball))

    def ball(self, screen):
        circle(screen, self.color, (self.x, self.y), self.r)

    def new_score(self, x_m, y_m, ball, balls):
        if self.r**2 >= ((self.x - x_m)**2 + (self.y - y_m)**2):
            self.delite(ball, balls)
            return 1
        else:
            return 0


class Square():
    def __init__(self, x, y, v_x, v_y, a, color, life):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.a = a
        self.color = color
        self.life = life

    def trance(self, screen, square, squares):
        x = self.x + self.v_x * time
        y = self.y + self.v_y * time

        a = self.a

        if x <= a / 2:
            self.x = 2 * a / 2 - x
            self.v_x = - self.v_x
        elif x >= (side - a / 2):
            self.x = 2 * (side - a / 2) - x
            self.v_x = - self.v_x
        else:
            self.x = x

        if y <= a / 2:
            self.y = 2 * a / 2 - y
            self.v_y = - self.v_y
        elif y >= (side - a / 2):
            self.y = 2 * (side - a / 2) - y
            self.v_y = - self.v_y
        else:
            self.y = y

        if self.life == 0:
            self.delite(square, squares)
        else:
            self.life -= 1
            self.square(screen)

    def delite(self, square, squares):
        squares.pop(squares.index(square))

    def square(self, screen):
        a = self.a
        rect(screen, self.color, (self.x - a / 2, self.y - a / 2, a, a))

    def new_score(self, x_m, y_m, square, squares):
        if (self.a / 2 >= (abs(self.x - x_m))) and (self.a / 2 >= abs(self.y - y_m)):
            self.delite(square, squares)
            return 10
        else:
            return 0



def new_ball(screen, balls):
    '''рисует новый кружочек '''
    x = float(randint(100, 300))
    y = float(randint(100, 300))
    r = float(randint(10, 50))
    v_x = float(randint(-10, 10)) * 5
    v_y = float(randint(-10, 10)) * 5
    color = COLORS[randint(0, 5)]
    balls.append(Ball(x, y, v_x, v_y, r, color, 10 * FPS))
    balls[len(balls) - 1].ball(screen)

def new_square(screen, squares):
    '''рисует новый кружочек '''
    x = float(randint(100, 300))
    y = float(randint(250, 300))
    a = float(randint(10, 50))
    v_x = float(randint(-10, 10)) * 5
    v_y = float(randint(-10, 10)) * 5
    color = COLORS[randint(0, 5)]
    squares.append(Square(x, y, v_x, v_y, a, color, 3 * FPS))
    squares[len(squares) - 1].square(screen)

def trance(screen, balls, squares, time, side):
    for ball in balls:
        ball.trance(screen, ball, balls)
    for square in squares:
        square.trance(screen, square, squares)


def new_score_g(score, x_m, y_m, balls, squares):
    for ball in balls:
        score += ball.new_score(x_m, y_m, ball, balls)
    for square in squares:
        score += square.new_score(x_m, y_m, square, squares)
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
    return people


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
        game_time_i = 15

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
                    score = new_score_g(score, x_m, y_m, balls, squares)
                    # на всякий случай выводим счёт в командную строку
                    print("score --- {}".format(score))

            # передвижение частиц
            trance(screen, balls, squares, time, side)

            # если прошло 6с или на экране нет кружочков, добавляем новый
            if (k_b == 1 * FPS) or (len(balls) == 0):
                new_ball(screen, balls)
                # флажок ставим в положение 0
                k_b = 0
            # обновляем флажок
            k_b += 1

            # # если прошло 6с или на экране нет квадратиков, добавляем новый
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
        people = result(name, score)
        # print(result(name, score))


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


            k_r = 0
            for i in range(len(people)):
                f6 = pygame.font.Font(None, 36)
                text6 = f6.render('{}. {} --- {}'.format(i + 1, people[i][1], people[i][0]), 20, WHITE)
                screen.blit(text6, (5, 130 + k_r))
                k_r += 25


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