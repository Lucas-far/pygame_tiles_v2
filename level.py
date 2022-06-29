

import pygame
from settings import *
from tile import Tile
from player import Player


class Level:
    def __init__(self):
        self.canvas = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.setup_level()

    def run(self):
        self.visible_sprites.draw(self.canvas)

    def setup_level(self):
        for row_index, row in enumerate(scenario):
            for col_index, col in enumerate(row):
                # print(f'{col_index}:{row}->{col_index * tile_size}')
                # print(f'{row_index}:{row}->{row_index * tile_size}')
                x = col_index * tile_size
                y = row_index * tile_size
                if col == 'X':
                    Tile((x, y), self.visible_sprites)
                elif col == 'P':
                    Player((x, y), self.visible_sprites)
                # branch mais antiga
