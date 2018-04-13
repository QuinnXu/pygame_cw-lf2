### cha1 attack function ### attack ###

import pygame
from pygame.sprite import Sprite

### attack is realized by small model shooting ###
class Attack2(Sprite):
    def __init__(self, screen, cha2):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load('image/attack.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centery = cha2.rect.centery
        self.rect.left = cha2.rect.centerx

        self.x = float(self.rect.x)

        self.speed_factor = 8

    def update(self):
        self.x += self.speed_factor
        self.rect.x = self.x

    


