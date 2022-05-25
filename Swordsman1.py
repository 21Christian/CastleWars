import pygame
from Constants import *
from random import randint

swordsman1_ready = pygame.image.load('player1/sword/ready.png')

swordsman1_run = []
swordsman1_run.append(pygame.image.load('player1/sword/run-0.png'))
swordsman1_run.append(pygame.image.load('player1/sword/run-1.png'))
swordsman1_run.append(pygame.image.load('player1/sword/run-2.png'))
swordsman1_run.append(pygame.image.load('player1/sword/run-3.png'))
swordsman1_run.append(pygame.image.load('player1/sword/run-4.png'))
swordsman1_run.append(pygame.image.load('player1/sword/run-5.png'))
swordsman1_run.append(pygame.image.load('player1/sword/run-6.png'))
swordsman1_run.append(pygame.image.load('player1/sword/run-7.png'))
swordsman1_run.append(pygame.image.load('player1/sword/run-8.png'))
swordsman1_run.append(pygame.image.load('player1/sword/run-9.png'))
swordsman1_run.append(pygame.image.load('player1/sword/run-10.png'))
swordsman1_run.append(pygame.image.load('player1/sword/run-11.png'))

swordsman1_attack = []
swordsman1_attack.append(pygame.image.load('player1/sword/attack-0.png'))
swordsman1_attack.append(pygame.image.load('player1/sword/attack-1.png'))
swordsman1_attack.append(pygame.image.load('player1/sword/attack-2.png'))
swordsman1_attack.append(pygame.image.load('player1/sword/attack-3.png'))
swordsman1_attack.append(pygame.image.load('player1/sword/attack-4.png'))
swordsman1_attack.append(pygame.image.load('player1/sword/attack-5.png'))
swordsman1_attack.append(pygame.image.load('player1/sword/attack-6.png'))
swordsman1_attack.append(pygame.image.load('player1/sword/attack-7.png'))

swordsmasn1_dead = []
swordsmasn1_dead.append(pygame.image.load('player1/sword/fallen-0.png'))
swordsmasn1_dead.append(pygame.image.load('player1/sword/fallen-1.png'))
swordsmasn1_dead.append(pygame.image.load('player1/sword/fallen-2.png'))
swordsmasn1_dead.append(pygame.image.load('player1/sword/fallen-3.png'))
swordsmasn1_dead.append(pygame.image.load('player1/sword/fallen-4.png'))
swordsmasn1_dead.append(pygame.image.load('player1/sword/fallen-5.png'))





class Swordsman1(pygame.sprite.Sprite):

    def __init__(self, ready, run, attack, dead):
        super().__init__()

        # Attributes
        self.ready = ready
        self.run_sprites = run
        self.attack_sprites = attack
        self.dead_sprites = dead
        self.image = self.ready
        self.rect = self.image.get_rect(midbottom = (randint(55 , 157), 250 - GROUND_HEIGHT))
        self.health = SWORD_HEALTH
        # Phase
        self.unleash = False
        self.attacking = False
        self.tic = 0
        self.index = 0
        self.time = 0

    def update(self):
        if self.health <= 0:
            self.tic += 1
            if self.tic >= 6:
                self.index += 0.5
                self.tic = 0
            if self.index >= len(self.dead_sprites):
                self.index = 0
                self.kill()
            self.image = self.dead_sprites[int(self.index)]

        elif self.time < SWORD_TRAIN:
            self.time += 1
        else:
            # do running Animation
            if self.unleash == True:
                self.tic += 1
                if self.tic >= 6:
                    self.index += 1
                    self.tic = 0
                if self.index >= len(self.run_sprites):
                    self.index = 0
                self.image = self.run_sprites[self.index]
                self.rect.x += SWORD_SPEED
                #do attacking animation
            elif self.attacking == True:
                self.tic += 1
                if self.tic >= 6:
                    self.index += 1
                    self.tic = 0
                if self.index >= len(self.attack_sprites):
                    self.index = 0
                self.image = self.attack_sprites[self.index]



