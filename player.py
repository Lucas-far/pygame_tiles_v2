

import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.Surface((tile_size / 2, tile_size * 2))
        self.image.fill(player_color)
        self.rect = self.image.get_rect(center=pos)
