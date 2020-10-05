import pygame
from pygame.draw import *
from random import randint

# picture №17

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 700))

def nlo(screen, x, y, k):
    '''
    рисование нло
    screen - дисплей, на который выводится изображение
    x, y - координаты центра
    k - коэффициент размера картинки

    (255, 255, 255) - белый
    (190, 190, 190), (230, 230, 230) - серый
    (253, 233, 16) - жёлтый

    '''
    # смещаем координаты для удобства
    x, y = x - int(250 * k) / 2, y - int(50 * k) / 2
    
    # поверхность для того чтобы сделать отрегулировать прозрачность сопла
    treu = pygame.Surface((int(240 * k), int(150 * k)))
    
    # задаём цвет фона
    treu.fill((255, 255, 255))
    
    # прозрачный слой(Все пиксели, цвет которых совпадает с переданным в set_colorkey() значением, станут прозрачными)
    treu.set_colorkey((255, 255, 255))
    
    # сопло нло
    pygame.draw.polygon(treu, (250, 250, 250), [(int(125 * k), 0), (int(240 * k), int(150 * k)), (int(10 * k), int(150 * k))])
    
    # прозрачность сопла
    treu.set_alpha(100) 
    
    # наложение сопла
    screen.blit(treu, (x, y)) 

    # тело нло
    pygame.draw.ellipse(screen, (190, 190, 190), (x, y ,int(250 * k), int(75 * k)))
    pygame.draw.ellipse(screen, (230, 230, 230), (int(x + 30 * k), int(y - 15 * k), int(190 * k), int(60 * k)))
    
    # иллюминаторы
    pygame.draw.ellipse(screen, (253, 233, 16), (int(x + 110 * k), int(y + 50 * k), int(30 * k), int(18 * k)))
    pygame.draw.ellipse(screen, (253, 233, 16), (int(x + 60 * k), int(y + 45 * k) ,int(30 * k), int(18 * k)))
    pygame.draw.ellipse(screen, (253, 233, 16), (int(x + 160 * k), int(y + 45 * k),int(30 * k), int(18 * k)))
    pygame.draw.ellipse(screen, (253, 233, 16), (int(x + 15 * k), int(y + 30 * k) ,int(30 * k), int(18 * k)))
    pygame.draw.ellipse(screen, (253, 233, 16), (int(x + 210 * k), int(y + 30 * k) ,int(30 * k), int(18 * k)))

