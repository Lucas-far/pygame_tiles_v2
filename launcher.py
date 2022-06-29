

import pygame
from settings import *
from level import Level

pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

level = Level()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
    screen.fill(bg_color)
    level.run()
    pygame.display.update()
    clock.tick(60)
