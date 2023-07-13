import pygame
from constants import *
from auxiliar import Auxiliar

class Enemy:
    def __init__(self,move_x=0,move_y=0,position_x=0,position_y=0,direction=0,speed_walk=0,speed_run=0,power_jump=0,amount_gravity=0,frame_rate_ms=0,move_rate_ms=0,p_scale=1,walk_ms=100,run_ms=500,stay_ms=550,jump_ms=552,attack_ms=680,walk_on=True,run_on=True,stay_on=True,jump_on=True,attack_on=True,die_on=True):
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
        self.animation = self.idle_l_action
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
        self.elapsed_time_animation = 0
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
        self.die_on = die_on
        self.rect_ground_collision_r = pygame.Rect(self.rect.x+self.rect.w/4.5,self.rect.y+self.rect.h-15,self.rect.w/4,10)
        self.rect_ground_collision_l = pygame.Rect(self.rect.x+self.rect.w/1.8,self.rect.y+self.rect.h-15,self.rect.w/4,10)
        self.rect_hit_collision = pygame.Rect(self.rect.x+self.rect.w/3,self.rect.y+5,self.rect.w/3,self.rect.h-15)
        self.rect_vision = pygame.Rect(self.rect.x,self.rect.y+self.rect.h/3,self.rect.w/2,self.rect.h/4)
        self.is_dead = False
        self.die_sound = pygame.mixer.Sound("Juego_freeknight\mis_assets\Sounds\mAssassinDie.wav")
        self.swords_crash_sound = pygame.mixer.Sound("Juego_freeknight\mis_assets\Sounds\eMeleeHit5.wav")
        self.life = 2
        
    def walk(self,direction):
        #Metodo de animacion de caminata del enemigo
        self.direction = direction
        if self.direction == DIRECTION_R:
            self.move_x = self.speed_walk
            self.animation = self.walk_r_action                    
            if PRINTS: print("Caminando a la derecha")  
        else:
            self.move_x = -self.speed_walk
            self.animation = self.walk_l_action            
            if PRINTS: print("Caminando a la izquierda")
        
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
                if PRINTS: print("Saltando a la derecha")
            else:
                self.animation = self.jump_l_action
                if PRINTS: print("Saltando a la izquierda")
            self.move_y = -self.power_jump
            self.frame = 0
            self.is_jump = True
        elif is_grounded == False:
            self.is_jump = False
            self.stay()
    
    def attack(self):
        #Metodo de animacion de ataque del enemigo. Con sonido
        if self.direction == DIRECTION_R:
            self.animation = self.attack_r_action
            self.move_x = 0
        else:
            self.animation = self.attack_l_action
            self.move_x = 0

    def run(self):
        #Metodo de animacion de correr del enemigo
        if self.direction == DIRECTION_R:
            self.animation = self.run_r_action            
            self.move_x = self.speed_run
        else:
            self.animation = self.run_l_action            
            self.move_x = -self.speed_run

    def die(self):
        #Metodo de animacion de morir del enemigo. Con sonido
        if self.direction == DIRECTION_R:
            self.animation == self.die_r_action
            self.move_x = 0
        else:
            self.animation == self.die_l_action
            self.move_x = 0
        self.die_sound.play()
        
    def automove(self,player):
        '''Gestiona las acciones del personaje por tiempo y cercania'''
        if self.is_dead == False:
            self.time_acumulator +=1  
            print( self.time_acumulator)
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
            if self.in_visual(player):
                self.attack()
            
    def do_movement(self, delta_ms,player,world):
        #Metodo que realiza el cambio de frame
        self.tiempo_transcurrido_move += delta_ms
        if self.tiempo_transcurrido_move >= self.move_rate_ms:
            if (abs(self.y_start_jump) - abs(self.rect.y)) > self.power_jump and self.is_jump:
                self.move_y = 0
            self.tiempo_transcurrido_move = 0
            self.move_rect_x(self.move_x)
            self.move_rect_y(self.move_y) 
            
            if (self.direction == DIRECTION_R and self.rect.x < WINDOWS_WIDTH - self.rect.w*1.8) or (self.direction == DIRECTION_L and self.rect.x > 0):
                self.move_rect_x(self.move_x)

            if self.is_grounded(world) == False:
                self.move_rect_y(self.amount_gravity)
            elif self.is_jump:
                self.jump(False)
            else:
                self.automove(player)  
            if self.life < 1:          
                self.die()
                self.is_dead = True
                player.score += 100
            if self.rect.y > WINDOWS_HEIGHT:
                self.die()
                self.is_dead = True
                
    def is_grounded(self,world):
        #Metodo que regista la colision con el suelo
        m_return = False
        for platform in world.tile_list:
            if self.direction == DIRECTION_R:
                if self.rect_ground_collision_r.colliderect(platform[1]):
                    m_return = True
                    self.in_air = False
                    break
            elif self.direction == DIRECTION_L:
                if self.rect_ground_collision_l.colliderect(platform[1]):
                    m_return = True
                    self.in_air = False
                    break
            else:
                self.in_air = True
                m_return = False
        return m_return

    def is_hit(self,player):
        #Metodo que regista si el player golpeo al enemigo
        m_return = False
        if (self.rect_hit_collision.colliderect(player.rect_attack_collision_r) or self.rect_hit_collision.colliderect(player.rect_attack_collision_l)) and player.is_attack:
            if PRINTS: print("El Heroe me ah Golpeado")  
            self.life -= 1
            if PRINTS: print("vidas enemigo: "+str(self.life))
            m_return = True
        return m_return
    
    def in_visual(self,player):
        #Metodo que permite al enemigo atacar al player si entra en su rango de vision
        m_return = False
        if self.rect_vision.colliderect(player.rect):
            if self.direction == DIRECTION_L:
                self.animation = self.attack_l_action
                m_return = True
            else:
                self.animation = self.attack_r_action
                m_return = True
        return m_return
    
    def move_rect_x(self,delta_x=0):
        '''Mueve los rectangulos en x'''        
        self.rect.x += delta_x
        self.rect_ground_collision_r.x += delta_x
        self.rect_ground_collision_l.x += delta_x
        self.rect_hit_collision.x += delta_x
        self.rect_vision.x += delta_x
        if self.direction == DIRECTION_R:
           self.rect_vision = pygame.Rect(self.rect.x+self.rect.w/1.33,self.rect.y+self.rect.h/3,self.rect.w/4,self.rect.h/4)
        else:
            self.rect_vision = pygame.Rect(self.rect.x,self.rect.y+self.rect.h/3,self.rect.w/4,self.rect.h/4)
        

    def move_rect_y(self,delta_y=0):
        '''Mueve los rectangulos en y'''
        self.rect.y += delta_y
        self.rect_ground_collision_r.y += delta_y
        self.rect_ground_collision_l.y += delta_y
        self.rect_hit_collision.y += delta_y

    def do_animation(self,delta_ms):
        #Metodo que realiza el cambio de frame
        self.elapsed_time_animation += delta_ms
        if self.elapsed_time_animation >= self.frame_rate_ms:
            self.elapsed_time_animation = 0
            if self.frame < len(self.animation) - 1:
                self.frame += 1 
            else:
                self.frame = 0

    def update(self,delta_ms,player,world): 
        #Metodo que actualiza movimiento y animacion
        self.do_movement(delta_ms,player,world)
        self.do_animation(delta_ms)

    def draw(self,screen):
        #Metodo que dibuja por pantalla
        if DEBUG:   
            pygame.draw.rect(screen,C_WHITE,self.rect,2)
            pygame.draw.rect(screen,C_GREEN,self.rect_ground_collision_r,2)
            pygame.draw.rect(screen,C_BLUE,self.rect_ground_collision_l,2)
            pygame.draw.rect(screen,C_RED,self.rect_hit_collision,2)
            pygame.draw.rect(screen,C_RED,self.rect_vision,2)
            
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)