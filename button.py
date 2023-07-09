import pygame
from constants import *

class Button:
    def __init__(self,position_x,position_y,image):
        self.image = pygame.transform.scale(pygame.image.load(image),(WINDOWS_WIDTH//10,WINDOWS_HEIGHT//8))
        self.rect = self.image.get_rect()
        self.rect.x = position_x
        self.rect.y = position_y
        self.is_clicked = False
        self.click_sound = pygame.mixer.Sound("Juego_freeknight\mis_assets\Sounds\iButtonError.wav")
        
    def draw(self,screen):
        screen.blit(self.image,self.rect)
        if self.click:
            return True

    def click(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.is_clicked = True
                action = True
                self.click_sound.play()
                if PRINTS: print("Me clickeaste")
        if pygame.mouse.get_pressed()[0] == 0:
            self.is_clicked = False
        return action