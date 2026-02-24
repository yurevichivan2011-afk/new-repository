import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    pygame.display.flip()
pygame.quit()

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Движущийся квадрат')
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

rect_size = 50
x = WIDTH
y = HEIGHT
speed_x = 5
speed_y = 5

x += speed_x
y += speed_y

if x + rect_size > WIDTH or x < 0:
    speed_x = -speed_x
if y + rect_size > HEIGHT or y < 0:
    speed_y = -speed_y

rect_size = 50
x = WIDTH
y = HEIGHT
speed_x = 5
speed_y = 5

screen.fill(BLACK)
pygame.draw.rect(screen, BLUE, (x, y, rect_size))
pygame.display.flip()
pygame.quit()
