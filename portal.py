import pygame
from constants import *
from auxiliar import Auxiliar
class Portal:
    def __init__(self,position_x,position_y):
        self.idle_action = Auxiliar.getSurfaceFromSpriteSheet(RESOURCES_FOLDER+"tileset\portal\portal__x1_closed_png_1354837277.png",10,3,False,2,1)
        self.animation = self.idle_action
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = position_x
        self.rect.y = position_y
        self.rect_collision = pygame.Rect(self.rect.x+self.rect.w/4,self.rect.y+25,self.rect.w/2,self.rect.h/3)
        self.frame_rate_ms = 250
        self.is_reached = False
        self.level_2 = False
        self.level_3 = False
        self.level_final = False
        self.open_sound = pygame.mixer.Sound(RESOURCES_FOLDER+"Sounds\\aDoor.wav")
        self.elapsed_time_animation = 0

    def collider(self,player,delta_ms):
        self.elapsed_time_animation += delta_ms
        if self.rect_collision.colliderect(player.rect_hit_collision) and not self.is_reached:
            self.open_sound.play()
            if self.elapsed_time_animation > 70:
                self.is_reached = True

    def do_animation(self,delta_ms):
        self.elapsed_time_animation += delta_ms
        if self.elapsed_time_animation >= self.frame_rate_ms:
            self.elapsed_time_animation = 0
            if self.frame < len(self.animation) -1:
                self.frame += 1 
            else:
                self.frame = 0

    def update(self,delta_ms,player): 
        self.do_animation(delta_ms)
        self.collider(player,delta_ms)

    def draw(self,screen):
        if DEBUG:   
            pygame.draw.rect(screen,C_WHITE,self.rect,2)
            pygame.draw.rect(screen,C_GREEN,self.rect_collision,2)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)