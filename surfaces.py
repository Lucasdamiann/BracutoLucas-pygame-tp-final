import pygame
from constants import *

class Surfaces:
    def __init__(self,data):
        self.floor_l = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER +"tileset\graveyard\Tiles\\1.png"),(TILE_SIZE,TILE_SIZE))
        self.floor_c = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER +"tileset\graveyard\Tiles\\2.png"),(TILE_SIZE,TILE_SIZE))
        self.floor_r = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER +"tileset\graveyard\Tiles\\3.png"),(TILE_SIZE,TILE_SIZE))
        self.platform_l = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER +"tileset\graveyard\Tiles\\4.png"),(TILE_SIZE,TILE_SIZE))
        self.platform_c = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER +"tileset\graveyard\Tiles\\5.png"),(TILE_SIZE,TILE_SIZE))
        self.platform_r = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER +"tileset\graveyard\Tiles\\6.png"),(TILE_SIZE,TILE_SIZE))
        self.floor_l_snow = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER +"tileset\winter\Tiles\\1.png"),(TILE_SIZE,TILE_SIZE))
        self.floor_c_snow = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER +"tileset\winter\Tiles\\2.png"),(TILE_SIZE,TILE_SIZE))
        self.floor_r_snow = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER +"tileset\winter\Tiles\\3.png"),(TILE_SIZE,TILE_SIZE))
        self.platform_l_snow = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER +"tileset\winter\Tiles\\14.png"),(TILE_SIZE,TILE_SIZE))
        self.platform_c_snow = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER +"tileset\winter\Tiles\\15.png"),(TILE_SIZE,TILE_SIZE))
        self.platform_r_snow = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER +"tileset\winter\Tiles\\16.png"),(TILE_SIZE,TILE_SIZE))
        self.floor_l_forest = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER +"tileset\\forest\Tiles\\1.png"),(TILE_SIZE,TILE_SIZE))
        self.floor_c_forest = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER +"tileset\\forest\Tiles\\2.png"),(TILE_SIZE,TILE_SIZE))
        self.floor_r_forest = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER +"tileset\\forest\Tiles\\3.png"),(TILE_SIZE,TILE_SIZE))
        self.platform_l_forest = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER +"tileset\\forest\Tiles\\13.png"),(TILE_SIZE,TILE_SIZE))
        self.platform_c_forest = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER +"tileset\\forest\Tiles\\14.png"),(TILE_SIZE,TILE_SIZE))
        self.platform_r_forest = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER +"tileset\\forest\Tiles\\15.png"),(TILE_SIZE,TILE_SIZE))
        self.skelleton_l = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER+"tileset\graveyard\Objects\Skeleton.png"),(TILE_SIZE/2,TILE_SIZE/2))
        self.tombstone = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER+"tileset\graveyard\Objects\TombStone (1).png"),(TILE_SIZE,TILE_SIZE))
        self.bush = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER+"tileset\graveyard\Objects\Bush (1).png"),(TILE_SIZE/2,TILE_SIZE/2))
        self.arrowsign = pygame.transform.scale(pygame.image.load(RESOURCES_FOLDER+"tileset\graveyard\Objects\ArrowSign.png"),(TILE_SIZE,TILE_SIZE))
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
                    img = self.tombstone
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
                elif tile == 10:
                    img = self.floor_l_snow
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                elif tile == 11:
                    img = self.floor_c_snow
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                elif tile == 12:
                    img = self.floor_r_snow
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                elif tile == 13:
                    img = self.floor_l_forest
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                elif tile == 14:
                    img = self.floor_c_forest
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                elif tile == 15:
                    img = self.floor_r_forest
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                elif tile == 16:
                    img = self.platform_l
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                elif tile == 17:
                    img = self.platform_c
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                elif tile == 18:
                    img = self.platform_r
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                elif tile == 19:
                    img = self.platform_l_snow
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                elif tile == 20:
                    img = self.platform_c_snow
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                elif tile == 21:
                    img = self.platform_r_snow
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                elif tile == 22:
                    img = self.platform_l_forest
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                elif tile == 23:
                    img = self.platform_c_forest
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                elif tile == 24:
                    img = self.platform_r_forest
                    img_rect = img.get_rect()
                    img_rect.x = col_counter * TILE_SIZE
                    img_rect.y = row_counter * TILE_SIZE
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                col_counter += 1
            row_counter += 1

    def draw(self,screen):
        for tile in self.tile_list:
            screen.blit(tile[0],tile[1])
            if DEBUG:
                pygame.draw.rect(screen,C_RED,tile[1],2)

    def draw_life(self,screen):
        for life in self.life_list:
            screen.blit(life[0],life[1])   