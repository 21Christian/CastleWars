import pygame
from Constants import *

t_arrow2 = []
t_arrow2.append(pygame.image.load('player2/bow/arrowdiag-0.png'))


class TowerArrow2(pygame.sprite.Sprite):
    def __init__(self, t_arrow2):
        super().__init__()

        self.index = 0
        self.image = t_arrow2[self.index]
        self.rect = self.image.get_rect(center=(1000 - WALL_POS, 250 - TOWER_HEIGHT))

    def update(self):
        self.rect.x -= 6
        self.rect.y += 4