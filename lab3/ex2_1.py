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
	pygame.draw.ellipse(screen, (255, 250, 232), (x, y, 170, 80))
	pygame.draw.ellipse(screen, (255, 250, 232), (x + 100, y - 70, 100, 40))
	pygame.draw.ellipse(screen, (255, 250, 232), (x + 100, y - 85, 70, 60))

	pygame.draw.ellipse(screen, (251, 0, 255), (x + 128, y - 75, 20, 16))
	pygame.draw.ellipse(screen, (255, 250, 232), (x + 100, y - 85, 10, 10))
	pygame.draw.ellipse(screen, (0, 0, 0), (x + 99, y - 86, 5, 5))



# tree(50, 200)
unicorn(200, 200)

# pygame.draw.circle(screen, (0, 0, 0), (200, 200), 100, 3)
# pygame.draw.circle(screen, (255, 0, 0), (160, 170), 30, 0)
# pygame.draw.circle(screen, (255, 0, 0), (240, 170), 20, 0)
# pygame.draw.circle(screen, (0, 0, 0), (160, 170), 30, 1)
# pygame.draw.circle(screen, (0, 0, 0), (240, 170), 20, 1)
# pygame.draw.circle(screen, (0, 0, 0), (160, 170), 10, 0)
# pygame.draw.circle(screen, (0, 0, 0), (240, 170), 10, 0)
# pygame.draw.polygon(screen, (0, 0, 0), [(210, 174), (300, 60), (290, 50), (200, 164)])
# pygame.draw.polygon(screen, (0, 0, 0), [(190, 160), (200, 150), (60, 60), (50, 70)])
# pygame.draw.rect(screen, (0, 0, 0), (150, 240, 100, 20))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()