def alien(screen, x, y, k, m):
    '''
    рисование пришельца
    screen - дисплей, на который выводится изображение
    x, y - координаты центра
    k - коэффициент размера картинки
    m - (1) - нормальная ориентация, (-1) - обратная 

    (255, 255, 255) - белый
    (190, 190, 190), (230, 230, 230) - серый
    (253, 233, 16) - жёлтый

    (187, 240, 51) - зелёно-жёлтый
    (187, 255, 51) - зелёно-жёлтый

    '''
    
    # поверхность, на которой рисуется пришелец
    al = pygame.Surface((int(600), int(700)))

    # задаём цвет фона
    al.fill((255, 255, 255))

    # прозрачный слой(Все пиксели, цвет которых совпадает с переданным в set_colorkey() значением, станут прозрачными)
    al.set_colorkey((255, 255, 255))

    #рандомный цвет для некоторых деталий
    surprise = (randint(128, 255), randint(0, 128), 0)

    # тело
    pygame.draw.ellipse(al, (187, 240, 51), (x, y, int(k * 50), int(k * 105)))

    # левая рука
    pygame.draw.ellipse(al, (187, 255, 51), (int(x - 30 * k), int(y + 5 * k), int(k * 40), int(k * 40)))  
    pygame.draw.ellipse(al, (187, 255, 51), (int(x - 42 * k), int(y + 35 * k), int(k * 25), int(k * 25)))
    pygame.draw.ellipse(al, (187, 255, 51), (int(x - 35 * k), int(y + 55 * k), int(k * 20), int(k * 20)))
    
    # правая рука
    pygame.draw.ellipse(al, (187, 255, 51), (int(x + 47 * k), int(y + 5 * k), int(k * 40), int(k * 40)))  
    pygame.draw.ellipse(al, (187, 255, 51), (int(x + 70 * k), int(y + 35 * k), int(k * 25), int(k * 25)))
    pygame.draw.ellipse(al, (187, 255, 51), (int(x + 88 * k), int(y + 50 * k), int(k * 25), int(k * 17)))
    
    # яблоко
    pygame.draw.circle(al, surprise, [int(x + 120 * k), int(y + 45 * k)], int(k * 22))  
    pygame.draw.line(al, (0, 0, 0), [int(x + 125 * k), int(y + 30 * k)], [int(x + 130 * k), int(y + 15*k)], 2)
    pygame.draw.polygon(al, (0, 230, 0), [(int(x + 126 * k), int(y + 19 * k)), (int(x + 138 * k), int(y + 10 * k)), (int(x + 132 * k),int(y + 15 * k))])
    
    # левая нога
    pygame.draw.ellipse(al, (187, 255, 51), (int(x - 15 * k), int(y + 75 * k), int(k * 40), int(k * 40)))  
    pygame.draw.ellipse(al, (187, 255, 51), (int(x - 20 * k), int(y + 105 * k), int(k * 30), int(k * 30)))
    pygame.draw.ellipse(al, (187, 255, 51), (int(x - 22 * k), int(y + 125 * k), int(k * 20), int(k * 20)))
    pygame.draw.ellipse(al, surprise, (int(x - 20 * k), int(y + 145 * k), int(k * 27), int(k * 15)))
    
    # правая нога
    pygame.draw.ellipse(al, (187, 255, 51), (int(x + 30 * k), int(y + 75 * k), int(k * 40), int(k * 40)))  
    pygame.draw.ellipse(al, (187, 255, 51), (int(x + 40 * k), int(y + 105 * k), int(k * 30), int(k * 30)))
    pygame.draw.ellipse(al, (187, 255, 51), (int(x + 38 * k), int(y + 125 * k), int(k * 20), int(k * 20)))
    pygame.draw.ellipse(al, surprise, (int(x + 40 * k), int(y + 145 * k), int(k * 27), int(k * 15)))
    
    # голова
    image  = pygame.image.load('head.png')  
    image.set_colorkey((255, 255, 255))
    image = pygame.transform.scale(image, (int(150 * k), int(146 * k)))
    image_rect=image.get_rect(topleft=(int(x - 63 * k), int(y - 125 * k)))
    al.blit(image, image_rect)

    #left corn
    pygame.draw.circle(al, (187, 255, 51), [int(x - 30 * k), int(y - 95 * k)], int(k * 12))  
    pygame.draw.circle(al, surprise, [int(x - 40 * k), int(y - 110 * k)], int(k * 8))
    
    #left corn
    pygame.draw.circle(al, (187, 255, 51), [int(x + 20 * k), int(y - 113 * k)], int(k * 12))  
    pygame.draw.circle(al, surprise, [int(x + 15 * k), int(y - 131 * k)], int(k * 8))
    
    #ориентация пришельца
    if (m == -1): 
        
        #обратная ориентация
        al = pygame.transform.flip(al, True,False)
    
    # добавление шришельца на диспелй
    screen.blit(al, (0, 0))

def fog(screen, x, y, k):
    '''
    рисование тумана в небе
    screen - дисплей, на который выводится изображение
    x, y - координаты центра
    k - коэффициент размера картинки

    (255, 255, 255) - белый

    '''

    # поверхность, на которой рисуется туман
    fog = pygame.Surface((int(600), int(700)))

    # задаём цвет фона
    fog.fill((0, 0, 0))

    # прозрачный слой(Все пиксели, цвет которых совпадает с переданным в set_colorkey() значением, станут прозрачными)
    fog.set_colorkey((0, 0, 0))

    for i in range(100, 1, -1):
        i *= 0.01

        pygame.draw.ellipse(fog, (255, 255, 255), (int(x + i * k * 100), int(y - i * k * 15), int(i * k * 200), int(i * k * 30)))

        fog.set_alpha(3)

        screen.blit(fog, (x, y))



# фон(небо, земля)
pygame.draw.polygon(screen, (8, 30, 69), [(0, 0), (600, 0), (600, 400), (0, 400)])
pygame.draw.polygon(screen, (18, 53, 36), [(0, 400), (600, 400), (600,700), (0, 700)])

# луна
pygame.draw.circle(screen, (253, 245, 230), [450, 100], 60)

# небо
fog(screen, 100, 100, 1)
# image  = pygame.image.load('clouds2.jpg')
# image.set_colorkey((255, 255, 255))
# image = pygame.transform.scale(image, (600, 400))
# image_rect = image.get_rect()
# image.set_alpha(100)
# screen.blit(image, image_rect)

# элементы
# nlo(40, 300, 1)
# nlo(400, 400, 0.7)
# nlo(70, 450, 0.8)
# alien(300, 400, 1, 1)
# alien(450, 500, 0.8, 1)
# alien(450, 600, 0.5, -1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()