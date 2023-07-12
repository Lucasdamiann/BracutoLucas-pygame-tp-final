import pygame
from constants import *
from auxiliar import Auxiliar

class Player:
    '''Esto es un jugador'''
    def __init__(self,move_x,move_y,position_x,position_y,direction,speed_walk,speed_run,power_jump,amount_gravity,frame_rate_ms,move_rate_ms,p_scale=1) -> None:
       self.reset(move_x,move_y,position_x,position_y,direction,speed_walk,speed_run,power_jump,amount_gravity,frame_rate_ms,move_rate_ms,p_scale=0.15)
    
    def reset(self,move_x,move_y,position_x,position_y,direction,speed_walk,speed_run,power_jump,amount_gravity,frame_rate_ms,move_rate_ms,p_scale=1):
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
        self.hit_r_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+PLAYER_FOLDER+"Hit ({0}).png",1,3,flip=False,scale=p_scale)
        self.hit_l_action = Auxiliar.getSurfaceFromSeparateFiles(RESOURCES_FOLDER+PLAYER_FOLDER+"Hit ({0}).png",1,3,flip=True,scale=p_scale)
        self.animation = self.idle_r_action
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = position_x
        self.rect.y = position_y
        self.is_jump = False
        self.in_air = False
        self.amount_gravity = amount_gravity
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.power_jump = power_jump
        self.move_x = move_x
        self.move_y = move_y
        self.direction = direction
        self.move_rate_ms = move_rate_ms
        self.elapsed_time_move = 0
        self.elapsed_time_hit = 0
        self.frame_rate_ms = frame_rate_ms
        self.elapsed_time_animation = 0
        self.y_start_jump = 0
        self.rect_ground_collision_r = pygame.Rect(self.rect.x+self.rect.w/3.8,self.rect.y+self.rect.h-10,self.rect.w/3,10)
        self.rect_ground_collision_l = pygame.Rect(self.rect.x+self.rect.w/2.2,self.rect.y+self.rect.h-10,self.rect.w/3,10)
        self.rect_attack_collision_r = pygame.Rect(self.rect.x+self.rect.w-self.rect.w/3,self.rect.y+self.rect.h/2,self.rect.w/3,self.rect.h/3)
        self.rect_attack_collision_l = pygame.Rect(-self.rect.x,self.rect.y+self.rect.h/2,self.rect.w/3,self.rect.h/3)
        self.rect_hit_collision = pygame.Rect(self.rect.x+self.rect.w/3.8,self.rect.y+5,self.rect.w/2.1,self.rect.h-15)
        self.hit_counter = 0
        self.is_attack = False
        self.is_dead = False
        self.is_dead_triggered = False
        self.score = 0
        self.life_bar = 50
        self.die_sound  = pygame.mixer.Sound("Juego_freeknight\mis_assets\Sounds\pMaleDie.wav")
        self.melee_hit = pygame.mixer.Sound("Juego_freeknight\mis_assets\Sounds\eSwingWeapon1.wav")
        self.walk_sound = pygame.mixer.Sound("Juego_freeknight\mis_assets\Sounds\pw_step-02.wav")
        self.run_sound = pygame.mixer.Sound("Juego_freeknight\mis_assets\Sounds\pWalk(Grass).wav")
        self.swords_crash_sound = pygame.mixer.Sound("Juego_freeknight\mis_assets\Sounds\eMeleeHit5.wav")
        self.game_complete = False
        
    def walk(self,direction):
        '''comentar los metodos'''
        if(self.animation != self.walk_r_action and self.animation != self.walk_l_action):
            self.direction = direction
            if self.direction == DIRECTION_R:
                self.move_x = self.speed_walk
                self.animation = self.walk_r_action    
                if PRINTS: print("Caminando a la derecha")  
            else:
                self.move_x = -self.speed_walk
                self.animation = self.walk_l_action            
                if PRINTS: print("Caminando a la izquierda")
            self.frame= 0
            self.walk_sound.play()

    def stay(self):
        '''Metodo con el cual el personaje se queda quieto'''   
        if(self.animation != self.idle_r_action and self.animation != self.idle_l_action):     
            if self.direction == DIRECTION_R:
                self.animation = self.idle_r_action          
            else:
                self.animation = self.idle_l_action
            self.move_x = 0
            self.move_y = 0
            self.frame= 0

    def jump(self):
        '''Metodo con el cual el personaje salta'''   
        if(self.animation != self.jump_r_action and self.animation != self.jump_l_action):
            if self.is_jump == False and self.in_air == False:
                self.y_start_jump = self.rect.y
                if self.direction == DIRECTION_R:
                    self.animation = self.jump_r_action  
                    if PRINTS: print("Saltando a la derecha")
                else:
                    self.animation = self.jump_l_action
                    if PRINTS: print("Saltando a la izquierda")
                self.move_y = -self.power_jump
                # self.frame = 0
                self.is_jump = True
                self.in_air = True
            elif self.in_air == True:
                self.is_jump = False  
                self.stay()
                if PRINTS: print("quieto sin saltar")
    
    def attack(self):
        if(self.animation != self.attack_r_action and self.animation != self.attack_l_action):
            if self.direction == DIRECTION_R:
                self.animation = self.attack_r_action
                self.move_x = 0
            else:
                self.animation = self.attack_l_action                
                self.move_x = 0
            self.melee_hit.play()
            if PRINTS: print("pego")     
            
    def run(self,direction):
        if(self.animation != self.run_r_action and self.animation != self.run_l_action):
            self.direction = direction
            if self.direction == DIRECTION_R:
                self.animation = self.run_r_action            
                self.move_x = self.speed_run
            else:
                self.animation = self.run_l_action            
                self.move_x = -self.speed_run
            self.frame = 0
            self.run_sound.play()
            if PRINTS: print("corro")

    def hit(self):
        if(self.animation != self.hit_r_action and self.animation != self.hit_l_action):
            if self.direction == DIRECTION_R:
                self.animation = self.hit_r_action
                self.move_x = 0
            else:
                self.animation = self.hit_l_action
                self.move_x = 0
            self.frame= 0
            if PRINTS: print("me pega")

    def die(self):        
        if(self.animation != self.die_r_action and self.animation != self.die_l_action):
            if self.direction == DIRECTION_R:
                self.animation = self.die_r_action            
            else:
                self.animation = self.die_l_action
            self.move_x = 0
            self.is_dead_triggered = True
            self.die_sound.play()
            if PRINTS: print("muerto")

    def events(self,action_button,enemy_list):
        '''Gestiona las acciones del personaje'''
        if self.is_grounded:
            if action_button[pygame.K_d] and not action_button[pygame.K_a]:
                if action_button[pygame.K_LSHIFT] and action_button[pygame.K_d]:
                    self.run(DIRECTION_R)
                else:
                    self.walk(DIRECTION_R)
            elif action_button[pygame.K_a] and not action_button[pygame.K_d]:
                if action_button[pygame.K_LSHIFT] and action_button[pygame.K_a]:
                    self.run(DIRECTION_L) 
                else:self.walk(DIRECTION_L)              
            elif action_button[pygame.K_SPACE] and self.is_jump == False:
                self.jump()
                self.is_jump = False
            elif action_button[pygame.K_e] and self.is_attack == False:
                self.attack()
                self.is_attack = True
                for enemy in enemy_list:
                    if self.is_collision(enemy) or self.is_attack:
                        enemy.is_hit(self)
                        self.is_attack = False
                        break
            elif not action_button[pygame.K_a] and not action_button[pygame.K_d] and not action_button[pygame.K_SPACE] and not action_button[pygame.K_e]:
                self.stay()
            elif (action_button[pygame.K_SPACE] and action_button[pygame.K_e]) or (action_button[pygame.K_a] and action_button[pygame.K_d]):
                self.stay()
            


    def enemy_events(self,enemy_list,life_list,delta_ms):
        self.elapsed_time_hit += delta_ms
        self.life_bar
        if self.elapsed_time_hit >= 80:
            self.elapsed_time_hit = 0
            for enemy in enemy_list:
                if self.is_hit(enemy):
                    self.life_bar -=1
                    if PRINTS: print("Contador de golpe recibido "+str(self.life_bar))  
                    self.hit()
                    if self.life_bar < 1:
                        self.die()
                        self.is_dead = True

    def do_movement(self, delta_ms,world,enemy_list,life_list):
        self.elapsed_time_move += delta_ms
        if self.elapsed_time_move >= self.move_rate_ms:
            if (abs(self.y_start_jump) - abs(self.rect.y)) > self.power_jump and not self.is_jump:
                self.move_y = 0
            self.elapsed_time_move = 0
            self.move_rect_y(self.move_y) 

            if (self.direction == DIRECTION_R and self.rect.x < WINDOWS_WIDTH - self.rect_hit_collision.width*1.5) or (self.direction == DIRECTION_L and self.rect_hit_collision.x > 0):
                self.move_rect_x(self.move_x)

            self.enemy_events(enemy_list,life_list,delta_ms)

            if self.is_grounded(world) == False:
                self.move_rect_y(self.amount_gravity)
                if self.rect.y > WINDOWS_HEIGHT:
                    self.die()
                    self.is_dead = True

    def is_grounded(self,world):
        m_return = False
        for platform in world.tile_list:
            if self.direction == DIRECTION_R:
                if self.rect_ground_collision_r.colliderect(platform[1].x,platform[1].y,platform[1].w,5):
                    m_return = True
                    self.in_air = False
                    self.is_jump = False
                    break
            elif self.direction == DIRECTION_L:
                if self.rect_ground_collision_l.colliderect(platform[1]):
                    m_return = True
                    self.in_air = False
                    self.is_jump = False
                    break
            else:
                self.in_air = True
                m_return = False
        return m_return
    
    def is_collision(self,enemy):
        m_return = False
        if self.is_attack:
            if self.direction == DIRECTION_R and self.rect_attack_collision_r.colliderect(enemy.rect_hit_collision):
                if PRINTS: print("GOLPEO AL ENEMIGO") 
                self.swords_crash_sound.play()
                m_return = True
            elif self.direction == DIRECTION_L and self.rect_attack_collision_l.colliderect(enemy.rect_hit_collision):
                if PRINTS: print("GOLPEO AL ENEMIGO")  
                self.swords_crash_sound.play()
                m_return = True
            else:print("NO GOLPEO A NADIE")  
        return m_return

    def is_hit(self,enemy):
        m_return = False
        if self.rect_hit_collision.colliderect(enemy.rect_vision):
            if PRINTS: print("El enemigo me ah Golpeado")      
            m_return = True
        return m_return


    def move_rect_x(self,delta_x=0):
        '''Mueve los rectangulos en x'''
        self.rect.x += delta_x
        self.rect_ground_collision_r.x += delta_x
        self.rect_ground_collision_l.x += delta_x
        self.rect_attack_collision_l.x += delta_x
        self.rect_attack_collision_r.x += delta_x
        self.rect_hit_collision.x += delta_x


    def move_rect_y(self,delta_y=0):
        '''Mueve los rectangulos en y'''
        self.rect.y += delta_y
        self.rect_ground_collision_r.y += delta_y
        self.rect_ground_collision_l.y += delta_y
        self.rect_attack_collision_l.y += delta_y
        self.rect_attack_collision_r.y += delta_y
        self.rect_hit_collision.y += delta_y

    def do_animation(self,delta_ms,animate = True):
        self.elapsed_time_animation += delta_ms
        if animate:
            if self.elapsed_time_animation >= self.frame_rate_ms:
                self.elapsed_time_animation = 0
                if self.frame < len(self.animation) -1:
                    self.frame += 1 
                else:
                    self.frame = 0

    def update(self,delta_ms,world,enemy_list,life_list): 
        self.do_movement(delta_ms,world,enemy_list,life_list)        
        self.do_animation(delta_ms)

    def draw(self,screen):
        if DEBUG:   
            pygame.draw.rect(screen,C_WHITE,self.rect,2)
            pygame.draw.rect(screen,C_GREEN,self.rect_ground_collision_r,2)
            pygame.draw.rect(screen,C_BLUE,self.rect_ground_collision_l,2)
            pygame.draw.rect(screen,C_RED,self.rect_attack_collision_l,2)
            pygame.draw.rect(screen,C_YELLOW_2,self.rect_attack_collision_r,2)
            pygame.draw.rect(screen,C_PINK,self.rect_hit_collision,2)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)