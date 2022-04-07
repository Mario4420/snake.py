#!/usr/bin/env python

import pygame
import sys
import random
from enum import Enum, auto


def main():
    pygame.init()

    SCREEN_WIDTH  = 600
    SCREEN_HEIGHT  = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    FPS = 10

    score = 0
    TEXT_X = 0
    TEXT_Y = 0
    TEXT_COLOR = (255, 255, 255)

    font = pygame.font.SysFont(None, 25)

    running = True

    BG_COLOR = (0, 0, 0)

    PART_SIZE = 30

    SNAKE_COLOR = (255, 0, 0)
    snake = [pygame.Rect(0, 0, PART_SIZE, PART_SIZE)]

    class SNAKE_DIRS(Enum):
        UP = auto()
        DOWN = auto()
        LEFT = auto()
        RIGHT = auto()

    snake_dir = 0

    FRUIT_COLOR = (0, 0, 255)
    fruit = generate_fruit(PART_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT)

    while running:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_w:
                    snake_dir = SNAKE_DIRS.UP

                if e.key == pygame.K_s:
                    snake_dir = SNAKE_DIRS.DOWN

                if e.key == pygame.K_a:
                    snake_dir = SNAKE_DIRS.LEFT

                if e.key == pygame.K_d:
                    snake_dir = SNAKE_DIRS.RIGHT

        screen.fill(BG_COLOR)

        move_snake(snake, SNAKE_DIRS, snake_dir, PART_SIZE)
        if snake[0].colliderect(fruit):
            score += 1
            fruit = generate_fruit(PART_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT)

        draw_snake(screen, SNAKE_COLOR, snake)
        draw_fruit(screen, FRUIT_COLOR, fruit)
        draw_text(screen, TEXT_X, TEXT_Y, font, f"score: {score}", TEXT_COLOR)

        pygame.display.update()
        clock.tick(FPS)


def draw_snake(screen, color, snake):
    for rect in snake:
        pygame.draw.rect(screen, color, rect)


def draw_fruit(screen, color, rect):
    pygame.draw.rect(screen, color, rect)


def draw_text(screen, x, y, font, text, col):
    text = font.render(text, True, col)
    screen.blit(text, (x, y))


def move_snake(snake, snake_dirs, snake_dir, speed):
    for part in snake:
        if snake_dir == snake_dirs.UP:
            part.y -= speed

        if snake_dir == snake_dirs.DOWN:
            part.y += speed

        if snake_dir == snake_dirs.LEFT:
            part.x -= speed

        if snake_dir == snake_dirs.RIGHT:
            part.x += speed


def generate_fruit(fruit_size, screen_width, screen_height):
    return pygame.Rect(random.randrange(0, (screen_width-fruit_size)+1, fruit_size),
                       random.randrange(0, (screen_height-fruit_size)+1, fruit_size),
                       fruit_size,
                       fruit_size)


if __name__ == "__main__":
    main()
