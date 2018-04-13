### cha1 function ### player2 ###

import pygame
from pygame.sprite import Sprite

class Cha1(Sprite):

    def __init__(self,screen):

        super().__init__()
        
        self.screen = screen
        self.image = pygame.image.load('image/cha1.png')
        self.rect = self.image.get_rect() 
        self.screen_rect = screen.get_rect()

        self.rect.centerx = 900 ### initial location ###
        self.rect.bottom = 530

        self.center = float(self.rect.centerx)
        self.player_start_y = self.rect.centery

        ### image lanch ###

        self.moving_right = False # move right #
        self.moving_left = False # move left #
        self.moving_up = False # jump #
        self.bullet = False # shoot bullet #
        self.fire = False # shoot ball #
        self.attack = False # attack #

        #self.bigone = False ### ult skill not added ###

        self.jump_vel = 0.0
        self.current_frame = 0
        self.last_update = 0

       
      
    def update(self,cha2):
        now = pygame.time.get_ticks()
        # image list #
        cha1_f=[pygame.image.load('image/cha1f1.png'),
               pygame.image.load('image/cha1f2.png'),
               pygame.image.load('image/cha1f3.png'),
               pygame.image.load('image/cha1f4.png'),
               pygame.image.load('image/cha1f5.png'),
               pygame.image.load('image/cha1f6.png')]

        cha1_a = [pygame.image.load('image/cha1a1.png'),
                  pygame.image.load('image/cha1a2.png'),
                  pygame.image.load('image/cha1a3.png'),
                  pygame.image.load('image/cha1a4.png'),
                  pygame.image.load('image/cha1a5.png'),]

        cha1_w =[pygame.image.load('image/cha1.png'),
                pygame.image.load('image/cha1walk.png')]

        cha1_b = [pygame.image.load('image/cha1bullet1.png'),
                  pygame.image.load('image/cha1bullet2.png'),
                  pygame.image.load('image/cha1bullet3.png'),]

        #       cha1_ult=[pygame.image.load('image/ult1_cha1.png'),   ### ult skill not added ###
        #               pygame.image.load('image/ult2_cha1.png'),
        #            pygame.image.load('image/ult3_cha1.png')]
        
        ### walk speed ###
        if self.moving_right and self.rect.right<=1000:
            self.center += 10
            if now - self.last_update > 150:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % 2
                self.image = cha1_w[self.current_frame]

        if self.moving_left and self.rect.left>=cha2.rect.right:
            self.center -= 10
            if now - self.last_update > 150:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % 2
                self.image = cha1_w[self.current_frame]
            
        if self.attack:
            self.center += 5
            if now - self.last_update > 90:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % 5
                self.image = cha1_a[self.current_frame]

        if self.fire:
            self.center -= 0
            if now - self.last_update > 90:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % 5
                self.image = cha1_f[self.current_frame]

        if self.bullet:
            self.center += 0
            if now - self.last_update > 150:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % 3
                self.image = cha1_b[self.current_frame]


       
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
                self.image=pygame.image.load('image/cha1.png')
         
        self.rect.centerx= self.center

    #        if self.bigone: ### ult skill not added ###
    #            self.center-=0
    #            if now - self.last_update > 300:
    #                self.last_update = now
    #                self.current_frame = (self.current_frame + 1) % 3
    #                self.image = cha1_ult[self.current_frame]
    #                self.rect = self.image.get_rect()
    #
    #                self.rect.centerx = 500
    #                self.rect.bottom = 540

    def blitme(self):
        self.screen.blit(self.image,self.rect)
