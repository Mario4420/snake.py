#!/usr/bin/env python
import pygame
import sys

def main():
    WIDTH  = 600
    HEIGHT  = 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()
    FPS = 60

    running = True

    BG_COLOR = (0, 0, 0)

    while running:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                sys.exit()

        screen.fill(BG_COLOR)
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
