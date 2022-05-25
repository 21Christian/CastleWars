import pygame
from Constants import *

class Tower(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.Spara = False
        self.shootTimer = 0
        if player == 1:
            self.image = pygame.image.load('player1/building/tower.png')
            self.rect = self.image.get_rect(midbottom = (WALL_POS, 250 - GROUND_HEIGHT))
        elif player == 2:
            self.image = pygame.image.load('player2/building/tower.png')
            self.rect = self.image.get_rect(midbottom=(1000 - WALL_POS, 250 - GROUND_HEIGHT))

    def update(self):
        self.shootTimer += 1
        if self.shootTimer >= TOWER_REST:
            self.shootTimer = 0
            self.Spara = False