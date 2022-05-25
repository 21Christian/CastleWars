import pygame
from Constants import *

t_arrow1 = []
t_arrow1.append(pygame.image.load('player1/bow/arrowdiag-0.png'))

class TowerArrow1(pygame.sprite.Sprite):
    def __init__(self, t_arrow1):
        super().__init__()

        self.index = 0
        self.image = t_arrow1[self.index]
        self.rect = self.image.get_rect(center =(WALL_POS, 250 - TOWER_HEIGHT))

    def update(self):
        self.rect.x += 6
        self.rect.y += 4