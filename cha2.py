### cha2 function ### player1 ###

import pygame
from pygame.sprite import Sprite

class Cha2(Sprite):

    def __init__(self,screen):

        super().__init__()

        self.screen = screen
        self.image = pygame.image.load('image/cha2.png')
        self.rect = self.image.get_rect() 
        self.screen_rect = screen.get_rect()

        self.rect.centerx = 100 ### initial location ###
        self.rect.bottom = 530

        self.center = float(self.rect.centerx)
        self.player_start_y = self.rect.centery

        ### image lanch ###

        self.moving_right =False # move right #
        self.moving_left = False # move left #
        self.moving_up = False  # jump #
        self.bullet = False # shoot bullet #
        self.fire = False # shoot ball #
        self.attack = False # attack #

        ### initial value setting ###
        self.jump_vel = 0.0
        self.current_frame = 0
        self.last_update = 0

    def update(self,cha1):
        now = pygame.time.get_ticks()
        # image list #
        cha2_w=[pygame.image.load('image/cha2.png'), # walk images loading #
                pygame.image.load('image/cha2walk.png')]

        cha2_a = [pygame.image.load('image/cha2a1.png'), # attack images loading #
                  pygame.image.load('image/cha2a2.png'),
                  pygame.image.load('image/cha2a3.png'),
                  pygame.image.load('image/cha2a4.png'),]

        cha2_f=[pygame.image.load('image/cha2f1.png'), # shoot ball images loading #
                pygame.image.load('image/cha2f2.png'),
                pygame.image.load('image/cha2f3.png'),
                pygame.image.load('image/cha2f4.png')]

        cha2_b = [pygame.image.load('image/cha2bullet1.png'), # shoot bullet images loading #
                  pygame.image.load('image/cha2bullet2.png'),
                  pygame.image.load('image/cha2bullet3.png'),]

        if self.moving_right and self.rect.right<=cha1.rect.left:
        ### walk speed ###
            self.center+= 10
            if now - self.last_update > 150:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % 2 # present image by frame #
                self.image = cha2_w[self.current_frame]

        if self.moving_left and self.rect.left>=0:
            self.center-= 10
            if now - self.last_update > 150:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % 2
                self.image = cha2_w[self.current_frame]

        ### jump height ###
        if self.moving_up:
            if self.jump_vel < 0:
                self.jump_vel += 0.6
            elif self.jump_vel >= 0:
                self.jump_vel += 6
            self.rect.centery += self.jump_vel
            if self.rect.centery > self.player_start_y:
                self.moving_up = False
                self.rect.centery = self.player_start_y
                self.jump_vel = 0.0

        ### ###
        if self.bullet:
            self.center -= 0
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % 3
                self.image = cha2_b[self.current_frame]

        if self.fire:
            self.center -= 0
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % 4
                self.image = cha2_f[self.current_frame]

        if self.attack:
            self.center -= 1
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % 4
                self.image = cha2_a[self.current_frame]

        self.rect.centerx =self.center

    def blitme(self):

        self.screen.blit(self.image,self.rect)
