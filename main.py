import json
import sys
import pygame
from constants import *
from player import Player
from platforms import Platform
from enemy import Enemy
from surfaces import Surfaces
from coins import Coin
from button import Button
from potion import Potion
from portal import Portal
pygame.init()
screen = pygame.display.set_mode((WINDOWS_WIDTH,WINDOWS_HEIGHT))
world_data = [
            [9,9,9,9,9,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,8,0,0,5,0,0,10,0,0,0,7,8,0,0,8,8,6,8,8,8,8,0,0,0],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
        ]
world = Surfaces(world_data)

start_button = Button(WINDOWS_WIDTH / 4 ,WINDOWS_HEIGHT / 2,START_BUTTON)
settings_button = Button(WINDOWS_WIDTH / 4 + (start_button.rect.w),WINDOWS_HEIGHT / 2,SET_BUTTON)
scores_button = Button(WINDOWS_WIDTH / 4 + (start_button.rect.w*2),WINDOWS_HEIGHT / 2,SCORE_BUTTON)
credit_button = Button(WINDOWS_WIDTH / 4 + (start_button.rect.w*3),WINDOWS_HEIGHT / 2,CREDIT_BUTTON)
exit_button = Button(WINDOWS_WIDTH / 4 + (start_button.rect.w*4),WINDOWS_HEIGHT / 2,EXIT_BUTTON)
back_button = Button(WINDOWS_WIDTH / 2 - (start_button.rect.w/2),WINDOWS_HEIGHT / 2,BACK_BUTTON)
next_button = Button(WINDOWS_WIDTH / 2 - (start_button.rect.w/2),WINDOWS_HEIGHT / 2,NEXT_BUTTON)
restart_button = Button(WINDOWS_WIDTH / 2 - (start_button.rect.w/2),WINDOWS_HEIGHT / 2,RESTART_BUTTON)

player = Player(move_x=0,move_y=0,position_x=1,position_y=(WINDOWS_HEIGHT/12),direction=DIRECTION_R,speed_walk=5,speed_run=8,power_jump=100,amount_gravity=14,frame_rate_ms=60,move_rate_ms=30,p_scale=0.15)

def credits():
    pygame.display.set_caption("Credits")
    while True:
        screen.fill(C_YELLOW_2)
        settings_text = pygame.font.SysFont("Calibri",35).render("CREDITS",True,C_GREEN)
        settings_rect = settings_text.get_rect(center=(WINDOWS_WIDTH/2,WINDOWS_HEIGHT/5))
        back_button.draw(screen)
        credit_text = pygame.font.SysFont("Calibri",35).render("Creado por Lucas Damian Bracuto",True,C_BLUE)
        screen.blit(settings_text,settings_rect)
        screen.blit(credit_text,(WINDOWS_WIDTH/4,WINDOWS_HEIGHT/3))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.click():
                    main_menu()
                
        pygame.display.update()
        
