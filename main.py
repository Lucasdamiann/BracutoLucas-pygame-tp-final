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
from boss import Boss
from ranking import Ranking
from library_freeknight import *

pygame.init()
screen = pygame.display.set_mode((WINDOWS_WIDTH,WINDOWS_HEIGHT))
clock = pygame.time.Clock()

start_button = Button(WINDOWS_WIDTH / 4 ,WINDOWS_HEIGHT / 2,START_BUTTON)
settings_button = Button(WINDOWS_WIDTH / 4 + (start_button.rect.w*2),WINDOWS_HEIGHT / 2,SET_BUTTON)
exit_button = Button(WINDOWS_WIDTH / 4 + (start_button.rect.w*4),WINDOWS_HEIGHT / 2,EXIT_BUTTON)
scores_button = Button(WINDOWS_WIDTH / 4 + (start_button.rect.w*2),WINDOWS_HEIGHT / 2,SCORE_BUTTON)
credit_button = Button(WINDOWS_WIDTH / 4 + (start_button.rect.w*3),WINDOWS_HEIGHT / 2,CREDIT_BUTTON)
back_button = Button(WINDOWS_WIDTH / 12,WINDOWS_HEIGHT / 12,BACK_BUTTON)
next_button = Button(WINDOWS_WIDTH / 2 - (start_button.rect.w/2),WINDOWS_HEIGHT / 2,NEXT_BUTTON)
ok_button =  Button(WINDOWS_WIDTH / 2 - (start_button.rect.w/2),WINDOWS_HEIGHT / 2,OK_BUTTON)
restart_button = Button(WINDOWS_WIDTH / 2 - (start_button.rect.w/2),WINDOWS_HEIGHT / 2,RESTART_BUTTON)
mute_button = Button(WINDOWS_WIDTH / 4 + (start_button.rect.w*3),WINDOWS_HEIGHT/2,MUSIC_OFF_BUTTON)
unmute_button = Button(WINDOWS_WIDTH / 4 + (start_button.rect.w),WINDOWS_HEIGHT/2,MUSIC_ON_BUTTON)
ranking_button = Button(WINDOWS_WIDTH / 4 + (start_button.rect.w),WINDOWS_HEIGHT/2,MUSIC_ON_BUTTON)

player = Player(move_x=0,move_y=0,position_x=1,position_y=(WINDOWS_HEIGHT)-200,direction=DIRECTION_R,speed_walk=5,speed_run=8,power_jump=100,amount_gravity=14,frame_rate_ms=60,move_rate_ms=30,p_scale=0.15)
total_time = 5 * 60 #minutos por segundos
start_time = time.time()
ranking = Ranking()
ranking.create_db()

def name_player():
    pygame.display.set_caption("Name your player")
    while True:
        player_name = ''
        font = pygame.font.SysFont('Terminal',40)
        text_box = pygame.Rect(WINDOWS_WIDTH/2 -55, WINDOWS_HEIGHT/3.1,100,50)
        active = False
        color = pygame.Color('purple')
        named = False
        while True:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    if text_box.collidepoint(events.pos):
                        active = True
                    else:
                        active = False
                if events.type == pygame.KEYDOWN:
                    if active:
                        if events.key == pygame.K_BACKSPACE:
                            player_name = player_name[:-1]
                        else:
                            player_name += events.unicode
                if back_button.click():
                    main_menu()
                elif ok_button.click():
                    ranking.player_name = player_name
                    named = True
                elif start_button.click() and named:
                    # set_up_level_1()
                    set_up_level_final()

            screen.fill(C_BLACK)
            name_text = pygame.font.SysFont("Middle Ages Deco PERSONAL USE",35).render("Name your player",True,C_WHITE)
            screen.blit(name_text,name_text.get_rect(center=(WINDOWS_WIDTH/2,WINDOWS_HEIGHT/5)))
            if active:
                color = pygame.Color(C_RED)
            else:
                color = pygame.Color(C_BLUE)

                if start_button.click():
                    print(player_name)
            back_button.draw(screen)
            start_button.draw(screen)
            ok_button.draw(screen)
            pygame.draw.rect(screen,color, text_box,4)
            surf = font.render(player_name,True,C_WHITE)
            screen.blit(surf, (WINDOWS_WIDTH/2 -50, WINDOWS_HEIGHT/3))
            text_box.w = max(100, surf.get_width()+10)
            pygame.display.update()

