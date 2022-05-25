import pygame
from Constants import *
from random import *

archer2_ready = pygame.image.load('player2/bow/ready.png')

archer2_run = []
archer2_run.append(pygame.image.load('player2/bow/run-0.png'))
archer2_run.append(pygame.image.load('player2/bow/run-1.png'))
archer2_run.append(pygame.image.load('player2/bow/run-2.png'))
archer2_run.append(pygame.image.load('player2/bow/run-3.png'))
archer2_run.append(pygame.image.load('player2/bow/run-4.png'))
archer2_run.append(pygame.image.load('player2/bow/run-5.png'))
archer2_run.append(pygame.image.load('player2/bow/run-6.png'))
archer2_run.append(pygame.image.load('player2/bow/run-7.png'))
archer2_run.append(pygame.image.load('player2/bow/run-8.png'))
archer2_run.append(pygame.image.load('player2/bow/run-9.png'))
archer2_run.append(pygame.image.load('player2/bow/run-10.png'))
archer2_run.append(pygame.image.load('player2/bow/run-11.png'))

archer2_shoot = []
archer2_shoot.append(pygame.image.load('player2/bow/shoot-0.png'))
archer2_shoot.append(pygame.image.load('player2/bow/shoot-1.png'))

archer2_dead = []
archer2_dead.append(pygame.image.load('player2/bow/fallen-0.png'))
archer2_dead.append(pygame.image.load('player2/bow/fallen-1.png'))
archer2_dead.append(pygame.image.load('player2/bow/fallen-2.png'))
archer2_dead.append(pygame.image.load('player2/bow/fallen-3.png'))
archer2_dead.append(pygame.image.load('player2/bow/fallen-4.png'))
archer2_dead.append(pygame.image.load('player2/bow/fallen-5.png'))


class Archer2(pygame.sprite.Sprite):
    def __init__(self, ready, run, shoot, dead):
        super().__init__()

        # Attributes
        self.ready = ready
        self.run_sprites = run
        self.shoot_sprites = shoot
        self.dead_sprites = dead
        self.image = self.ready
        self.rect = self.image.get_rect(midbottom = (randint(1000 - BARRACKS_POS - 20, 1000 - BARRACKS_POS + 20), 250 - GROUND_HEIGHT))
        self.health = ARCHER_HEALTH
        # Phase
        self.unleash = False
        self.shoot = False
        self.shootFlag = False
        self.tic = 0
        self.index = 0
        self.time = 0

    def update(self):

        if self.time < ARCHER_TRAIN:
            self.time += 1
        elif self.health <= 0:
            self.tic += 1
            if self.tic >= 6:
                self.index += 0.5
                self.tic = 0
            if self.index >= len(self.dead_sprites):
                self.index = 0
                self.kill()
            self.image = self.dead_sprites[int(self.index)]

        else:
            # do running Animation
            if self.unleash == True:
                self.tic += 1
                if self.tic >= 6:
                    self.index += 1
                    self.tic = 0
                if self.index >= len(self.run_sprites):
                    self.index = 0
                self.image = self.run_sprites[int(self.index)]
                self.rect.x -= ARCHER_SPEED
            # do attacking animation
            elif self.shoot == True:

                self.tic += 1
                if self.tic >= 6:
                    self.index += 0.2
                    self.tic = 0
                if self.index >= len(self.shoot_sprites):
                    self.index = 0
                    self.shootFlag = False
                self.image = self.shoot_sprites[int(self.index)]