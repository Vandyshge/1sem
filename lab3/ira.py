import pygame
from pygame.draw import *
from random import randint

# picture №17

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 700))


# цвета
WHITE = (255, 255, 255)
GRAY1 = (190, 190, 190)
GRAY2 = (230, 230, 230)
YELLOW = (253, 233, 16)
ALLIEN = (187, 255, 51)
ALLIEN_0 = (187, 240, 40)
BLACK = (0, 0, 0)
GREEN = (0, 230, 0)
WHITE_GRAY = (250, 250, 250)
SKY = (8, 30, 69)
GROUND = (18, 53, 36)
MOON = (253, 245, 230)


def nlo(screen, x, y, k):
    '''
    рисование нло
    screen - дисплей, на который выводится изображение
    x, y - координаты центра
    k - коэффициент размера картинки

    '''
    # смещаем координаты для удобства
    x, y = x - int(250 * k) / 2, y - int(50 * k) / 2
    
    # поверхность для того чтобы сделать отрегулировать прозрачность сопла
    treu = pygame.Surface((int(240 * k), int(150 * k)))
    
    # задаём цвет фона
    treu.fill(WHITE)
    
    # прозрачный слой(Все пиксели, цвет которых совпадает с переданным в set_colorkey() значением, станут прозрачными)
    treu.set_colorkey(WHITE)
    
    # сопло нло
    pygame.draw.polygon(treu, WHITE_GRAY, [(int(125 * k), 0), (int(240 * k), int(150 * k)), (int(10 * k), int(150 * k))])
    
    # прозрачность сопла
    treu.set_alpha(100) 
    
    # наложение сопла
    screen.blit(treu, (x, y)) 

    # тело нло
    pygame.draw.ellipse(screen, GRAY1, (x, y ,int(250 * k), int(75 * k)))
    pygame.draw.ellipse(screen, GRAY1, (int(x + 30 * k), int(y - 15 * k), int(190 * k), int(60 * k)))
    
    # иллюминаторы
    pygame.draw.ellipse(screen, YELLOW, (int(x + 110 * k), int(y + 50 * k), int(30 * k), int(18 * k)))
    pygame.draw.ellipse(screen, YELLOW, (int(x + 60 * k), int(y + 45 * k) ,int(30 * k), int(18 * k)))
    pygame.draw.ellipse(screen, YELLOW, (int(x + 160 * k), int(y + 45 * k),int(30 * k), int(18 * k)))
    pygame.draw.ellipse(screen, YELLOW, (int(x + 15 * k), int(y + 30 * k) ,int(30 * k), int(18 * k)))
    pygame.draw.ellipse(screen, YELLOW, (int(x + 210 * k), int(y + 30 * k) ,int(30 * k), int(18 * k)))


