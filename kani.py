import pygame
import time
import random

pygame.init()
width, height = 600, 400
block_size = 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (213, 50, 80)
blue = (50, 153, 213)

clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 30)

def draw_score(score):
    value = score_font.render("Score: " + str(score), True, red)
    screen.blit(value, [0, 0])

def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], block_size, block_size])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

def game_loop():
    game_over = False
    game_close = False
    x = width / 2
    y = height / 2
    dx = 0
    dy = 0
    snake = []
    length = 1
    food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
    speed = 15

    while not game_over:
        while game_close:
            screen.fill(black)
            message("You lost! Press Q to Quit or R to Restart", red)
            draw_score(length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -block_size
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = block_size
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dy = -block_size
                    dx = 0
                elif event.key == pygame.K_DOWN and dy == 0:
                    dy = block_size
                    dx = 0

        x += dx
        y += dy

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        screen.fill(blue)
        pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])

        snake_head = [x, y]
        snake.append(snake_head)

        if len(snake) > length:
            del snake[0]

        for segment in snake[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(block_size, snake)
        draw_score(length - 1)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            length += 1
            speed += 0.5

        clock.tick(speed)

    pygame.quit()
    quit()

game_loop()
