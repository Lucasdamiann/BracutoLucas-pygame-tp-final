import pygame
import sqlite3
from constants import *
class Ranking:
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load("Juego_freeknight\mis_assets\\btn\Banner01.png"),(WINDOWS_WIDTH/2,WINDOWS_HEIGHT/2))
        self.player_name = None

    def create_db(self):
        #crea la base de datos
        connection = sqlite3.connect("ranking.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS ranking (name TEXT,score TEXT)")  
        connection.close()

    def insert_player(self,score):
        #inserta valores a la tabla de la base de datos
        connection = sqlite3.connect("ranking.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO ranking VALUES (?,?)",(self.player_name,score))
        connection.commit()
        connection.close()
    
    def print_ranking(self,screen):
        #imprime la tabla ranking
        connection = sqlite3.connect("ranking.db")
        cursor = connection.cursor()
        cursor.execute("SELECT name, score FROM ranking")
        rows = cursor.fetchmany(5)
        row_acumulator = 0
        for row in rows:
            print(row)
            name = row[0]
            score = row[1]
            line = "{0}: {1}\n".format(name,score)
            row_acumulator += 50
            menu_text = pygame.font.SysFont("Arial",50).render(line,True,C_BLACK)
            screen.blit(menu_text,menu_text.get_rect(center=(WINDOWS_WIDTH/2,WINDOWS_HEIGHT/3+row_acumulator)))
        row_acumulator = 0
        connection.close()

