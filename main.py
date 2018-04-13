### main function ###

import sys
import pygame
import locale
from pygame.sprite import Group
from pygame.locals import *
from settings import Settings
from cha1 import Cha1
from cha2 import Cha2
from blood1 import Blood1
from blood2 import Blood2
from button import Button
import game_functions as gf

def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((1000,600))
    pygame.display.set_caption('Fighter')

    cha1=Cha1(screen)
    bullets1=Group()
    balls1=Group()
    attacks1=Group()
    cha2=Cha2(screen)
    bullets2=Group()
    balls2=Group()
    attacks2=Group()
    blood1=Blood1(screen)
    blood2=Blood2(screen)
    p2_win=False

    bgm=pygame.mixer.music.load('voice/bgm.wav')
    pygame.mixer.music.play(-1,0.0)
    
    clock=pygame.time.Clock()

    button = Button(screen)


    while True:
        clock.tick(250)

        gf.check_events(screen,cha1,cha2,bullets1,bullets2,balls1,balls2,attacks1,attacks2)

        screen.blit(ai_settings.inter_image,[0,0])
        button.blitme()
        button.is_start()
        if button.game_start ==True:
            gf.update_bullets1(bullets1,cha2)
            gf.update_bullets2(bullets2,cha1)
            gf.update_balls1(balls1, cha2)
            gf.update_balls2(balls2, cha1)
            gf.update_attacks1(attacks1, cha1)
            gf.update_attacks2(attacks2, cha2)

            gf.update_blood1(blood1,cha2,bullets1,balls1,cha1,attacks1)
            gf.update_blood2(blood2,cha2,bullets2,balls2,cha1,attacks2)
            gf.inter_ball_bullets(bullets1,bullets2,balls1,balls2)
            gf.inter_bullets(bullets1,bullets2)
            gf.update_cha1(cha1,cha2)
            gf.update_cha2(cha2,bullets1,balls1,cha1)
            screen.blit(ai_settings.bg_image,[0,0])
            gf.update_screen(cha1,cha2,bullets1,bullets2,balls1,balls2,blood1,blood2)


        pygame.display.flip()

       
        
run_game()
