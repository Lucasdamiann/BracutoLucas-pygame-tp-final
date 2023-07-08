import pygame
from enemy import Enemy
from auxiliar import Auxiliar
from constants import *
from coins import Coin
class Surfaces:
    def __init__(self,data):
        self.floor_l = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER +"tileset\graveyard\Tiles\Tile (1).png"),(TILE_SIZE,TILE_SIZE))
        self.floor_c = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER+"tileset\graveyard\Tiles\Tile (2).png"),(TILE_SIZE,TILE_SIZE))
        self.floor_r = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER+"tileset\graveyard\Tiles\Tile (3).png"),(TILE_SIZE,TILE_SIZE))
        self.skelleton_l = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER+"tileset\graveyard\Objects\Skeleton.png"),(TILE_SIZE,TILE_SIZE/2))
        self.deadbush = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER+"tileset\graveyard\Objects\DeadBush.png"),(TILE_SIZE,TILE_SIZE/2))
        self.bush = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER+"tileset\graveyard\Objects\Bush (2).png"),(TILE_SIZE,TILE_SIZE/2))
        self.arrowsign = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER+"tileset\graveyard\Objects\ArrowSign.png"),(TILE_SIZE,TILE_SIZE/2))
        self.tree = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER+"tileset\graveyard\Objects\Tree.png"),(TILE_SIZE*2,TILE_SIZE*2))
        self.life_bar = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER+"Bars\Bar_Segment01.png"),(TILE_SIZE/2,TILE_SIZE/4))
        self.tile_list = []   
        self.life_list = []
        row_counter = 0
        for row in data:
            col_counter = 0
            for tile in row:
                if tile == 1:
                    img = self.floor_l     
                    img_rect = img.get_rect() 
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)             
                elif tile == 2:
                    img = self.floor_c    
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)               
                elif tile == 3:
                    img = self.floor_r  
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)              
                elif tile == 4:
                    img = self.skelleton_l
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                elif tile == 5:
                    img = self.deadbush
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)   
                elif tile == 6:
                    img = self.bush
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                elif tile == 7:
                    img = self.arrowsign
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                elif tile == 8:
                    img = self.tree
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                elif tile == 9:
                    img = self.life_bar
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.life_list.append(tile)
                col_counter += 1
            row_counter += 1

    def draw(self,screen):
        for tile in self.tile_list:
            screen.blit(tile[0],tile[1])

    def draw_life(self,screen):
        for life in self.life_list:
            screen.blit(life[0],life[1])   


