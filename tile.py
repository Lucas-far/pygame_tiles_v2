

import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill(tile_color)
        self.rect = self.image.get_rect(center=pos)