def alien(screen, x, y, k, m):
    '''
    рисование пришельца
    screen - дисплей, на который выводится изображение
    x, y - координаты центра
    k - коэффициент размера картинки
    m - (False) - нормальная ориентация, (True) - обратная 

    '''
    
    # поверхность, на которой рисуется пришелец
    al = pygame.Surface((int(600), int(700)))

    # задаём цвет фона
    al.fill(WHITE)

    # прозрачный слой(Все пиксели, цвет которых совпадает с переданным в set_colorkey() значением, станут прозрачными)
    al.set_colorkey(WHITE)

    #рандомный цвет для некоторых деталий
    surprise = (randint(128, 255), randint(0, 128), 0)

    # тело
    pygame.draw.ellipse(al, ALLIEN_0, (x, y, int(k * 50), int(k * 105)))

    # левая рука
    pygame.draw.ellipse(al, ALLIEN, (int(x - 30 * k), int(y + 5 * k), int(k * 40), int(k * 40)))  
    pygame.draw.ellipse(al, ALLIEN, (int(x - 42 * k), int(y + 35 * k), int(k * 25), int(k * 25)))
    pygame.draw.ellipse(al, ALLIEN, (int(x - 35 * k), int(y + 55 * k), int(k * 20), int(k * 20)))
    
    # правая рука
    pygame.draw.ellipse(al, ALLIEN, (int(x + 47 * k), int(y + 5 * k), int(k * 40), int(k * 40)))  
    pygame.draw.ellipse(al, ALLIEN, (int(x + 70 * k), int(y + 35 * k), int(k * 25), int(k * 25)))
    pygame.draw.ellipse(al, ALLIEN, (int(x + 88 * k), int(y + 50 * k), int(k * 25), int(k * 17)))
    
    # яблоко
    pygame.draw.circle(al, surprise, [int(x + 120 * k), int(y + 45 * k)], int(k * 22))  
    pygame.draw.line(al, BLACK, [int(x + 125 * k), int(y + 30 * k)], [int(x + 130 * k), int(y + 15*k)], 2)
    pygame.draw.polygon(al, GREEN, [(int(x + 126 * k), int(y + 19 * k)), (int(x + 138 * k), int(y + 10 * k)), (int(x + 132 * k),int(y + 15 * k))])
    
    # левая нога
    pygame.draw.ellipse(al, ALLIEN, (int(x - 15 * k), int(y + 75 * k), int(k * 40), int(k * 40)))  
    pygame.draw.ellipse(al, ALLIEN, (int(x - 20 * k), int(y + 105 * k), int(k * 30), int(k * 30)))
    pygame.draw.ellipse(al, ALLIEN, (int(x - 22 * k), int(y + 125 * k), int(k * 20), int(k * 20)))
    pygame.draw.ellipse(al, surprise, (int(x - 20 * k), int(y + 145 * k), int(k * 27), int(k * 15)))
    
    # правая нога
    pygame.draw.ellipse(al, ALLIEN, (int(x + 30 * k), int(y + 75 * k), int(k * 40), int(k * 40)))  
    pygame.draw.ellipse(al, ALLIEN, (int(x + 40 * k), int(y + 105 * k), int(k * 30), int(k * 30)))
    pygame.draw.ellipse(al, ALLIEN, (int(x + 38 * k), int(y + 125 * k), int(k * 20), int(k * 20)))
    pygame.draw.ellipse(al, surprise, (int(x + 40 * k), int(y + 145 * k), int(k * 27), int(k * 15)))
    
    # голова
    image  = pygame.image.load('head.png')  
    image.set_colorkey(WHITE)
    image = pygame.transform.scale(image, (int(150 * k), int(146 * k)))
    image_rect=image.get_rect(topleft=(int(x - 63 * k), int(y - 125 * k)))
    al.blit(image, image_rect)

    #left corn
    pygame.draw.circle(al, ALLIEN, [int(x - 30 * k), int(y - 95 * k)], int(k * 12))  
    pygame.draw.circle(al, surprise, [int(x - 40 * k), int(y - 110 * k)], int(k * 8))
    
    #left corn
    pygame.draw.circle(al, ALLIEN, [int(x + 20 * k), int(y - 113 * k)], int(k * 12))  
    pygame.draw.circle(al, surprise, [int(x + 15 * k), int(y - 131 * k)], int(k * 8))
    
    #ориентация пришельца
    if not m: 
        
        #обратная ориентация
        al = pygame.transform.flip(al, True,False)
    
    # добавление шришельца на диспелй
    screen.blit(al, (0, 0))


def fog(screen, x, y, a, b, k):
    '''
    рисование тумана в небе
    screen - дисплей, на который выводится изображение
    x, y - координаты центра
    a, b - размеры тумана
    k - коэффициент размера картинки

    '''
    # рисование тумана с ореолом 
    for i in range(100, 1, -1):
        # размерный коэфициент
        i *= 0.01

        # поверхность, на которой рисуется туман
        fog = pygame.Surface((int(600), int(700)))

        # задаём цвет фона
        fog.fill(BLACK)

        # прозрачный слой(Все пиксели, цвет которых совпадает с переданным в set_colorkey() значением, станут прозрачными)
        fog.set_colorkey(BLACK)

        # размеры i-ого тумана
        a_i, b_i = int(i * k * a), int(i * k * b)

        # i-ый туман
        pygame.draw.ellipse(fog, WHITE, (x + int(k * a) / 2, y + int(k * b) / 2, a_i, b_i))

        # коэффициент прозрачности
        fog.set_alpha(3)

        # вставляем i-ый туман
        screen.blit(fog, (x + int(k * a) / 2 - int(a_i / 2), y + int(k * b) / 2 - int(b_i / 2)))



# фон(небо, земля)
pygame.draw.polygon(screen, SKY, [(0, 0), (600, 0), (600, 400), (0, 400)])
pygame.draw.polygon(screen, GROUND, [(0, 400), (600, 400), (600,700), (0, 700)])

# луна
pygame.draw.circle(screen, MOON, [450, 100], 60)

# небо
fog(screen, 30, 30, 600, 60, 1)
fog(screen, -10, 70, 600, 60, 1)
fog(screen, -150, 120, 600, 60, 1)
fog(screen, -300, 0, 600, 60, 1)
fog(screen, -75, 150, 600, 60, 1)
fog(screen, -300, 40, 600, 60, 1)
fog(screen, -400, 155, 600, 60, 1)
fog(screen, -345, 85, 600, 60, 1)
fog(screen, 10, -10, 600, 60, 1)

# элементы
nlo(screen, 40, 300, 1)
nlo(screen, 450, 300, 0.7)
nlo(screen, 100, 450, 0.8)
alien(screen, 300, 400, 1, False)
alien(screen, 450, 500, 0.8, False)
alien(screen, 450, 600, 0.5, True)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()