### cha2 bullet function ### skill ###

import pygame
from pygame.sprite import Sprite

class Bullet2(Sprite):

    def __init__(self,screen,cha2):

        super().__init__()
        self.screen = screen

        self.image = pygame.image.load('image/bullet_cha2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centery = cha2.rect.centery
        self.rect.left = cha2.rect.right

        self.x=float(self.rect.x)
        ### ball speed ###
        self.speed_factor = 10

    def update(self):

        self.x+=self.speed_factor
        self.rect.x=self.x

    def draw_bullet(self):
        self.screen.blit(self.image,self.rect)
