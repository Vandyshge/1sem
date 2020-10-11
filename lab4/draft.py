import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
side = 400
screen = pygame.display.set_mode((side, side))



# Начальная позиция прямоугольника
rect_x = 50
 
# -------- Цикл главной программы -----------
while done==False:
    for event in pygame.event.get(): # Пользователь что-то сделал
        if event.type == pygame.QUIT: # Если пользователь щёлкнул на кнопки закрытия
            done=True # Поставить значение done, чтобы выйти из цикла
 
    # Установить фон окна
    screen.fill(black)
 
    pygame.draw.rect(screen,white,[rect_x,50,50,50])
    rect_x += 1