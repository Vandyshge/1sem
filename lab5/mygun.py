import pygame
from pygame.draw import *
from random import randint
import numpy as np
pygame.init()

# кол-во кадров в секнуду
FPS = 100
# время одного кадра
dt = 1 / FPS
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


# массив кружочков-снарядов
balls_bullet = []
# массив кружочков-мишений
balls_target = []


class Ball():
    '''Ball - объект кружочек'''
    def __init__(self, x, y, v_x, v_y, r, color, life=5*FPS, g=20):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.k = 0
        self.r = r
        self.color = color
        self.life = life
        self.g = g

    def trance(self, screen, ball, balls):
        '''
        перемещение кружочка за dt

        screen - экран
        ball - кружочек
        balls - массив кружочков

        '''
        # возможные перемещения за dt
        dx = self.v_x * dt
        dy = self.v_y * dt + self.g * dt**2 / 2

        r = self.r

        # реализация столкновений между кружочками
        # k = 1, если кружочек в эту эпоху уже сталкивался. Иначе 0
        if self.k == 0:
            # проверяем столкнётся ли кружочек с другими в следующий момент
            for elem in balls:
                if elem != self:
                    if (self.x + dx - elem.x)**2 + (self.y + dy - elem.y)**2 <= (r + elem.r)**2:
                        # изменяем параметры кружочка, с которым столкнулся ball
                        if elem.k == 0:
                            l_x = self.x - elem.x
                            l_y = self.y - elem.y
                            l = (l_x**2 + l_y**2)**0.5
                            sin = l_y / l
                            cos = l_x / l
                            v_x, v_y = elem.v_x, elem.v_y
                            elem.v_x = v_x * (- cos ** 2 + sin ** 2) + v_y * (-2 * sin * cos)
                            elem.v_y = v_x * (-2 * sin * cos) + v_y * (cos ** 2 - sin ** 2)
                            elem.k = 1
                        # изменяем параметры кружочка
                        l_x = elem.x - self.x
                        l_y = elem.y - self.y
                        l = (l_x**2 + l_y**2)**0.5
                        sin = l_y / l
                        cos = l_x / l
                        v_x, v_y = self.v_x, self.v_y
                        self.v_x = v_x * (- cos ** 2 + sin ** 2) + v_y * (-2 * sin * cos)
                        self.v_y = v_x * (-2 * sin * cos) + v_y * (cos ** 2 - sin ** 2)
                        self.k = 1
                        # изменяем перемещение с учётом столкновения 
                        dx = self.v_x * dt
                        dy = self.v_y * dt + self.g * dt**2 / 2

        # новая координата
        x = self.x + dx
        y = self.y + dy
        self.v_y = self.v_y + self.g * dt
        
        # реализация откскока от стенки по оси x
        if x <= r:
            self.x = 2 * r - x
            self.v_x = - self.v_x
        elif x >= (side - r):
            self.x = 2 * (side - r) - x
            self.v_x = - self.v_x
        else:
            # если нет отскока
            self.x = x

        # реализация откскока от стенки по оси y
        if y <= r:
            self.y = 2 * r - y
            self.v_y = - self.v_y
        elif y >= (side - r):
            self.y = 2 * (side - r) - y
            self.v_y = - self.v_y
        else:
            # если нет отскока
            self.y = y

        if self.life == 0:
            # время закончилось, шарик удаляем
            self.delite(ball, balls)
        else:
            # частица жива
            self.life -= 1
            # рисование частицы
            self.ball(screen)

    def delite(self, ball, balls):
        '''
        удаление кружочка

        ball - кружочек
        balls - массив кружочков

        '''
        balls.pop(balls.index(ball))

    def ball(self, screen):
        '''
        рисование кружочка

        screen - экран

        '''
        circle(screen, self.color, (int(self.x), int(self.y)), int(self.r))

    def new_score(self, balls_bullet):
        '''
        если мышкой попали по кружочку, даётся 1 очко

        ball - кружочек
        balls_bullet - массив кружочков-снарядов

        '''
        for elem in balls_bullet:
            if (elem.r + self.r)**2 >= ((self.x - elem.x)**2 + (self.y - elem.y)**2):
                # удаляем все кружочки
                Game.delite()
                # возвращаем 1 - кол-во очков за убитый кружочек
                return 1
            else:
                # не попали
                return 0



