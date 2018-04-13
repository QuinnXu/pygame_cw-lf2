### game function ###

import sys
import pygame
from bullet1 import Bullet1
from cha2 import Cha2
from cha1 import Cha1
from bullet2 import Bullet2
from ball1 import Ball1
from ball2 import Ball2
from attack1 import Attack1
from attack2 import Attack2
from button import Button

######### key down  ########

def check_keydown_event(event,screen,cha1,cha2,bullets1,bullets2,balls1,balls2,attacks1,attacks2):

####### Cha1 control #######

    # move right # right #
    if event.key == pygame.K_RIGHT:
        cha1.moving_right =True

    # move left # left #
    elif event.key == pygame.K_LEFT:
        cha1.moving_left = True

    # jump # up #
    elif event.key == pygame.K_UP: # jump #
        if not cha1.moving_up:
            cha1.moving_up = True
            cha1.jump_vel = -18.0
            cha1.image=pygame.image.load('image/cha1jump.png')

    # attack # b #
    elif event.key == pygame.K_b: # attack
        cha1.attack = True
        fire_attack1(screen, cha1, attacks1)

    # ball # n #
    elif event.key == pygame.K_n:
        cha1.fire = True
        fire_ball1(screen, cha1, balls1)

    # bullet # m #
    elif event.key == pygame.K_m:
        cha1.bullet = True
        pygame.mixer.music.load('voice/ha.wav')
        pygame.mixer.music.play(1,0.0)
        fire_bullet1(screen,cha1,bullets1)

#    elif event.key == pygame.K_l: ### ult skill not added ###
#        cha1.bigone = True



####### Cha2 control #######

    # move right # d #
    elif event.key == pygame.K_d:
        cha2.moving_right =True

    # move left # a #
    elif event.key == pygame.K_a:
        cha2.moving_left = True

    # jump # w #
    elif event.key == pygame.K_w:
        if not cha2.moving_up:
            cha2.moving_up = True
            cha2.jump_vel = -18.0
            cha2.image = pygame.image.load('image/cha2jump.png')

    # attack # f #
    elif event.key == pygame.K_f:
        cha2.attack = True
        fire_attack2(screen, cha2, attacks2)

    # ball # g #
    elif event.key == pygame.K_g:
        fire_ball2(screen, cha2, balls2)
        cha2.fire = True

    # bullet # h #
    elif event.key == pygame.K_h:
        cha2.bullet = True
        pygame.mixer.music.load('voice/ha.wav')
        pygame.mixer.music.play(1,0.0)
        fire_bullet2(screen,cha2,bullets2)


####### skills def function #######

def fire_bullet1(screen,cha1,bullets1):
    if len(bullets1)< 1 : # existing bullet allowance #
        new_bullet1 = Bullet1(screen,cha1)
        bullets1.add(new_bullet1)

def fire_bullet2(screen,cha2,bullets2):
    if len(bullets2)< 1 :
        new_bullet2 = Bullet2(screen,cha2)
        bullets2.add(new_bullet2)

def fire_ball1(screen,cha1,balls1):
    if len(balls1)< 10 : # existing ball allowance #
        new_ball1 = Ball1(screen,cha1)
        balls1.add(new_ball1)

def fire_ball2(screen,cha2,balls2):
    if len(balls2)< 10 :
        new_ball2 = Ball2(screen,cha2)
        balls2.add(new_ball2)

def fire_attack1(screen,cha1,attacks1):
    if len(attacks1)< 1 :
        new_attack1 = Attack1(screen,cha1)
        attacks1.add(new_attack1)

def fire_attack2(screen,cha2,attacks2):
    if len(attacks2)< 1 :
        new_attack2 = Attack2(screen,cha2)
        attacks2.add(new_attack2)

########## key up  #########

def check_keyup_event(event,cha1,cha2):

