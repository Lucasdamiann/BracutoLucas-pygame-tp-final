import sys
import pygame
from constants import *
from player import Player
from enemy import Enemy
from surfaces import Surfaces
from coins import Coin
from button import Button
from potion import Potion
from portal import Portal
import time
pygame.init()
screen = pygame.display.set_mode((WINDOWS_WIDTH,WINDOWS_HEIGHT))
clock = pygame.time.Clock()


start_button = Button(WINDOWS_WIDTH / 4 ,WINDOWS_HEIGHT / 2,START_BUTTON)
settings_button = Button(WINDOWS_WIDTH / 4 + (start_button.rect.w),WINDOWS_HEIGHT / 2,SET_BUTTON)
scores_button = Button(WINDOWS_WIDTH / 4 + (start_button.rect.w*2),WINDOWS_HEIGHT / 2,SCORE_BUTTON)
credit_button = Button(WINDOWS_WIDTH / 4 + (start_button.rect.w*3),WINDOWS_HEIGHT / 2,CREDIT_BUTTON)
exit_button = Button(WINDOWS_WIDTH / 4 + (start_button.rect.w*4),WINDOWS_HEIGHT / 2,EXIT_BUTTON)
back_button = Button(WINDOWS_WIDTH / 12,WINDOWS_HEIGHT / 12,BACK_BUTTON)
next_button = Button(WINDOWS_WIDTH / 2 - (start_button.rect.w/2),WINDOWS_HEIGHT / 2,NEXT_BUTTON)
pause_button =  Button(WINDOWS_WIDTH / 2 - (start_button.rect.w/2),WINDOWS_HEIGHT / 2,PAUSE_BUTTON)
restart_button = Button(WINDOWS_WIDTH / 2 - (start_button.rect.w/2),WINDOWS_HEIGHT / 2,RESTART_BUTTON)

player = Player(move_x=0,move_y=0,position_x=1,position_y=(WINDOWS_HEIGHT/12),direction=DIRECTION_R,speed_walk=5,speed_run=8,power_jump=100,amount_gravity=14,frame_rate_ms=60,move_rate_ms=30,p_scale=0.15)
total_time = 5 * 60 #minutos por segundos
start_time = time.time()