def rankings():
    pygame.display.set_caption("Ranking")
    bg_ranking = pygame.transform.scale(pygame.image.load(RANKING),(WINDOWS_WIDTH,WINDOWS_HEIGHT))
    while True:
        screen.fill(C_BLACK)
        ranking_text = pygame.font.SysFont("Middle Ages Deco PERSONAL USE",35).render("RANKING",True,C_WHITE)
        ranking_rect = ranking_text.get_rect(center=(WINDOWS_WIDTH/2,WINDOWS_HEIGHT/5))
        back_button.draw(screen)
        screen.blit(bg_ranking,bg_ranking.get_rect())
        screen.blit(ranking_text,ranking_rect)
        ranking.insert_player(player.score)
        ranking.print_ranking(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.click():
                    main_menu()

        pygame.display.update()

def credits():
    pygame.display.set_caption("Credits")
    pygame.mixer.music.load(CREDITS_SOUND)
    pygame.mixer.music.play(-1)
   
    while True:
        screen.fill(C_BLACK)
        credits_text = pygame.font.SysFont("Middle Ages Deco PERSONAL USE",35).render("CREDITS",True,C_WHITE)
        credits_rect = credits_text.get_rect(center=(WINDOWS_WIDTH/2,WINDOWS_HEIGHT/5))
        back_button.draw(screen)
        thanks_message = pygame.font.SysFont("Terminal",50).render("¡Gracias por jugar Free Knight!",True,C_WHITE)
        credits_message = pygame.font.SysFont("Terminal",35).render("Creado por Lucas Damian Bracuto",True,C_WHITE)
        screen.blit(credits_text,credits_rect)
        screen.blit(thanks_message,thanks_message.get_rect(center=(WINDOWS_WIDTH/2,WINDOWS_HEIGHT/3)))
        screen.blit(credits_message,credits_message.get_rect(center=(WINDOWS_WIDTH/2,WINDOWS_HEIGHT/2)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.click():
                    main_menu()

        pygame.display.update()

def set_up_level_final():
    world_data = load_levels("Juego_freeknight\levels.json")[3]
    world = Surfaces(world_data)
    bg_image = pygame.transform.scale(pygame.image.load(BG_LVL_FINAL),(WINDOWS_WIDTH,WINDOWS_HEIGHT)).convert() #acelera el juego y consume menos recursos
    pygame.mixer.Sound(LVL_FINAL_SUBSOUND).play()
    pygame.mixer.music.load(LVL_FINAL_SOUND)
    pygame.mixer.music.play(-1)
    boss = Boss(move_x=0,move_y=0,position_x=WINDOWS_WIDTH/2,position_y=WINDOWS_HEIGHT/16,direction=DIRECTION_L,speed_walk=1,speed_run=2,power_jump=5,amount_gravity=14,frame_rate_ms=60,move_rate_ms=40,p_scale=0.2,attack_on=True,walk_on=True,run_on=True,jump_on=True)
    boss_list = [boss]
    coin_list = []
    coin = Coin(520,400)
    coin_list.append(coin)
    coin2 = Coin(250,450)
    coin_list.append(coin2)
    coin_out = Coin(0,1000)
    coin_list.append(coin_out)
    potion_list = []
    life_potion = Potion(position_x=1000,position_y=440)
    life_potion_out = Potion(position_x=0,position_y=1000)
    potion_list.append(life_potion)
    potion_list.append(life_potion_out)
    portal = Portal(position_x=1500,position_y=1000)
    portal.level_final = True
    play(True,clock,player,portal,bg_image,boss_list,potion_list,coin_list,world)

def set_up_level_3():
    world_data = load_levels("Juego_freeknight\levels.json")[2]
    world = Surfaces(world_data)
    bg_image = pygame.transform.scale(pygame.image.load(BG_LVL_3),(WINDOWS_WIDTH,WINDOWS_HEIGHT)).convert() #acelera el juego y consume menos recursos
    pygame.mixer.music.load(LVL3_SOUND)
    pygame.mixer.music.play(-1)
    enemy_list = []
    enemy_1 = Enemy(move_x=0,move_y=0,position_x=500,position_y=400,direction=DIRECTION_L,speed_walk=1,speed_run=2,power_jump=35,amount_gravity=14,frame_rate_ms=90,move_rate_ms=25,p_scale=0.1,attack_on=False,walk_on=False,run_on=False,jump_on=False)
    enemy_2 = Enemy(move_x=0,move_y=0,position_x=300,position_y=GROUND_LEVEL,direction=DIRECTION_R,speed_walk=2,speed_run=3,power_jump=35,amount_gravity=14,frame_rate_ms=90,move_rate_ms=25,p_scale=0.1,attack_on=False,walk_on=False,run_on=False,jump_on=False)
    enemy_3 = Enemy(move_x=0,move_y=0,position_x=600,position_y=0,direction=DIRECTION_R,speed_walk=2,speed_run=3,power_jump=35,amount_gravity=14,frame_rate_ms=90,move_rate_ms=25,p_scale=0.1,attack_on=False,walk_on=False,run_on=False,jump_on=False)
    enemy_list.append(enemy_1)
    enemy_list.append(enemy_2)
    enemy_list.append(enemy_3)
    coin_list = []
    coin = Coin(500,600)
    coin_list.append(coin)
    coin2 = Coin(600,650)
    coin_list.append(coin2)
    coin_out = Coin(0,1000)
    coin_list.append(coin_out)
    potion_list = []
    life_potion = Potion(position_x=TILE_SIZE*7,position_y=TILE_SIZE*11)
    life_potion_out = Potion(position_x=0,position_y=1000)
    potion_list.append(life_potion)
    potion_list.append(life_potion_out)
    portal = Portal(position_x=630,position_y=440)
    portal.level_3 = True

    play(True,clock,player,portal,bg_image,enemy_list,potion_list,coin_list,world)

def set_up_level_2():
    world_data = load_levels("Juego_freeknight\levels.json")[1]
    world = Surfaces(world_data)
    bg_image = pygame.transform.scale(pygame.image.load(BG_LVL_2),(WINDOWS_WIDTH,WINDOWS_HEIGHT)).convert() #acelera el juego y consume menos recursos
    pygame.mixer.music.load(LVL2_SOUND)
    pygame.mixer.music.play(-1)
    enemy_list = []
    enemy_1 = Enemy(move_x=0,move_y=0,position_x=500,position_y=400,direction=DIRECTION_L,speed_walk=1,speed_run=2,power_jump=35,amount_gravity=14,frame_rate_ms=90,move_rate_ms=25,p_scale=0.1,attack_on=False,walk_on=False,run_on=False,jump_on=False)
    enemy_2 = Enemy(move_x=0,move_y=0,position_x=300,position_y=0,direction=DIRECTION_R,speed_walk=2,speed_run=3,power_jump=35,amount_gravity=14,frame_rate_ms=90,move_rate_ms=25,p_scale=0.1,attack_on=False,walk_on=False,run_on=False,jump_on=False)
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
    portal = Portal(position_x=900,position_y=185)
    portal.level_2 = True
    
    play(True,clock,player,portal,bg_image,enemy_list,potion_list,coin_list,world)

def set_up_level_1(): 

    world_data = load_levels("Juego_freeknight\levels.json")[0]
    world = Surfaces(world_data)
    bg_image = pygame.transform.scale(pygame.image.load(BG_LVL_1),(WINDOWS_WIDTH,WINDOWS_HEIGHT)).convert() #acelera el juego y consume menos recursos
    pygame.mixer.music.load(LVL1_SOUND)
    pygame.mixer.music.play(-1)
    enemy_list = []
    enemy_1 = Enemy(move_x=0,move_y=0,position_x=500,position_y=GROUND_LEVEL,direction=DIRECTION_L,speed_walk=1,speed_run=2,power_jump=20,amount_gravity=10,frame_rate_ms=90,move_rate_ms=25,p_scale=0.1,attack_on=True,walk_on=True,run_on=False,jump_on=False)
    enemy_2 = Enemy(move_x=0,move_y=0,position_x=300,position_y=601,direction=DIRECTION_R,speed_walk=2,speed_run=3,power_jump=35,amount_gravity=14,frame_rate_ms=90,move_rate_ms=25,p_scale=0.1,attack_on=True,walk_on=True,run_on=False,jump_on=False)
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
    life_potion = Potion(position_x=850,position_y=600)
    life_potion_out = Potion(position_x=0,position_y=1000)
    potion_list.append(life_potion)
    potion_list.append(life_potion_out)
    portal = Portal(position_x=900,position_y=GROUND_LEVEL+30)
    play(True,clock,player,portal,bg_image,enemy_list,potion_list,coin_list,world)

def score(portal):
    pygame.display.set_caption("Scores")
    pygame.mixer.music.load(SCORE_SCREEN_SOUND)
    pygame.mixer.music.play(-1)
    bg_score = pygame.transform.scale(pygame.image.load(BLUR),(WINDOWS_WIDTH,WINDOWS_HEIGHT))#acelera el juego y consume menos recursos
    while True:
        screen.fill(C_PEACH)
        settings_text = pygame.font.SysFont("Middle Ages Deco PERSONAL USE",35).render("SCORES",True,C_WHITE)
        font = pygame.font.SysFont("Terminal",35).render("PLAYER: "+str(player.score),True,C_BLACK)
        next_text = pygame.font.SysFont("Terminal",25).render("NEXT LEVEL",True,C_WHITE)
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
                    if not portal.level_2 and not portal.level_3:
                        set_up_level_2()
                    elif not portal.level_3:
                        set_up_level_3()
                    elif not portal.level_final:
                        set_up_level_final()
                    elif portal.level_final:
                        rankings()
                    
                        
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
        font = pygame.font.SysFont("Terminal",35).render("SCORE: "+str(player.score),True,C_YELLOW_2)
        life = pygame.font.SysFont("Terminal",35).render("LIFE: "+str(player.life_bar),True,C_PINK)

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
            score(portal)

        if player.game_complete:
            rankings()

        #pocion
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
        mute_button.draw(screen)
        unmute_button.draw(screen)
        credit_button.draw(screen)
        screen.blit(settings_text,settings_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.click():
                    main_menu()
                elif credit_button.click():
                    credits()
                elif mute_button.click():
                    pygame.mixer.music.set_volume(0.0)
                elif unmute_button.click():
                    pygame.mixer.music.set_volume(1)

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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.click():
                    name_player()
                elif settings_button.click():
                    settings()
                elif exit_button.click():
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

main_menu()