####### Cha1 control #######

    # move right # right #
    if event.key == pygame.K_RIGHT:
        cha1.moving_right = False
        cha1.image = pygame.image.load('image/cha1.png')

    # move left # left #
    elif event.key == pygame.K_LEFT:
        cha1.moving_left = False
        cha1.image = pygame.image.load('image/cha1.png')

    # jump # up #
    elif event.key == pygame.K_UP:
        cha1.image = pygame.image.load('image/cha1.png')

    # attack # b #
    elif event.key == pygame.K_b:
        cha1.attack = False
        cha1.image = pygame.image.load('image/cha1.png')

    # ball # n #
    elif event.key == pygame.K_n:
        cha1.fire = False
        cha1.image = pygame.image.load('image/cha1.png')

    # bullet # m #
    elif event.key == pygame.K_m:
        cha1.bullet = False
        cha1.image = pygame.image.load('image/cha1.png')

#    elif event.key == pygame.K_l: ### ult skill not added ###
#        cha1.bigone = False
#        cha1.image = pygame.image.load('image/cha1.png')
#        cha1.rect = cha1.image.get_rect()
#        cha1.rect.centerx = 500
#        cha1.rect.bottom = 530
              
####### Cha2 control #######

    # move right # d #
    if event.key == pygame.K_d:
        cha2.moving_right = False
        cha2.image = pygame.image.load('image/cha2.png')

    # move left # a #
    elif event.key == pygame.K_a:
        cha2.moving_left = False
        cha2.image = pygame.image.load('image/cha2.png')

    # jump # up #
    elif event.key == pygame.K_w:
        cha2.image = pygame.image.load('image/cha2.png')

    # attack # f #
    elif event.key == pygame.K_f:
        cha2.attack = False
        cha2.image = pygame.image.load('image/cha2.png')

    # ball # g #
    elif event.key == pygame.K_g:
        cha2.fire = False
        cha2.image = pygame.image.load('image/cha2.png')

    # bullet # h #
    elif event.key == pygame.K_h:
        cha2.bullet = False
        cha2.image = pygame.image.load('image/cha2.png')

### event check ###

def check_events(screen,cha1,cha2,bullets1,bullets2,balls1,balls2,attacks1,attacks2):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys,exit()

        elif event.type == pygame.K_ESCAPE:
            sys,exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,screen,cha1,cha2,bullets1,bullets2,balls1,balls2,attacks1,attacks2)
            
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,cha1,cha2)

####### skill check #######

def update_bullets1(bullets1,cha2):
    bullets1.update()
    for bullet in bullets1.copy():
        if pygame.sprite.collide_circle_ratio(0.55)(cha2,bullet)or bullet.rect.right<=0:
            bullets1.remove(bullet)

def update_bullets2(bullets2,cha1):
    bullets2.update()
    for bullet in bullets2.copy():
        if pygame.sprite.collide_circle_ratio(0.55)(cha1,bullet)or bullet.rect.right>=1000:
            bullets2.remove(bullet)

def update_balls1(balls1,cha2):
    balls1.update()
    for ball in balls1.copy():
        if pygame.sprite.collide_circle_ratio(0.55)(cha2,ball)or ball.rect.right<=0 :
            balls1.remove(ball)

def update_balls2(balls2,cha1):
    balls2.update()
    for ball in balls2.copy():
        if pygame.sprite.collide_circle_ratio(0.55)(cha1,ball)or ball.rect.right>=1000:
                balls2.remove(ball)

def inter_ball_bullets(bullets1,bullets2,balls1,balls2):
    for ball in balls1.copy():
        for bullet in bullets2.copy():
            if pygame.sprite.collide_rect(bullet,ball):
                balls1.remove(ball)
    for ball in balls2.copy():
        for bullet in bullets1.copy():
            if pygame.sprite.collide_rect(bullet,ball):
                balls2.remove(ball)

def inter_bullets(bullets1,bullets2):
    for bullet1 in bullets1.copy():
        for bullet2 in bullets2.copy():
            if pygame.sprite.collide_circle_ratio(1)(bullet1,bullet2):
                bullets1.remove(bullet1)
                bullets2.remove(bullet2)
            