def score():
    pygame.display.set_caption("Scores")
    pygame.mixer.music.load(SCORE_SCREEN_SOUND)
    pygame.mixer.music.play(-1)
    bg_score = pygame.transform.scale(pygame.image.load(BLUR),(WINDOWS_WIDTH,WINDOWS_HEIGHT))#acelera el juego y consume menos recursos

    while True:
        screen.fill(C_BLUE_2)
        settings_text = pygame.font.SysFont("Calibri",35).render("Scores",True,C_GREEN)
        font = pygame.font.SysFont("Calibri",35).render("Player: "+str(player.score),True,(255,0,0))
        screen.blit(bg_score,bg_score.get_rect())
        settings_rect = settings_text.get_rect(center=(WINDOWS_WIDTH/2,WINDOWS_HEIGHT/5))
        back_button.draw(screen)
        next_button.draw(screen)
        screen.blit(font,(WINDOWS_WIDTH/2 - (font.get_width()/2),WINDOWS_HEIGHT/4))
        screen.blit(settings_text,settings_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.click():
                    main_menu()
                elif next_button.click():
                    pass
                
        pygame.display.update()

def set_up_level():
    clock = pygame.time.Clock()
    bg_image = pygame.transform.scale(pygame.image.load(SELECTED_BG),(WINDOWS_WIDTH,WINDOWS_HEIGHT)).convert() #acelera el juego y consume menos recursos
    pygame.mixer.music.load(LVL1_SOUND)
    pygame.mixer.music.play()
    enemy_list = []
    #enemy_1 = Enemy(move_x=0,move_y=0,position_x=50,position_y=GROUND_LEVEL,direction=DIRECTION_L,speed_walk=1,speed_run=2,power_jump=35,amount_gravity=14,frame_rate_ms=90,move_rate_ms=25,p_scale=0.1,attack_on=False,walk_on=False,run_on=False,jump_on=False)
    enemy_2 = Enemy(move_x=0,move_y=0,position_x=300,position_y=601,direction=DIRECTION_R,speed_walk=2,speed_run=3,power_jump=35,amount_gravity=14,frame_rate_ms=90,move_rate_ms=25,p_scale=0.1,attack_on=False,walk_on=False,run_on=False,jump_on=False)
    #enemy_list.append(enemy_1)
    enemy_list.append(enemy_2)
    platform_list = []
    plataforma_1 = Platform(position_x=450,position_y=600,width=100,height=50)
    plataforma_2 = Platform(position_x=600,position_y=650,width=100,height=50)
    platform_list.append(plataforma_1)
    platform_list.append(plataforma_2)
    coin_list = []
    coin = Coin(500,550)
    coin_list.append(coin)
    coin2 = Coin(600,550)
    coin_list.append(coin2)
    coin_out = Coin(0,1000)
    coin_list.append(coin_out)
    potion_list = []
    life_potion = Potion(position_x=600,position_y=600)
    life_potion_out = Potion(position_x=0,position_y=1000)
    potion_list.append(life_potion)
    potion_list.append(life_potion_out)
    portal = Portal(position_x=900,position_y=GROUND_LEVEL+30)
    
    play(True,clock,player,portal,bg_image,enemy_list,platform_list,potion_list,coin_list)

def play(run,clock,player,portal,bg_image,enemy_list,platform_list,potion_list,coin_list):
   while run:
    screen.blit(bg_image,bg_image.get_rect())
    delta_ms = clock.tick(FPS) 
    font = pygame.font.SysFont("Calibri",35).render("SCORE: "+str(player.score),True,(255,0,0))
    life = pygame.font.SysFont("Calibri",35).render("LIFE: "+str(world.life_list),True,(255,0,0))
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit

    if len(coin_list) > 0:
        for coin in coin_list:
            coin.draw(screen)
            coin.update(player)
            if coin.is_collected:
                print(player.score)
                coin_list.remove(coin)

    screen.blit(font,(10,50))
    screen.blit(life,(10,150))
    world.draw(screen)
    world.draw_life(screen)
    coin.draw(screen)
    pressed_key = pygame.key.get_pressed() 
    
    if player.is_dead == False:
        player.events(pressed_key,enemy_list)
        player.update(delta_ms,platform_list,enemy_list,world.life_list)
    else:
        if restart_button.draw(screen):
            if restart_button.click():
                player.reset(move_x=0,move_y=0,position_x=1,position_y=(WINDOWS_HEIGHT/12),direction=DIRECTION_R,speed_walk=5,speed_run=8,power_jump=100,amount_gravity=14,frame_rate_ms=60,move_rate_ms=30,p_scale=0.15)
    
    portal.draw(screen)
    portal.update(delta_ms,player)
    if portal.is_reached:
        score()

    if len(potion_list) > 0:
        for potion in potion_list:
            potion.draw(screen)
            potion.update(player,world)
            if potion.is_collected:
                potion_list.remove(potion)

    for enemy in enemy_list:
        enemy.draw(screen)
        enemy.update(delta_ms,platform_list,player)
        if enemy.is_dead:
            enemy_list.remove(enemy)
    
    for platform in platform_list:
        platform.draw(screen)
    
    player.draw(screen)
    pygame.display.flip()

def settings():
    pygame.display.set_caption("Settings")
    blur = pygame.transform.scale(pygame.image.load(BLUR),(WINDOWS_WIDTH,WINDOWS_HEIGHT))#acelera el juego y consume menos recursos
    
    while True:
        screen.fill(C_YELLOW_2)
        screen.blit(blur,blur.get_rect())
        settings_text = pygame.font.SysFont("Calibri",35).render("SETTINGS",True,C_GREEN)
        settings_rect = settings_text.get_rect(center=(WINDOWS_WIDTH/2,WINDOWS_HEIGHT/5))
        back_button.draw(screen)
        screen.blit(settings_text,settings_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.click():
                    main_menu()
                
        pygame.display.update()
        
def main_menu():
    pygame.display.set_caption("Menu")
    pygame.mixer.music.load(MAIN_SOUND)
    pygame.mixer.music.play(-1)
    bg_templar = pygame.transform.scale(pygame.image.load(BG_MAIN_MENU2),(WINDOWS_WIDTH,WINDOWS_HEIGHT))#acelera el juego y consume menos recursos

    while True:
        screen.fill(C_WHITE)

        menu_text = pygame.font.SysFont("Middle Ages Deco PERSONAL USE",100).render("Free Knight",True,C_BLACK)
        menu_rect = menu_text.get_rect(center=(WINDOWS_WIDTH/2,WINDOWS_HEIGHT/5))
        screen.blit(bg_templar,bg_templar.get_rect())
        start_button.draw(screen)
        settings_button.draw(screen)
        exit_button.draw(screen)
        scores_button.draw(screen)
        credit_button.draw(screen)
        screen.blit(menu_text,menu_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.click():
                    set_up_level()
                elif settings_button.click():
                    settings()
                elif scores_button.click():
                    score()
                elif credit_button.click():
                    credits()
                elif exit_button.click():
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

main_menu()