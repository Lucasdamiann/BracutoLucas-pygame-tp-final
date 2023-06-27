import pygame
from constants import *
from auxiliar import Auxiliar
from platforms import Platform

class Character:
    def __init__(self,move_x=0,move_y=0,position_x=0,position_y=0,direction=0,speed_walk=0,speed_run=0,power_jump=0,amount_gravity=0,frame_rate_ms=0,move_rate_ms=0,p_scale=1,walk_ms=100,run_ms=500,stay_ms=550,jump_ms=552,attack_ms=680,walk_on=True,run_on=True,stay_on=True,jump_on=True,attack_on=True) -> None:
        self.walk_r_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+ENEMY_FOLDER+"WALK\_WALK_00{0}.png",0,7,flip=False,scale=p_scale)
        self.walk_l_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+ENEMY_FOLDER+"WALK\_WALK_00{0}.png",0,7,flip=True,scale=p_scale)
        self.jump_r_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+ENEMY_FOLDER+"JUMP\_JUMP_00{0}.png",0,7,flip=False,scale=p_scale)
        self.jump_l_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+ENEMY_FOLDER+"JUMP\_JUMP_00{0}.png",0,7,flip=True,scale=p_scale)
        self.idle_r_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+ENEMY_FOLDER+"IDLE\_IDLE_00{0}.png",0,7,flip=False,scale=p_scale)
        self.idle_l_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+ENEMY_FOLDER+"IDLE\_IDLE_00{0}.png",0,7,flip=True,scale=p_scale)
        self.attack_r_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+ENEMY_FOLDER+"ATTACK\_ATTACK_00{0}.png",0,7,flip=False,scale=p_scale)
        self.attack_l_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+ENEMY_FOLDER+"ATTACK\_ATTACK_00{0}.png",0,7,flip=True,scale=p_scale)
        self.die_r_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+ENEMY_FOLDER+"DIE\_DIE_00{0}.png",0,7,flip=False,scale=p_scale)
        self.die_l_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+ENEMY_FOLDER+"DIE\_DIE_00{0}.png",0,7,flip=True,scale=p_scale)
        self.run_r_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+ENEMY_FOLDER+"RUN\_RUN_00{0}.png",0,7,flip=False,scale=p_scale)
        self.run_l_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+ENEMY_FOLDER+"RUN\_RUN_00{0}.png",0,7,flip=True,scale=p_scale)
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
        self.time_acumulator = 0
        self.walk_on = walk_on
        self.walk_ms = walk_ms
        self.run_on = run_on
        self.run_ms = run_ms
        self.stay_on = stay_on
        self.stay_ms = stay_ms
        self.jump_on = jump_on
        self.jump_ms = jump_ms
        self.attack_on = attack_on
        self.attack_ms = attack_ms
        self.rect_ground_collision_r = pygame.Rect(self.rect.x+self.rect.w/4.5,self.rect.y+self.rect.h-10,self.rect.w/4,10)
        self.rect_ground_collision_l = pygame.Rect(self.rect.x+self.rect.w/1.8,self.rect.y+self.rect.h-10,self.rect.w/4,10)
        self.rect_hit_collision_l = pygame.Rect(self.rect.x+self.rect.w/2.1,self.rect.y+5,self.rect.w/2.3,self.rect.h-15)
        self.rect_hit_collision_r = pygame.Rect(self.rect.x+self.rect.w/10,self.rect.y+5,self.rect.w/2.3,self.rect.h-15)
        
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

    def automove(self):
        '''Gestiona las acciones del personaje'''
        print("Acumulador: {}".format(self.time_acumulator))
        self.time_acumulator +=1  
        if self.direction == DIRECTION_L and self.time_acumulator <= self.walk_ms and self.walk_on:
            self.walk(DIRECTION_L)
            self.time_acumulator +=1
        elif self.direction == DIRECTION_R and self.time_acumulator <= self.walk_ms and self.walk_on:
            self.walk(DIRECTION_R)
            self.time_acumulator +=1
        elif self.walk_ms < self.time_acumulator <= self.run_ms and self.run_on:
            self.run()      
            self.time_acumulator +=1  
        elif self.run_ms < self.time_acumulator <= self.stay_ms and self.stay_on:
            self.stay()
            self.time_acumulator +=1
        elif self.stay_ms < self.time_acumulator <= self.jump_ms and self.jump_on:
            self.jump(True)
            self.time_acumulator +=1
        elif self.jump_ms < self.time_acumulator <= self.attack_ms and self.attack_on:
            self.attack()   
            self.time_acumulator +=1  
        elif self.time_acumulator > self.attack_ms:
            self.time_acumulator = 0
            if self.direction == DIRECTION_L:             
                self.direction = DIRECTION_R
            else:
                self.direction = DIRECTION_L
            
            
    
    def do_movement(self, delta_ms,platform_list):
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
            else:
                self.automove()  

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

    def is_hit(self):
        pass

    def move_rect_x(self,delta_x=0):
        '''Mueve los rectangulos en x'''
        print(self.rect.x)
        print(delta_x)
        self.rect.x += delta_x
        self.rect_ground_collision_r.x += delta_x
        self.rect_ground_collision_l.x += delta_x
        self.rect_hit_collision_l.x += delta_x
        self.rect_hit_collision_r.x += delta_x
        
    def move_rect_y(self,delta_y=0):
        '''Mueve los rectangulos en y'''
        self.rect.y += delta_y
        self.rect_ground_collision_r.y += delta_y
        self.rect_ground_collision_l.y += delta_y
        self.rect_hit_collision_l.y += delta_y
        self.rect_hit_collision_r.y += delta_y

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if self.tiempo_transcurrido_animation >= self.frame_rate_ms:
            self.tiempo_transcurrido_animation = 0
            if self.frame < len(self.animation) - 1:
                self.frame += 1 
            else:
                self.frame = 0

    def update(self,delta_ms,platform_list): 
        self.do_movement(delta_ms,platform_list)
        self.do_animation(delta_ms)

    def draw(self,screen):
       
        if DEBUG:   
            pygame.draw.rect(screen,C_WHITE,self.rect)
            pygame.draw.rect(screen,C_GREEN,self.rect_ground_collision_r)
            pygame.draw.rect(screen,C_BLUE,self.rect_ground_collision_l)
            pygame.draw.rect(screen,C_PINK,self.rect_hit_collision_l)
            pygame.draw.rect(screen,C_BLUE_2,self.rect_hit_collision_r)
            
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        