import pygame
from Constants import *
from random import randint

# Worker Stand
worker2_ready = pygame.image.load('player2/worker/ready.png')

# Worker Running to the dig
worker2_run_left = []
worker2_run_left.append(pygame.transform.flip(pygame.image.load('player2/worker/run-0.png'), True, False))
worker2_run_left.append(pygame.transform.flip(pygame.image.load('player2/worker/run-1.png'), True, False))
worker2_run_left.append(pygame.transform.flip(pygame.image.load('player2/worker/run-2.png'), True, False))
worker2_run_left.append(pygame.transform.flip(pygame.image.load('player2/worker/run-3.png'), True, False))
worker2_run_left.append(pygame.transform.flip(pygame.image.load('player2/worker/run-4.png'), True, False))
worker2_run_left.append(pygame.transform.flip(pygame.image.load('player2/worker/run-5.png'), True, False))

# Worker Running to the mine
worker2_run_right = []
worker2_run_right.append(pygame.image.load('player2/worker/run-0.png'))
worker2_run_right.append(pygame.image.load('player2/worker/run-1.png'))
worker2_run_right.append(pygame.image.load('player2/worker/run-2.png'))
worker2_run_right.append(pygame.image.load('player2/worker/run-3.png'))
worker2_run_right.append(pygame.image.load('player2/worker/run-4.png'))
worker2_run_right.append(pygame.image.load('player2/worker/run-5.png'))

# Worker Digging
worker2_dig = []
worker2_dig.append(pygame.transform.flip(pygame.image.load('player2/worker/dig-0.png'), True, False))
worker2_dig.append(pygame.transform.flip(pygame.image.load('player2/worker/dig-1.png'), True, False))
worker2_dig.append(pygame.transform.flip(pygame.image.load('player2/worker/dig-2.png'), True, False))
worker2_dig.append(pygame.transform.flip(pygame.image.load('player2/worker/dig-3.png'), True, False))
worker2_dig.append(pygame.transform.flip(pygame.image.load('player2/worker/dig-4.png'), True, False))
worker2_dig.append(pygame.transform.flip(pygame.image.load('player2/worker/dig-5.png'), True, False))
worker2_dig.append(pygame.transform.flip(pygame.image.load('player2/worker/dig-6.png'), True, False))
worker2_dig.append(pygame.transform.flip(pygame.image.load('player2/worker/dig-7.png'), True, False))
worker2_dig.append(pygame.transform.flip(pygame.image.load('player2/worker/dig-8.png'), True, False))

# Worker Repairing
worker2_repair = []
worker2_repair.append(pygame.image.load('player2/worker/repair-0.png'))
worker2_repair.append(pygame.image.load('player2/worker/repair-1.png'))
worker2_repair.append(pygame.image.load('player2/worker/repair-2.png'))
worker2_repair.append(pygame.image.load('player2/worker/repair-3.png'))


class Worker2(pygame.sprite.Sprite):

    def __init__(self, ready, run_right, run_left, dig, repair):
        super().__init__()

        # Attributes
        self.ready = ready
        self.run_left_sprites = run_left
        self.run_right_sprites = run_right
        self.dig_sprites = dig
        self.repair_sprites = repair

        self.image = self.ready
        self.rect = self.image.get_rect(midbottom=(1000 - randint(75 , 137) , 250 - GROUND_HEIGHT))
        # Phase
        self.run_left = False
        self.run_right = False
        self.dig = False
        self.repair = False

        self.tic = 0
        self.index = 0
        self.time = 0

    def update(self):
        self.time += 1

        # Animation running to mine
        if self.time > WORKER_TRAIN and self.dig == False and self.run_right == True and self.repair == False:
            self.tic += 1
            if self.tic == 6:
                self.index += 1
                self.tic = 0
            if self.index >= len(self.run_right_sprites):
                self.index = 0

            self.rect.x += WORKER_SPEED
            self.image = self.run_right_sprites[self.index]

        # Animation running to wall
        if self.time > 100 and self.dig == False and self.run_left == True and self.repair == False:
            self.tic += 1
            if self.tic == 6:
                self.index += 1
                self.tic = 0
            if self.index >= len(self.run_left_sprites):
                self.index = 0

            self.rect.x -= WORKER_SPEED
            self.image = self.run_left_sprites[self.index]

        # Animation for Digging
        if self.dig == True:
            self.tic += 1
            if self.tic == 6:
                self.index += 1
                self.tic = 0
            if self.index >= len(self.dig_sprites):
                self.index = 0

            self.image = self.dig_sprites[self.index]

        # Animation for Repairing
        if self.repair == True:
            self.tic += 1
            if self.tic == 6:
                self.index += 1
                self.tic = 0
            if self.index >= len(self.repair_sprites):
                self.index = 0

            self.image = self.repair_sprites[self.index]