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


# массив кружочков
balls_bullet = []
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
        circle(screen, self.color, (self.x, self.y), self.r)

    def new_score(self, ball):
        '''
        если мышкой попали по кружочку, даётся 1 очко

        x_m, y_m - координаты мышки
        ball - кружочек
        balls - массив кружочков

        '''
        for elem in balls_bullet:
            if (elem.r + self.r)**2 >= ((self.x - elem.x)**2 + (self.y - elem.y)**2):
                # удаляем умерший кружочек
                self.delite(ball, balls_target)
                elem.delite(elem, balls_bullet)
                Game.delite()
                # возвращаем 1 - кол-во очков за убитый кружочек
                return 1
            else:
                # не попали
                return 0



class Gun():
    def __init__(self):
        # self.a0 = 10
        self.b0 = 30
        # self.a = self.a0
        self.b = self.b0
        self.color = WHITE
        self.x, self.y = 10, 400
        self.t = 0
        self.time = 0

    def draw(self):
        if Mouse.p:
            if self.t < dt * 200:
                self.t += dt
                self.b = self.b * (1 + 0.005 * self.t)
        else:
            if self.t != 0:
                if not Game.p:
                    Game.n += 1
                    Game.new_ball_bullet(screen, balls_bullet)
                    self.t = 0
            self.b = self.b0
        # g = pygame.Surface((self.b, self.a))
        # g.fill(WHITE)
        # g.set_colorkey(BLACK)
        # rect(g, self.color, (0, 0, self.b, self.a))
        # g = pygame.transform.rotate(g, self.arctan())
        # screen.blit(g, (self.x, self.y))
        c_x = self.b * np.cos(self.arctan()) + self.x
        c_y = self.b * np.sin(self.arctan()) + self.y
        pygame.draw.line(screen, WHITE, [self.x, self.y], [c_x, c_y], 10)

    def arctan(self):
        x = Mouse.x - self.x
        y = self.y - Mouse.y
        return - np.arctan(y / x)



class Game():
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
        x = Gun.x + Gun.b * np.cos(Gun.arctan())
        y = Gun.y + Gun.b * np.sin(Gun.arctan())
        v = Gun.t * 75
        v_x = v * np.cos(Gun.arctan())
        v_y = v * np.sin(Gun.arctan())
        color = COLORS[randint(0, 5)]
        balls_bullet.append(Ball(x, y, v_x, v_y, 10, color))
        balls_bullet[len(balls_bullet) - 1].ball(screen)

    def new_ball_target(self, screen, balls_target):
        x = randint(200, 450)
        y = randint(50, 450)
        r = randint(5, 50)
        v_x = float(randint(-10, 10)) * 5
        v_y = float(randint(-10, 10)) * 5
        color = COLORS[randint(0, 5)]
        balls_target.append(Ball(x, y, v_x, v_y, r, color, life=10*FPS, g=0))
        balls_target[len(balls_target) - 1].ball(screen)

    def game_score(self):
        if len(balls_bullet) != 0:
            for ball in balls_target:
                score_i = ball.new_score(ball)
                if score_i != 0:
                    self.score += score_i
                    self.t = self.t0
                    self.game_time = 0
                    self.p = True

    def delite(self):
        global balls_bullet
        global balls_target
        balls_bullet = []
        balls_target = []


    def game_screen(self):
        f0 = pygame.font.Font(None, 36)
        text0 = f0.render('попытки: {}'.format(self.n), 5, WHITE)
        screen.blit(text0, (5, 5))

        f0 = pygame.font.Font(None, 36)
        text0 = f0.render('время: {}'.format(self.game_time), 5, WHITE)
        screen.blit(text0, (5, 30))

        for ball in balls_target:
            ball.ball(screen)

        circle(screen, WHITE, (Mouse.x, Mouse.y), 5)

        Gun.draw()

        if self.p == True:
            if self.score != 0: 
                f0 = pygame.font.Font(None, 36)
                text0 = f0.render('Вы спарвились за {} выстрелов'.format(self.n), 5, WHITE)
                screen.blit(text0, (50, 100))
            else:
                f0 = pygame.font.Font(None, 36)
                text0 = f0.render('Вы проиграли', 5, WHITE)
                screen.blit(text0, (150, 100))
            self.t -= 1
            print(self.t)
            if self.t == 0:
                self.n = 0
                self.game_time = self.game_time0
                self.score = 0
                self.p = False
                self.time_target = self.time_target0

    def game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEMOTION:
                Mouse.x, Mouse.y = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                Mouse.p = True
            if event.type == pygame.MOUSEBUTTONUP:
                Mouse.p = False

        for ball in balls_bullet:
            ball.trance(screen, ball, balls_bullet)
        for ball in balls_target:
            ball.trance(screen, ball, balls_target)

        if len(balls_target) == 0 and not self.p:
            Game.new_ball_target(screen, balls_target)

        if self.time_target == 0 and not self.p:
            Game.new_ball_target(screen, balls_target)
            self.time_target0
        self.time_target -= 1

        Game.game_screen()

        Game.game_score()

        if not self.p:
            if self.game_time_FPS == FPS:
                self.game_time -= 1
                self.game_time_FPS = 0
            self.game_time_FPS += 1

        if self.game_time == 0 and not self.p:
            self.t = self.t0
            self.game_time = 0
            self.p = True
            self.delite()


        pygame.display.update()

        screen.fill(BLACK)

        return False



class Mouse():
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

    finished = Game.game()

pygame.quit()