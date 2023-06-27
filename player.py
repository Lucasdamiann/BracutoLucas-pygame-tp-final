import pygame
from constants import *
from auxiliar import Auxiliar
from platforms import Platform
from character import Character
class Player:
    '''Esto es un jugador'''
    def __init__(self,move_x,move_y,position_x,position_y,direction,speed_walk,speed_run,power_jump,amount_gravity,frame_rate_ms,move_rate_ms,p_scale=1) -> None:
        self.walk_r_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+PLAYER_FOLDER+"Walk ({0}).png",1,10,flip=False,scale=p_scale)
        self.walk_l_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+PLAYER_FOLDER+"Walk ({0}).png",1,10,flip=True,scale=p_scale)
        self.jump_r_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+PLAYER_FOLDER+"Jump ({0}).png",1,10,flip=False,scale=p_scale)
        self.jump_l_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+PLAYER_FOLDER+"Jump ({0}).png",1,10,flip=True,scale=p_scale)
        self.idle_r_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+PLAYER_FOLDER+"Idle ({0}).png",1,10,flip=False,scale=p_scale)
        self.idle_l_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+PLAYER_FOLDER+"Idle ({0}).png",1,10,flip=True,scale=p_scale)
        self.attack_r_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+PLAYER_FOLDER+"Attack ({0}).png",1,10,flip=False,scale=p_scale)
        self.attack_l_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+PLAYER_FOLDER+"Attack ({0}).png",1,10,flip=True,scale=p_scale)
        self.die_r_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+PLAYER_FOLDER+"Dead ({0}).png",1,10,flip=False,scale=p_scale)
        self.die_l_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+PLAYER_FOLDER+"Dead ({0}).png",1,10,flip=True,scale=p_scale)
        self.run_r_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+PLAYER_FOLDER+"Run ({0}).png",1,10,flip=False,scale=p_scale)
        self.run_l_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+PLAYER_FOLDER+"Run ({0}).png",1,10,flip=True,scale=p_scale)
        self.animation = self.idle_r_action
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = position_x
        self.rect.y = position_y
        self.is_jump = False
        self.amount_gravity = amount_gravity
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.power_jump = power_jump
        self.move_x = move_x
        self.move_y = move_y
        self.direction = direction
        self.move_rate_ms = move_rate_ms
        self.tiempo_transcurrido_move = 0
        self.frame_rate_ms = frame_rate_ms
        self.tiempo_transcurrido_animation = 0
        self.y_start_jump = 0
        self.rect_ground_collision_r = pygame.Rect(self.rect.x+self.rect.w/3.8,self.rect.y+self.rect.h-10,self.rect.w/3,10)
        self.rect_ground_collision_l = pygame.Rect(self.rect.x+self.rect.w/2.2,self.rect.y+self.rect.h-7,self.rect.w/3,10)
        self.rect_attack_collision_r = pygame.Rect(self.rect.x+self.rect.w/1.4,self.rect.y+self.rect.h/2,self.rect.w/6,self.rect.h/2.5)
        self.rect_attack_collision_l = pygame.Rect(self.rect.x+self.rect.w/8,self.rect.y+self.rect.h/2,self.rect.w/6,self.rect.h/2.5)
        
    def walk(self,direction):
        '''comentar los metodos'''
        self.direction = direction
        if self.direction == DIRECTION_R:
            self.move_x = self.speed_walk
            self.animation = self.walk_r_action                    
            print("Caminando a la derecha")  
        else:
            self.move_x = -self.speed_walk
            self.animation = self.walk_l_action            
            print("Caminando a la izquierda")
        
    def stay(self):
        '''Metodo con el cual el personaje se queda quieto'''        
        if self.direction == DIRECTION_R:
            self.animation = self.idle_r_action          
        else:
            self.animation = self.idle_l_action
        self.move_x = 0
        self.move_y = 0
        self.is_jump = False  

    def jump(self,is_grounded = True):
        '''Metodo con el cual el personaje salta'''   
        if self.is_jump == False and is_grounded:
            self.y_start_jump = self.rect.y
            if self.direction == DIRECTION_R:
                self.animation = self.jump_r_action   
                print("Saltando a la derecha")
            else:
                self.animation = self.jump_l_action
                print("Saltando a la izquierda")
            self.move_y = -self.power_jump
            self.frame = 0
            self.is_jump = True
        elif is_grounded == False:
            self.is_jump = False
            self.stay()
    
    def attack(self):
        if self.direction == DIRECTION_R:
            self.animation = self.attack_r_action
            self.move_x = 0
        else:
            self.animation = self.attack_l_action
            self.move_x = 0

    def run(self):
        if self.direction == DIRECTION_R:
            self.animation = self.run_r_action            
            self.move_x = self.speed_run
        else:
            self.animation = self.run_l_action            
            self.move_x = -self.speed_run

    def events(self,action_button):
        '''Gestiona las acciones del personaje'''
    
        if action_button[pygame.K_d] and not action_button[pygame.K_a]:
            self.walk(DIRECTION_R)
            if action_button[pygame.K_LSHIFT] or action_button[pygame.K_RSHIFT]:
                self.run()      

        elif action_button[pygame.K_a] and not action_button[pygame.K_d]:
            self.walk(DIRECTION_L)     
            if action_button[pygame.K_LSHIFT] or action_button[pygame.K_RSHIFT]:
                self.run()

        elif action_button[pygame.K_SPACE] or action_button[pygame.K_w]:
            self.jump(True)

        elif action_button[pygame.K_e]:
            self.attack()     

        elif not action_button[pygame.K_a] and not action_button[pygame.K_d] and not action_button[pygame.K_SPACE] and not action_button[pygame.K_w]:
            self.stay()
    
    def do_movement(self, delta_ms,platform_list,enemy_list):
        self.tiempo_transcurrido_move += delta_ms
        if self.tiempo_transcurrido_move >= self.move_rate_ms:
            if (abs(self.y_start_jump) - abs(self.rect.y)) > self.power_jump and self.is_jump:
                print(abs(self.y_start_jump) - abs(self.rect.y))
                self.move_y = 0
            self.tiempo_transcurrido_move = 0
            self.move_rect_x(self.move_x)
            self.move_rect_y(self.move_y) 

            if self.is_grounded(platform_list) == False:
                self.move_rect_y(self.amount_gravity)
            elif self.is_jump:
                self.jump(False)
            if self.is_attacking(enemy_list):
                pass

    def is_grounded(self,platform_list):
        m_return = False
        if self.rect.y >= GROUND_LEVEL:
            m_return = True
        else:
            for platform in platform_list:
                if self.direction == DIRECTION_R:
                    if self.rect_ground_collision_r.colliderect(platform.rect_ground_collision):
                        m_return = True
                        break
                else:
                     if self.rect_ground_collision_l.colliderect(platform.rect_ground_collision):
                        m_return = True
                        break
        return m_return
    
    def is_attacking(self,enemy_list):
        m_return = False
        if len(enemy_list) != 0:
            for enemy in enemy_list:
                if self.direction == DIRECTION_R:
                    if self.rect_attack_collision_r.colliderect(enemy.rect_hit_collision_r) or self.rect_attack_collision_r.colliderect(enemy.rect_hit_collision_l):
                        print("GOLPEADO")
                        m_return = True
                        break
                else:
                    if self.rect_attack_collision_l.colliderect(enemy.rect_hit_collision_r) or self.rect_attack_collision_l.colliderect(enemy.rect_hit_collision_l):
                        print("GOLPEADO")
                        m_return = True
                        break
        return m_return

    def move_rect_x(self,delta_x=0):
        '''Mueve los rectangulos en x'''
        self.rect.x += delta_x
        self.rect_ground_collision_r.x += delta_x
        self.rect_ground_collision_l.x += delta_x
        self.rect_attack_collision_l.x += delta_x
        self.rect_attack_collision_r.x += delta_x


    def move_rect_y(self,delta_y=0):
        '''Mueve los rectangulos en y'''
        self.rect.y += delta_y
        self.rect_ground_collision_r.y += delta_y
        self.rect_ground_collision_l.y += delta_y
        self.rect_attack_collision_l.y += delta_y
        self.rect_attack_collision_r.y += delta_y

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if self.tiempo_transcurrido_animation >= self.frame_rate_ms:
            self.tiempo_transcurrido_animation = 0
            if self.frame < len(self.animation) - 1:
                self.frame += 1 
            else:
                self.frame = 0

    def update(self,delta_ms,platform_list,enemy_list): 
        self.do_movement(delta_ms,platform_list,enemy_list)
        self.do_animation(delta_ms)

    def draw(self,screen):
       
        if DEBUG:   
            #pygame.draw.rect(screen,C_WHITE,self.rect)
            pygame.draw.rect(screen,C_GREEN,self.rect_ground_collision_r)
            pygame.draw.rect(screen,C_BLUE,self.rect_ground_collision_l)
            pygame.draw.rect(screen,C_RED,self.rect_attack_collision_l)
            pygame.draw.rect(screen,C_YELLOW_2,self.rect_attack_collision_r)
            
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        