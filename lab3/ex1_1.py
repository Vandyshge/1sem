import pygame
from pygame.draw import *

pygame.init()

FPS = 400
screen = pygame.display.set_mode((400, 400))

screen.fill((125, 125, 125))
pygame.draw.circle(screen, (255, 255, 0), (200, 200), 100, 0)
pygame.draw.circle(screen, (0, 0, 0), (200, 200), 100, 3)
pygame.draw.circle(screen, (255, 0, 0), (160, 170), 30, 0)
pygame.draw.circle(screen, (255, 0, 0), (240, 170), 20, 0)
pygame.draw.circle(screen, (0, 0, 0), (160, 170), 30, 1)
pygame.draw.circle(screen, (0, 0, 0), (240, 170), 20, 1)
pygame.draw.circle(screen, (0, 0, 0), (160, 170), 10, 0)
pygame.draw.circle(screen, (0, 0, 0), (240, 170), 10, 0)
pygame.draw.polygon(screen, (0, 0, 0), [(210, 174), (300, 60), (290, 50), (200, 164)])
pygame.draw.polygon(screen, (0, 0, 0), [(190, 160), (200, 150), (60, 60), (50, 70)])
pygame.draw.rect(screen, (0, 0, 0), (150, 240, 100, 20))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()