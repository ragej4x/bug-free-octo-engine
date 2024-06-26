import math, pygame as pg
import configparser as cf 
import player
#INIT CONFIG FILE
config = cf.ConfigParser()
config.read('config.ini')

class Camera_class():
    def __init__(self, x ,y) -> None:
        self.cameraX = x
        self.cameraY = y
        self.cameraPosX = x 

        self.center_pos_width = int(config['Display']['Width']) // 4.5
        self.center_pos_height = int(config['Display']['Height']) // 4.5


        self.speed = 1.5
        
    def update(self, x, y, window):
        rect  = pg.Rect((x - self.cameraX , y - self.cameraY, 24, 24))
        center_col = pg.Rect((self.center_pos_width - 30 , self.center_pos_height - 35, 5, 5))


        if not center_col.colliderect(rect):

            angle = math.atan2(y - int(config['Display']['Height']) // 6 - self.cameraY, x - int(config['Display']['Width']) // 5.5 - self.cameraX)
            cdx = math.cos(angle)
            cdy = math.sin(angle)


            self.cameraX += cdx * self.speed
            self.cameraY += cdy * self.speed
            


        #print(rect.x , rect.y, self.cameraY, self.center_pos_height)