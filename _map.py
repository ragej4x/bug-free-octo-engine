import csv
import pygame as pg

class Map:
    def __init__(self) -> None:
        self.base_h_tile = []
        #self.base_h_data = 
        self.base_h_img = pg.image.load('data/map/base_h.png')
        self.base_h_tile_size = 16
        self.base_h = True
        for tile in range(11):
            self.base_h_tile.append (24 * tile)

    def load_base_h(self,MainPlayer, display, cameraX, cameraY):
        self.eventKey = pg.key.get_pressed()
        

        
        with open('data/map/base_h.dat') as self.base_h_data:
            data = csv.reader(self.base_h_data, delimiter=',')
            y = 0
            for row in data:

                x = -1
                for column in range(len(row)):
                    x += 1

                    if row[column] == "1":
                        self.barrier = pg.draw.rect(display, (255,255,255), (x * self.base_h_tile_size - self.base_h_tile_size - cameraX , y * self.base_h_tile_size - cameraY, self.base_h_tile_size , self.base_h_tile_size),1)




                    #COLLISION
                        if self.barrier.colliderect(MainPlayer.player_rect.x + MainPlayer.dx , MainPlayer.player_rect.y, MainPlayer.player_rect.width , MainPlayer.player_rect.height):
                            MainPlayer.dx = 0


                        if self.barrier.colliderect(MainPlayer.player_rect.x + MainPlayer.dx , MainPlayer.player_rect.y, MainPlayer.player_rect.width , MainPlayer.player_rect.height):
                            MainPlayer.dx = 0


                        if self.barrier.colliderect(MainPlayer.player_rect.x, MainPlayer.player_rect.y + MainPlayer.dy, MainPlayer.player_rect.width , MainPlayer.player_rect.height):
                            MainPlayer.dy = 0


                y += 1
        
        #LOAD MAP IMG
    def load_map_image(self, display, cameraX, cameraY):
        def load_map_image():
            display.blit(self.base_h_img, (0 - cameraX, 0 - cameraY))
        
        if self.base_h == True:
            load_map_image()
        