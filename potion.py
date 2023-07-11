import pygame
from auxiliar import Auxiliar
from constants import *
class Potion:
    def __init__(self,position_x,position_y):
        self.image = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER+"Items\potion_amorous_philtre\potion_amorous_philtre__x1_1_png_1354836963.png"),(TILE_SIZE/2,TILE_SIZE/1.5))
        self.is_collected = False
        self.potion_sound =  pygame.mixer.Sound(RESOURCES_FOLDER+"Sounds\eMix.wav")
        self.rect = self.image.get_rect()
        self.rect.center = (position_x,position_y)
        self.rect_collision = pygame.Rect(self.rect.x+self.rect.w/4,self.rect.y,self.rect.w/1.2,self.rect.h)

    def draw(self,screen):
        if DEBUG:   
            pygame.draw.rect(screen,C_RED,self.rect_collision,2)
        screen.blit(self.image,self.rect)
    
    def collider(self,player,world):
        if self.rect_collision.colliderect(player.rect_hit_collision):
            self.potion_sound.play()
            if PRINTS: print("Pocion consumida")
            world.life_list.append((world.life_bar,world.life_bar.get_rect()))
            player.life_bar = 100
            self.is_collected = True

    def update(self,player,world): 
        self.collider(player,world)