def credits():
    pygame.display.set_caption("Credits")
    while True:
        screen.fill(C_BLACK)
        credits_text = pygame.font.SysFont("Middle Ages Deco PERSONAL USE",35).render("CREDITS",True,C_WHITE)
        credits_rect = credits_text.get_rect(center=(WINDOWS_WIDTH/2,WINDOWS_HEIGHT/5))
        back_button.draw(screen)
        credits_message = pygame.font.SysFont("Calibri",35).render("Creado por Lucas Damian Bracuto",True,C_WHITE)
        credits_message_rect = credits_message.get_rect(center=(WINDOWS_WIDTH/2,WINDOWS_HEIGHT/3))
        screen.blit(credits_text,credits_rect)
        screen.blit(credits_message,credits_message_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.click():
                    main_menu()
                
        pygame.display.update()

def set_up_level_2():
    world_data = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [9,9,9,9,9,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,19,20,21,0,0,0,0,0],
            [0,0,0,19,20,21,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [10,11,11,12,0,10,11,11,11,12,0,10,11,11,11,12],
        ]
    world = Surfaces(world_data)
    bg_image = pygame.transform.scale(pygame.image.load(SELECTED_BG),(WINDOWS_WIDTH,WINDOWS_HEIGHT)).convert() #acelera el juego y consume menos recursos
    pygame.mixer.music.load(LVL1_SOUND)
    pygame.mixer.music.play()
    enemy_list = []
    enemy_1 = Enemy(move_x=0,move_y=0,position_x=500,position_y=GROUND_LEVEL,direction=DIRECTION_L,speed_walk=1,speed_run=2,power_jump=35,amount_gravity=14,frame_rate_ms=90,move_rate_ms=25,p_scale=0.1,attack_on=False,walk_on=False,run_on=False,jump_on=False)
    enemy_2 = Enemy(move_x=0,move_y=0,position_x=300,position_y=601,direction=DIRECTION_R,speed_walk=2,speed_run=3,power_jump=35,amount_gravity=14,frame_rate_ms=90,move_rate_ms=25,p_scale=0.1,attack_on=False,walk_on=False,run_on=False,jump_on=False)
    enemy_list.append(enemy_1)
    enemy_list.append(enemy_2)
    coin_list = []
    coin = Coin(500,600)
    coin_list.append(coin)
    coin2 = Coin(600,650)
    coin_list.append(coin2)
    coin_out = Coin(0,1000)
    coin_list.append(coin_out)
    potion_list = []
    life_potion = Potion(position_x=800,position_y=600)
    life_potion_out = Potion(position_x=0,position_y=1000)
    potion_list.append(life_potion)
    potion_list.append(life_potion_out)
    portal = Portal(position_x=500,position_y=WINDOWS_HEIGHT/2)
    
    play(True,clock,player,portal,bg_image,enemy_list,potion_list,coin_list,world)

def set_up_level_1():
        
    world_data = [
            [9,9,9,9,9,9,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,16,17,17,18],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,2,2,2,2,2,2,2,2,2,2,0,2,2,2,3],
        ]
    world = Surfaces(world_data)
    bg_image = pygame.transform.scale(pygame.image.load(SELECTED_BG),(WINDOWS_WIDTH,WINDOWS_HEIGHT)).convert() #acelera el juego y consume menos recursos
    pygame.mixer.music.load(LVL1_SOUND)
    pygame.mixer.music.play()
    enemy_list = []
    enemy_1 = Enemy(move_x=0,move_y=0,position_x=50,position_y=GROUND_LEVEL,direction=DIRECTION_L,speed_walk=1,speed_run=2,power_jump=20,amount_gravity=10,frame_rate_ms=90,move_rate_ms=25,p_scale=0.1,attack_on=False,walk_on=False,run_on=False,jump_on=False)
    enemy_2 = Enemy(move_x=0,move_y=0,position_x=300,position_y=601,direction=DIRECTION_R,speed_walk=2,speed_run=3,power_jump=35,amount_gravity=14,frame_rate_ms=90,move_rate_ms=25,p_scale=0.1,attack_on=False,walk_on=False,run_on=False,jump_on=False)
    enemy_list.append(enemy_1)
    enemy_list.append(enemy_2)
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
    
    play(True,clock,player,portal,bg_image,enemy_list,potion_list,coin_list,world)

