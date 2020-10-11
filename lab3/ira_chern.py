import pygame
from pygame.draw import *
from random import randint

#  picture №17

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 700))

def alien(screen, x, y, k, m):
    '''
    рисование пришельца
    screen - дисплей, где выводится изображение
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



alien(screen, 300, 400, 1, 1)

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