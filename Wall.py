import pygame
from Constants import *


class Wall(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        if player == 1:
            self.image = pygame.image.load('player1/building/wall.png')
            self.rect = self.image.get_rect(midbottom = (WALL_POS, 250 - GROUND_HEIGHT))
        elif player == 2:
            self.image = pygame.image.load('player2/building/wall.png')
            self.rect = self.image.get_rect(midbottom=(1000 - WALL_POS, 250 - GROUND_HEIGHT))