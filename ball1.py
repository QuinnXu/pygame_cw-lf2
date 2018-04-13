### cha1 ball function ### skill ###

import pygame
from pygame.sprite import Sprite


class Ball1(Sprite):
    def __init__(self, screen, cha1):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load('image/ball_cha1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centery = cha1.rect.centery
        self.rect.right = cha1.rect.centerx

        self.x = float(self.rect.x)
        ### bullet speed ###
        self.speed_factor = 15

    def update(self):
        self.x -= self.speed_factor
        self.rect.x = self.x

    def draw_ball(self):
        self.screen.blit(self.image, self.rect)