class Gun():
    '''Gun - объект-пушка'''
    def __init__(self):
        self.b0 = 30
        self.b = self.b0
        self.color = WHITE
        self.x, self.y = 10, 400
        self.t = 0
        self.time = 0

    def draw(self, balls_bullet):
        '''
        рисует пушку

        balls_bullet - массив кружочков-снарядов

        '''
        # если кнопка зажата, то увеличиваем длину пушки
        if Mouse.p:
            # ограничитель длинны
            if self.t < dt * 200:
                # увеличиваем длину
                self.t += dt
                self.b = self.b * (1 + 0.005 * self.t)
        else:
            # если t не равно 0, то был произведён выстрел
            if self.t != 0:
                # если игра не закончилась, то создаём кружочек-снаряд и увеличиваем кол-во попыток
                if not Game.p:
                    Game.n += 1
                    Game.new_ball_bullet(screen, balls_bullet)
                    self.t = 0
            self.b = self.b0
        # поворачиваем пушку по направению к мышке и рисуем
        c_x = self.b * np.cos(self.arctan()) + self.x
        c_y = self.b * np.sin(self.arctan()) + self.y
        pygame.draw.line(screen, WHITE, [int(self.x), int(self.y)], [int(c_x), int(c_y)], 10)

    def arctan(self):
        '''
        считает угол между горизанталью и положением мышки

        '''
        x = Mouse.x - self.x
        y = self.y - Mouse.y
        # проверка на случай, когда tg не определён
        if x == 0:
            arctan = - np.pi / 2
        else:
            arctan = - np.arctan(y / x)
        return arctan



