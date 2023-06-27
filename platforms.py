import pygame
from constants import *
from auxiliar import Auxiliar


class Platform:
    def __init__(self,position_x,position_y,width,height,):
        self.image = pygame.image.load(RESOURCES_FOLDER+TILES_FOLDER+"Tile (15).png")
        self.image = pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = position_x
        self.rect.y = position_y
        self.rect_ground_collision = pygame.Rect(self.rect.x,self.rect.y+self.rect.h-52,self.rect.w,10)

    def draw(self,screen):
        if DEBUG:   
            pygame.draw.rect(screen,C_ORANGE,self.rect)
            pygame.draw.rect(screen,C_GREEN,self.rect_ground_collision)
        screen.blit(self.image,self.rect)
         