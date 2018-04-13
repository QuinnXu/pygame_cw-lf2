### Cha1 blood function ###

import pygame

from pygame.sprite import Sprite

class Blood1:

    def __init__(self,screen):

        super().__init__()

        self.screen = screen

        self.rect = pygame.Rect(0,0,350,25) # initiall blood setting #

        self.rect.left = 90
        self.rect.top = 30

        self.color = (225,0,0)

    def draw_blood(self):
        pygame.draw.rect(self.screen,self.color,self.rect)


        