def update_attacks1(attacks1,cha1):
    attacks1.update()
    for attack in attacks1.copy():
        if attack.rect.right<cha1.rect.left:
            attacks1.remove(attack)

def update_attacks2(attacks2,cha2):
    attacks2.update()
    for attack in attacks2.copy():
        if attack.rect.right>cha2.rect.right:
            attacks2.remove(attack)

            
def update_cha1(cha1,cha2):
    cha1.update(cha2)
    
def update_cha2(cha2,bullets1,balls1,cha1):
    cha2.update(cha1)
    
####### blood check #######

def update_blood1(blood1,cha2,bullets1,balls1,cha1,attacks1):
    bullets1.update()
    for bullet in bullets1.copy():
        if pygame.sprite.collide_circle_ratio(0.6)(cha2,bullet):  # bullet damage #
            if blood1.rect.width >= 50:
                blood1.rect.width -= 50
                cha2.image=pygame.image.load('image/cha2gethit.png')
            else:
                cha2.image=pygame.image.load('image/cha2die.png')
                cha2.rect.centerx = 300
                cha2.rect.bottom = 580

    balls1.update()
    for ball in balls1.copy():
        if pygame.sprite.collide_circle_ratio(0.6)(cha2, ball): # ball damage #
            if blood1.rect.width >= 20:
                blood1.rect.width -= 20
                cha2.image = pygame.image.load('image/cha2gethit.png')
            else:
                cha2.image = pygame.image.load('image/cha2die.png')
                cha2.rect.centerx = 300
                cha2.rect.bottom = 580

    attacks1.update()
    for attack in attacks1.copy():
        if pygame.sprite.collide_rect(cha2, attack): # attack damage #
            if blood1.rect.width >= 100:
                blood1.rect.width -= 100
                cha2.image = pygame.image.load('image/cha2gethit.png')
            else:
                cha2.image = pygame.image.load('image/cha2die.png')
                cha2.rect.centerx = 300
                cha2.rect.bottom = 580

                
def update_blood2(blood2,cha2,bullets2,balls2,cha1,attacks2):
    bullets2.update()
    for bullet in bullets2.copy():
        if pygame.sprite.collide_circle_ratio(0.6)(cha1,bullet):
            if blood2.rect.width >= 50:
                blood2.rect.width -= 50
                cha1.image=pygame.image.load('image/cha1gethit.png')
            else:
                cha1.image=pygame.image.load('image/cha1die.png')
                cha1.rect.centerx = 300
                cha1.rect.bottom = 580

    balls2.update()
    for ball in balls2.copy():
        if pygame.sprite.collide_circle_ratio(0.6)(cha1, ball):
            if blood2.rect.width >= 20:
                blood2.rect.width -= 20
                cha1.image = pygame.image.load('image/cha1gethit.png')
            else:
                cha1.image = pygame.image.load('image/cha1die.png')
                cha1.rect.centerx = 300
                cha1.rect.bottom = 580

    attacks2.update()
    for attack in attacks2.copy():
        if pygame.sprite.collide_rect(cha1, attack):
            if blood2.rect.width >= 100:
                blood2.rect.width -= 100
                cha1.image = pygame.image.load('image/cha1gethit.png')
            else:
                cha1.image = pygame.image.load('image/cha1die.png')
                cha1.rect.centerx = 300
                cha1.rect.bottom = 580

        
   
# screen #
def update_screen(cha1,cha2,bullets1,bullets2,balls1,balls2,blood1,blood2):

    for bullet in bullets1.sprites():
        bullet.draw_bullet()
    for bullet in bullets2.sprites():
        bullet.draw_bullet()
    for ball in balls1.sprites():
        ball.draw_ball()
    for ball in balls2.sprites():
        ball.draw_ball()
    
    cha1.blitme()
    cha2.blitme()
    blood1.draw_blood()
    blood2.draw_blood()

    
            
