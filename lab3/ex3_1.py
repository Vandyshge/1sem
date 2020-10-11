import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((450, 610))

#10 kartinka

screen.fill((0, 235, 247))
pygame.draw.rect(screen, (2, 250, 15), (0, 300, 450, 310))

pygame.draw.circle(screen, (250, 217, 2), (430, 30), 100, 0)

def tree(x, y, a):
    pygame.draw.rect(screen, (189, 189, 189), (x, y, 30 * a, 150 * a)) #stvol
    pygame.draw.rect(screen, (237, 197, 128), (x, y, 30 * a, 150 * a), 2) 

    pygame.draw.ellipse(screen, (47, 161, 48), (x - 40 * a, y - 20 * a, 110 * a, 100 * a)) #listva
    pygame.draw.ellipse(screen, (36, 255, 105), (x - 40 * a, y - 20 * a, 110 * a, 100 * a), 2)

    pygame.draw.ellipse(screen, (47, 161, 48), (x - 50 * a, y - 200 * a, 130 * a, 200 * a))
    pygame.draw.ellipse(screen, (36, 255, 105), (x - 50 * a, y - 200 * a, 130 * a, 200 * a), 2)

    pygame.draw.ellipse(screen, (47, 161, 48), (x - 90 * a, y - 100 * a, 200 * a, 110 * a))
    pygame.draw.ellipse(screen, (36, 255, 105), (x - 90 * a, y - 100 * a, 200 * a, 110 * a), 2)

    pygame.draw.ellipse(screen, (173, 144, 40), (x - 55 * a, y - 30 * a, 20 * a, 20 * a))
    pygame.draw.ellipse(screen, (173, 144, 40), (x - 10 * a, y - 100 * a, 20 * a, 20 * a))
    pygame.draw.ellipse(screen, (173, 144, 40), (x + 45 * a, y - 150 * a, 20 * a, 20 * a))
    pygame.draw.ellipse(screen, (173, 144, 40), (x + 20 * a, y, 20 * a, 20 * a))


def unicorn(x, y, a):
    pygame.draw.ellipse(screen, (255, 250, 232), (x, y, 170 * a, 80 * a)) #body
    pygame.draw.ellipse(screen, (255, 250, 232), (x + 100 * a, y - 70 * a, 100 * a, 33 * a)) #nose
    pygame.draw.ellipse(screen, (255, 250, 232), (x + 100 * a, y - 85 * a, 70 * a, 50 * a)) #head

    pygame.draw.ellipse(screen, (251, 0, 255), (x + 133 * a, y - 73 * a, 18 * a, 15 * a)) #glas
    pygame.draw.ellipse(screen, (0, 0, 0), (x + 143 * a, y - 70 * a, 7 * a, 7 * a)) #crachek
    pygame.draw.ellipse(screen, (255, 250, 232), (x + 137 * a, y - 70 * a, 7 * a, 3 * a)) #blik

    pygame.draw.polygon(screen, (130, 164, 245), [(x + 140 * a,  y - 83 * a), (x + 140 * a, y - 170 * a), (x + 125 * a, y - 83 * a)]) # rog
    pygame.draw.rect(screen, (255, 250, 232), (x + 100 * a, y - 50 * a, 50 * a, 100 * a)) # neck

    pygame.draw.rect(screen, (255, 250, 232), (x + 137 * a, y + 30 * a, 11 * a, 100 * a)) # leg
    pygame.draw.rect(screen, (255, 250, 232), (x + 107 * a, y + 40 * a, 13 * a, 100 * a))
    pygame.draw.rect(screen, (255, 250, 232), (x + 60 * a, y + 33 * a, 12 * a, 100 * a))
    pygame.draw.rect(screen, (255, 250, 232), (x + 25 * a, y + 37 * a, 13 * a, 100 * a))

    pygame.draw.ellipse(screen, (162, 161, 255), (x + 85 * a, y - 80 * a, 35 * a, 15 * a)) #griva
    pygame.draw.ellipse(screen, (130, 189, 245), (x + 95 * a, y - 90 * a, 40 * a, 18 * a))
    pygame.draw.ellipse(screen, (222, 154, 237), (x + 90 * a, y - 85 * a, 30 * a, 13 * a))
    pygame.draw.ellipse(screen, (130, 245, 237), (x + 80 * a, y - 74 * a, 25 * a, 17 * a))
    pygame.draw.ellipse(screen, (162, 161, 255), (x + 70 * a, y - 70 * a, 35 * a, 15 * a))
    pygame.draw.ellipse(screen, (130, 189, 245), (x + 65 * a, y - 55 * a, 35 * a, 20 * a))
    pygame.draw.ellipse(screen, (222, 154, 237), (x + 70 * a, y - 60 * a, 33 * a, 15 * a))
    pygame.draw.ellipse(screen, (130, 245, 237), (x + 70 * a, y - 35 * a, 35 * a, 10 * a))
    pygame.draw.ellipse(screen, (222, 154, 237), (x + 68 * a, y - 18 * a, 40 * a, 25 * a))
    pygame.draw.ellipse(screen, (162, 161, 255), (x + 48 * a, y - 7 * a, 60 * a, 15 * a))
    pygame.draw.ellipse(screen, (130, 189, 245), (x + 69 * a, y - 29 * a, 37 * a, 25 * a))
    pygame.draw.ellipse(screen, (222, 154, 237), (x + 72 * a, y - 32 * a, 50 * a, 15 * a))
    pygame.draw.ellipse(screen, (162, 161, 255), (x + 68 * a, y - 42 * a, 40 * a, 17 * a))

    pygame.draw.ellipse(screen, (162, 161, 255), (x - 10 * a, y + 10 * a, 50 * a, 25 * a)) #hvost
    pygame.draw.ellipse(screen, (222, 154, 237), (x - 20 * a, y + 25 * a, 40 * a, 18 * a))
    pygame.draw.ellipse(screen, (130, 189, 245), (x - 25 * a, y + 35 * a, 43 * a, 19 * a))
    pygame.draw.ellipse(screen, (222, 154, 237), (x - 23 * a, y + 47 * a, 50 * a, 25 * a))
    pygame.draw.ellipse(screen, (130, 245, 237), (x - 27 * a, y + 62 * a, 45 * a, 19 * a))
    pygame.draw.ellipse(screen, (162, 161, 255), (x - 30 * a, y + 75 * a, 52 * a, 25 * a))
    pygame.draw.ellipse(screen, (222, 154, 237), (x - 43 * a, y + 90 * a, 43 * a, 20 * a))
    pygame.draw.ellipse(screen, (130, 245, 237), (x - 30 * a, y + 95 * a, 48 * a, 25 * a))
    pygame.draw.ellipse(screen, (130, 189, 245), (x - 35 * a, y + 107 * a, 43 * a, 15 * a))

def sun():
    for i in range(100, 10, -0.1):
        pygame.draw.circle(screen, (250, 217, 2), (350, 100), 100, 1)


tree(50, 300, 0.5)
tree(100, 250, 0.75)
tree(150, 300, 0.57)
tree(20, 350, 1)
tree(35, 400, 0.5)
unicorn(200, 450, 1)
unicorn(250, 250, 0.5)




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()