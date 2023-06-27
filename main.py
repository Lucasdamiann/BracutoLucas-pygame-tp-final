import sys
import pygame
from constants import *
from player import Player
from platforms import Platform
from character import Character
from enemy import Enemy
from auxiliar import Auxiliar
screen = pygame.display.set_mode((WINDOWS_WIDTH,WINDOWS_HEIGHT))
pygame.init()
clock = pygame.time.Clock()
bg_image = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER+SELECTED_BG),(WINDOWS_WIDTH,WINDOWS_HEIGHT))
player_1 = Player(move_x=0,move_y=0,position_x=1,position_y=600,direction=DIRECTION_R,speed_walk=5,speed_run=15,power_jump=50,amount_gravity=14,frame_rate_ms=60,move_rate_ms=50,p_scale=0.15)
enemy_list = []
enemy_1 = Enemy(move_x=0,move_y=0,position_x=900,position_y=600,direction=DIRECTION_L,speed_walk=1,speed_run=2,power_jump=35,amount_gravity=14,frame_rate_ms=90,move_rate_ms=25,p_scale=0.1,attack_on=False,walk_on=False,run_on=False,jump_on=False)
enemy_2 = Enemy(move_x=0,move_y=0,position_x=700,position_y=600,direction=DIRECTION_R,speed_walk=2,speed_run=3,power_jump=35,amount_gravity=14,frame_rate_ms=90,move_rate_ms=25,p_scale=0.1,attack_on=False,walk_on=False,run_on=False,jump_on=False)
enemy_list.append(enemy_1)
enemy_list.append(enemy_2)
platform_list = []
plataforma_1 = Platform(position_x=450,position_y=650,width=100,height=50)
plataforma_2 = Platform(position_x=600,position_y=650,width=100,height=50)
platform_list.append(plataforma_1)
platform_list.append(plataforma_2)
while True:
    pass    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit        
 
    delta_ms = clock.tick(FPS)
    pressed_key = pygame.key.get_pressed() 
    player_1.events(pressed_key)
    screen.blit(bg_image,bg_image.get_rect())
    player_1.update(delta_ms,platform_list,enemy_list)
    enemy_1.update(delta_ms,platform_list)
    enemy_2.update(delta_ms,platform_list)

    for enemy in enemy_list:
        enemy.draw(screen)
    
    for platform in platform_list:
         platform.draw(screen)
    
    player_1.draw(screen)
    pygame.display.flip()
    