def score():
    pygame.display.set_caption("Scores")
    pygame.mixer.music.load(SCORE_SCREEN_SOUND)
    pygame.mixer.music.play(-1)
    bg_score = pygame.transform.scale(pygame.image.load(BLUR),(WINDOWS_WIDTH,WINDOWS_HEIGHT))#acelera el juego y consume menos recursos
    while True:
        screen.fill(C_PEACH)
        settings_text = pygame.font.SysFont("Middle Ages Deco PERSONAL USE",35).render("SCORES",True,C_WHITE)
        font = pygame.font.SysFont("Middle Ages Deco PERSONAL USE",35).render("PLAYER: "+str(player.score),True,C_BLACK)
        next_text = pygame.font.SysFont("Middle Ages Deco PERSONAL USE",25).render("NEXT LEVEL",True,C_WHITE)
        screen.blit(bg_score,bg_score.get_rect())
        settings_rect = settings_text.get_rect(center=(WINDOWS_WIDTH/2,WINDOWS_HEIGHT/5))
        back_button.draw(screen)
        next_button.draw(screen)
        screen.blit(font,(WINDOWS_WIDTH/2 - (font.get_width()/2),WINDOWS_HEIGHT/4))
        screen.blit(next_text,(WINDOWS_WIDTH/2 - (next_text.get_width()/2),WINDOWS_HEIGHT/1.5))
        screen.blit(settings_text,settings_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.click():
                    main_menu()
                elif next_button.click():
                    set_up_level_2()
                
        pygame.display.update()

def timer(total_time, start_time):
    elapsed_time = time.time() - start_time
    time_left = max(total_time - elapsed_time,0) #el 0 evita que el timpo sea negativo
    timer_text = "TIEMPO RESTANTE: {0}".format(int(time_left))
    rendered_timer = pygame.font.SysFont("Calibri",15).render(timer_text, True, (255, 255, 255))
    text_rect = rendered_timer.get_rect(center=(WINDOWS_WIDTH // 2, WINDOWS_HEIGHT // 12))
    screen.blit(rendered_timer, text_rect)
    if time_left == 0:
        score()

def play(run,clock,player,portal,bg_image,enemy_list,potion_list,coin_list,world):
    while run:
        screen.blit(bg_image,bg_image.get_rect())
        delta_ms = clock.tick(FPS) 
        timer(total_time,start_time)
        font = pygame.font.SysFont("System",35).render("SCORE: "+str(player.score),True,C_YELLOW_2)
        life = pygame.font.SysFont("System",35).render("LIFE: "+str(world.life_list),True,C_PINK)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit

        #impresion por pantalla
        screen.blit(font,(10,50))
        screen.blit(life,(10,150))
        world.draw(screen)
        world.draw_life(screen)
        pressed_key = pygame.key.get_pressed() 
        
        #monedas
        if len(coin_list) > 0:
            for coin in coin_list:
                coin.draw(screen)
                coin.update(player)
                if coin.is_collected:
                    print(player.score)
                    coin_list.remove(coin)

        #portal de finalizacion de nivel
        portal.draw(screen)
        portal.update(delta_ms,player)
        if portal.is_reached:
            score()
        #potion de cura
        if len(potion_list) > 0:
            for potion in potion_list:
                potion.draw(screen)
                potion.update(player,world)
                if potion.is_collected:
                    potion_list.remove(potion)
        #enemigos
        for enemy in enemy_list:
            enemy.draw(screen)
            enemy.update(delta_ms,player,world)
            if enemy.is_dead:
                enemy_list.remove(enemy)
       
        
        player.draw(screen)
        if player.is_dead == False:
            player.events(pressed_key,enemy_list)
            player.update(delta_ms,world,enemy_list,world.life_list)
        else:
            lose = pygame.font.SysFont("System",50).render("YOU LOSE: ",True,C_WHITE)
            screen.blit(lose,(WINDOWS_WIDTH/2 - (lose.get_width()/2),WINDOWS_HEIGHT/3))
            if restart_button.draw(screen) and restart_button.click():
                player.reset(move_x=0,move_y=0,position_x=1,position_y=(WINDOWS_HEIGHT/12),direction=DIRECTION_R,speed_walk=5,speed_run=8,power_jump=100,amount_gravity=14,frame_rate_ms=60,move_rate_ms=30,p_scale=0.15)
        
        pygame.display.flip()

def settings():
    pygame.display.set_caption("Settings")
    blur = pygame.transform.scale(pygame.image.load(BLUR),(WINDOWS_WIDTH,WINDOWS_HEIGHT))
    
    while True:
        screen.fill(C_BLUE_2)
        screen.blit(blur,blur.get_rect())
        settings_text = pygame.font.SysFont("Middle Ages Deco PERSONAL USE",35).render("SETTINGS",True,C_WHITE)
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
    bg_templar = pygame.transform.scale(pygame.image.load(BG_MAIN_MENU2),(WINDOWS_WIDTH,WINDOWS_HEIGHT))
    bg_templar2 = pygame.transform.scale(pygame.image.load(BG_MAIN_MENU3),(WINDOWS_WIDTH,WINDOWS_HEIGHT))

    while True:
        screen.fill(C_WHITE)
        menu_text = pygame.font.SysFont("Middle Ages Deco PERSONAL USE",100).render("FREE KNIGHT",True,C_BLACK)
        menu_rect = menu_text.get_rect(center=(WINDOWS_WIDTH/2,WINDOWS_HEIGHT/3))
        screen.blit(bg_templar,bg_templar.get_rect())
        screen.blit(menu_text,menu_rect)
        screen.blit(bg_templar2,bg_templar2.get_rect())
        start_button.draw(screen)
        settings_button.draw(screen)
        exit_button.draw(screen)
        scores_button.draw(screen)
        credit_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.click():
                    set_up_level_1()
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
