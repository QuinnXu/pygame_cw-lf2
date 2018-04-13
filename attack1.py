### cha1 attack function ### attack ###

import pygame
from pygame.sprite import Sprite

### attack is realized by small model shooting ###
class Attack1(Sprite):
    def __init__(self, screen, cha1):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load('image/attack.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centery = cha1.rect.centery
        self.rect.right = cha1.rect.centerx

        self.x = float(self.rect.x)

        self.speed_factor = 8

    def update(self):
        self.x -= self.speed_factor
        self.rect.x = self.x

   


