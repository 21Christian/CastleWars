import pygame
from Constants import *

a_arrow1 = []
a_arrow1.append(pygame.image.load('player1/bow/arrowhor-0.png'))


class ArcherArrow1(pygame.sprite.Sprite):
    def __init__(self, a_arrow1, position):
        super().__init__()
        self.index = 0
        self.position = position
        self.image = a_arrow1[self.index]
        self.rect = self.image.get_rect(midbottom=(self.position, SCREEN_HEIGHT - 23))

    def update(self):
        self.rect.x += ARROW_SPEED

