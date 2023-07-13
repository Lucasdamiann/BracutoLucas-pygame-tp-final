import pygame
from constants import *

class Coin:
    def __init__(self,position_x,position_y):
        self.image = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER+"Items\coin\gem_ruby\gem_ruby__x1_1_png_1354831652.png"),(TILE_SIZE/2,TILE_SIZE/2))
        self.rect = self.image.get_rect()
        self.rect.center = (position_x,position_y)
        self.rect_collision = pygame.Rect(self.rect.x,self.rect.y,self.rect.w,self.rect.h)
        self.is_collected = False
        self.gem_sound =  pygame.mixer.Sound(RESOURCES_FOLDER+"Sounds\eGem.wav")

    def draw(self,screen):
        #Metodo que dibuja sobre la pantalla
        if DEBUG:   
            pygame.draw.rect(screen,C_RED,self.rect_collision,2)
        screen.blit(self.image,self.rect)
    
    def collider(self,player):
        #Metodo que regista la colision del enemigo con el botin
        if self.rect_collision.colliderect(player.rect_hit_collision):
            self.is_collected = True
            if PRINTS: print("Gema conseguida")
            self.gem_sound.play()
            player.score += 100
    
    def update(self,player):
        #Metodo que actualiza las colisiones 
        self.collider(player)