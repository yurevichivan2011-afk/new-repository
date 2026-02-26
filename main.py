import pygame
import random

COLOR_WHITE = (255, 0, 0)
COLOR_YELLOW = (255, 255, 102)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (213, 50, 80)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (50, 153, 213)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SNAKE_BLOCK = 10
SNAKE_SPEED = 15

pygame.init()
screen = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)
pygame.display.set_caption('Змейка: Улучшеная версия')

clock = pygame.time.Clock()

font_style = pygame.font.SysFont('bahnschift', 25)
score_font0 = pygame.font.SysFont('comicsansms', 35)

def display_score(score):
    value = score_font.render(f'Ваш счет: {score}', True, COLOR_YELLOW)
    screen.blit(value, [10, 10])

def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, COLOR_BLACK, [x[0], x[1], block_size, block_size])

def show_massage(msg, color):
    mesg = font_style.render(msg, True, color)
    text_rect = mesg.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_WIDTH / 3))
    screen.blit(mesg, text_rect)

def generate_food():
    foodx = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK)) / 10.0) * 10.0
    foody = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK)) / 10.0) * 10.0
    return foodx, foody

def game_loop():
    game_over = False
    game_close = False
    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2
    x1_change = 0
    y1_change = 0

snake_list = []
length_of_snake = 1
foodx, foody, = generate_food()

while not game_over:
    while game_close:
        screen.fill(COLOR_BLUE)
        show_massage('Вы програли! Q - выход, C - играть снова', COLOR_RED)
        display_score(length_of_snake - 1)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game.over = True
                    game_close = False
                     if event.key == pygame.K_q:
                         game.loop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x1_change == 0:
                x1_change = -SNAKE_BLOCK
                y1_change = 0
            elif event