class Game():
    '''Game - игра'''
    def __init__(self):
        self.score = 0
        self.n = 0
        self.t0 = 4 * FPS
        self.t = 0
        self.game_time_FPS = 0
        self.game_time0 = 15
        self.game_time = self.game_time0
        self.p = False
        self.time_target0 = 6 * FPS
        self.time_target = self.time_target0

    def new_ball_bullet(self, screen, balls_bullet):
        '''
        создаёт новый кружочек-снаряд

        screen - экран
        balls - массив кружочков-снарядов

        '''
        x = Gun.x + Gun.b * np.cos(Gun.arctan())
        y = Gun.y + Gun.b * np.sin(Gun.arctan())
        v = Gun.t * 75
        v_x = v * np.cos(Gun.arctan())
        v_y = v * np.sin(Gun.arctan())
        color = COLORS[randint(0, 5)]
        balls_bullet.append(Ball(x, y, v_x, v_y, 10, color))
        balls_bullet[len(balls_bullet) - 1].ball(screen)

    def new_ball_target(self, screen, balls_target):
        '''
        создаёт новый кружочек-мишень

        screen - экран
        balls - массив кружочков-мишений

        '''
        # создаём новый кружочек так, чтобы он не попал в другие кружочки
        k = 0
        while k == 0:
            # рандомные координаты центра и радиус
            x = float(randint(100, 300))
            y = float(randint(100, 300))
            r = float(randint(10, 50))
            # проверяем положение кружочка
            k1 = 0
            for ball in balls_target:
                if (x - ball.x)**2 + (y - ball.y)**2 <= (r + ball.r)**2:
                    k1 = 1
            # если он не наложился, выходим из цикла
            if k1 == 0:
                k = 1
        # рандомные координаты скорости и цвет
        v_x = float(randint(-10, 10)) * 5
        v_y = float(randint(-10, 10)) * 5
        color = COLORS[randint(0, 5)]
        # запись в массив нового кружочка(последнее число в массиве -  время жизни)
        balls_target.append(Ball(x, y, v_x, v_y, r, color, life=10*FPS, g=0))
        # рисование нового кружочков
        balls_target[len(balls_target) - 1].ball(screen)

    def game_score(self, balls_bullet, balls_target):
        '''
        считает очки(в данном случае проверяет попали в цель или нет)

        balls_bullet - массив кружочков-снарядов
        balls_target - массив кружочков-мишений

        '''
        # проверяем все мишений
        if len(balls_bullet) != 0:
            for ball in balls_target:
                score_i = ball.new_score(balls_bullet)
                # если попали, то обновляем переменные для вывода очков
                if score_i != 0:
                    self.score += score_i
                    # сколько вермени будет висеть результат
                    self.t = self.t0
                    self.game_time = 0
                    # флажок-Попал
                    self.p = True

    def delite(self):
        '''
        удаляет все объекты на экране

        balls_bullet - массив кружочков-снарядов
        balls_target - массив кружочков-мишений

        '''
        global balls_bullet
        global balls_target
        balls_bullet = []
        balls_target = []


    def game_screen(self, screen, balls_target):
        '''
        вывод на экран

        screen - экран
        balls_target - массив кружочков-мишений

        '''
        # время и кол-во попыток
        f0 = pygame.font.Font(None, 36)
        text0 = f0.render('попытки: {}'.format(self.n), 5, WHITE)
        screen.blit(text0, (5, 5))

        f0 = pygame.font.Font(None, 36)
        text0 = f0.render('время: {}'.format(self.game_time), 5, WHITE)
        screen.blit(text0, (5, 30))

        # кружочек мышки
        circle(screen, WHITE, (Mouse.x, Mouse.y), 5)

        # пушка
        Gun.draw(balls_bullet)

        # вывод результата, если попали или закончилось время
        if self.p == True:
            if self.score != 0: 
                # если попали
                f0 = pygame.font.Font(None, 36)
                text0 = f0.render('Вы справились за {} выстрелов'.format(self.n), 5, WHITE)
                screen.blit(text0, (50, 100))
            else:
                # если не попали
                f0 = pygame.font.Font(None, 36)
                text0 = f0.render('Вы проиграли', 5, WHITE)
                screen.blit(text0, (150, 100))
            # время
            self.t -= 1
            if self.t == 0:
                # если время вышло, обновляем параметры для следующей игры
                self.n = 0
                self.game_time = self.game_time0
                self.score = 0
                self.p = False
                self.time_target = self.time_target0

    def game(self, screen, balls_bullet, balls_target):
        '''
        тело игры

        screen - экран
        balls_bullet - массив кружочков-снарядов
        balls_target - массив кружочков-мишений

        '''
        # проверка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEMOTION:
                # запись новых координат мышки(если она подвинулась)
                Mouse.x, Mouse.y = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                # кнопка зажата
                Mouse.p = True
            if event.type == pygame.MOUSEBUTTONUP:
                # кнопка отжата
                Mouse.p = False

        # перемещение всех кружочков
        for ball in balls_bullet:
            ball.trance(screen, ball, balls_bullet)
        for ball in balls_target:
            ball.trance(screen, ball, balls_target)
        # если мешений нет и игра не закончена, создание одной мишени
        if len(balls_target) == 0 and not self.p:
            Game.new_ball_target(screen, balls_target)
        # созднаие мешени каждые time_target0
        if self.time_target == 0 and not self.p:
            Game.new_ball_target(screen, balls_target)
            self.time_target0
        self.time_target -= 1

        # вывод всего на экран
        Game.game_screen(screen, balls_target)

        # обновление очков
        Game.game_score(balls_bullet, balls_target)

        # посчёт оставшегося времени
        if not self.p:
            if self.game_time_FPS == FPS:
                self.game_time -= 1
                self.game_time_FPS = 0
            self.game_time_FPS += 1

        # игра окончена, если game_time закончилось
        if self.game_time == 0 and not self.p:
            self.t = self.t0
            self.game_time = 0
            self.p = True
            # удаление всех объектов
            self.delite()

        # обновление экрана
        pygame.display.update()
        screen.fill(BLACK)
        return False



class Mouse():
    '''Mouse - объект-мышка'''
    def __init__(self):
        self.x = 0
        self.y = 0
        self.p = False



Mouse = Mouse()
Gun = Gun()
Game = Game()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    finished = Game.game(screen, balls_bullet, balls_target)

pygame.quit()