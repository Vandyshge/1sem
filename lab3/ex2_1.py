import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((450, 610))

screen.fill((0, 235, 247))
pygame.draw.rect(screen, (2, 250, 15), (0, 300, 450, 310))

pygame.draw.circle(screen, (250, 217, 2), (430, 30), 100, 0)

def tree(x, y):
	pygame.draw.rect(screen, (189, 189, 189), (x, y, 30, 150))
	pygame.draw.ellipse(screen, (47, 161, 48), (x - 40, y - 20, 110, 100))
	pygame.draw.ellipse(screen, (47, 161, 48), (x - 90, y - 100, 200, 110))
	pygame.draw.ellipse(screen, (47, 161, 48), (x - 50, y - 200, 130, 200))

	pygame.draw.ellipse(screen, (173, 144, 40), (x - 55, y - 30, 20, 20))
	pygame.draw.ellipse(screen, (173, 144, 40), (x - 10, y - 100, 20, 20))
	pygame.draw.ellipse(screen, (173, 144, 40), (x + 45, y - 150, 20, 20))
	pygame.draw.ellipse(screen, (173, 144, 40), (x + 20, y, 20, 20))

def unicorn(x, y):
	pygame.draw.ellipse(screen, (255, 250, 232), (x, y, 170, 80)) #body
	pygame.draw.ellipse(screen, (255, 250, 232), (x + 100, y - 70, 100, 33)) #nose
	pygame.draw.ellipse(screen, (255, 250, 232), (x + 100, y - 85, 70, 50)) #head

	pygame.draw.ellipse(screen, (251, 0, 255), (x + 133, y - 73, 18, 15)) #glas
	pygame.draw.ellipse(screen, (0, 0, 0), (x + 143, y - 70, 7, 7)) #crachek
	pygame.draw.ellipse(screen, (255, 250, 232), (x + 137, y - 70, 7, 3)) #blik

	pygame.draw.polygon(screen, (130, 164, 245), [(x + 140,  y - 83), (x + 140, y - 170), (x + 125, y - 83)]) # rog
	pygame.draw.rect(screen, (255, 250, 232), (x + 100, y - 50, 50, 100)) # neck

	pygame.draw.rect(screen, (255, 250, 232), (x + 137, y + 30, 11, 100)) # leg
	pygame.draw.rect(screen, (255, 250, 232), (x + 107, y + 40, 13, 100))
	pygame.draw.rect(screen, (255, 250, 232), (x + 60, y + 33, 12, 100))
	pygame.draw.rect(screen, (255, 250, 232), (x + 25, y + 37, 13, 100))

	pygame.draw.ellipse(screen, (162, 161, 255), (x + 85, y - 80, 35, 15)) #griva
	pygame.draw.ellipse(screen, (130, 189, 245), (x + 95, y - 90, 40, 18))
	pygame.draw.ellipse(screen, (222, 154, 237), (x + 90, y - 85, 30, 13))
	pygame.draw.ellipse(screen, (130, 245, 237), (x + 80, y - 74, 25, 17))
	pygame.draw.ellipse(screen, (162, 161, 255), (x + 70, y - 70, 35, 15))
	pygame.draw.ellipse(screen, (130, 189, 245), (x + 65, y - 55, 35, 20))
	pygame.draw.ellipse(screen, (222, 154, 237), (x + 70, y - 60, 33, 15))
	pygame.draw.ellipse(screen, (130, 245, 237), (x + 70, y - 35, 35, 10))
	pygame.draw.ellipse(screen, (222, 154, 237), (x + 68, y - 18, 40, 25))
	pygame.draw.ellipse(screen, (162, 161, 255), (x + 48, y - 7, 60, 15))
	pygame.draw.ellipse(screen, (130, 189, 245), (x + 69, y - 29, 37, 25))
	pygame.draw.ellipse(screen, (222, 154, 237), (x + 72, y - 32, 50, 15))
	pygame.draw.ellipse(screen, (162, 161, 255), (x + 68, y - 42, 40, 17))

	pygame.draw.ellipse(screen, (162, 161, 255), (x - 10, y + 10, 50, 25)) #hvost
	pygame.draw.ellipse(screen, (222, 154, 237), (x - 20, y + 25, 40, 18))
	pygame.draw.ellipse(screen, (130, 189, 245), (x - 25, y + 35, 43, 19))
	pygame.draw.ellipse(screen, (222, 154, 237), (x - 23, y + 47, 50, 25))
	pygame.draw.ellipse(screen, (130, 245, 237), (x - 27, y + 62, 45, 19))
	pygame.draw.ellipse(screen, (162, 161, 255), (x - 30, y + 75, 52, 25))
	pygame.draw.ellipse(screen, (222, 154, 237), (x - 43, y + 90, 43, 20))
	pygame.draw.ellipse(screen, (130, 245, 237), (x - 30, y + 95, 48, 25))
	pygame.draw.ellipse(screen, (130, 189, 245), (x - 35, y + 107, 43, 15))






tree(50, 200)
unicorn(150, 300)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()