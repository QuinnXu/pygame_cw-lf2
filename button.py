### button function ###

import pygame

class Button():



    def __init__(self, screen):
        super().__init__()
        self.imageUp = pygame.image.load('image/p1.png').convert_alpha()
        self.imageDown = pygame.image.load('image/p2.png').convert_alpha()
        self.position = (500,450)
        self.game_start = False
        self.screen = screen
        
    def isOver(self):
        point_x,point_y = pygame.mouse.get_pos()
        x, y = self. position
        w, h = self.imageUp.get_size()

        in_x = x - w/2 < point_x < x + w/2
        in_y = y - h/2 < point_y < y + h/2
        return in_x and in_y

    def blitme(self):
        w, h = self.imageUp.get_size()
        x, y = self.position
        
        if self.isOver():
            self.screen.blit(self.imageDown, [x-w/2,y-h/2])
        else:
            self.screen.blit(self.imageUp, [x-w/2, y-h/2])
    def is_start(self):
        if self.isOver():
            b1,b2,b3 = pygame.mouse.get_pressed()
            if b1 == 1:
                self.game_start = True

