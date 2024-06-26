import pygame as pg
import os, configparser as cf
import player , animation
import camera

#INIT CONFIG FILE
config = cf.ConfigParser()
config.read('config.ini')


width = int(config['Display']['Width'])
height = int(config['Display']['Height'])


#DISPLAY
window = pg.display.set_mode((width, height))
display = pg.Surface((width//2.5, height//2.5))
clock = pg.time.Clock()
pg.init()

#CLASS OBJECTS
MainPlayer = player.Player_class(0,0)
#initialize camera
Camera = camera.Camera_class(MainPlayer.x , MainPlayer.y)

def eventHandler():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            os._exit(0)
    
    #USING DISPLAY SURFACE TO CREATE DYNAMIC RESOLUTION FOR PIXEL PERFECT RES
    dynamicRes = pg.transform.scale(display, (width, height))
    window.blit(dynamicRes, (0,0))

    pg.display.flip()
    clock.tick(60)



bg = pg.image.load('data/bck.png')
while True:
    
    display.fill((30,30,30))
    #window.fill(0)
    display.blit(bg , (0 - Camera.cameraX,0 - Camera.cameraY))
    #CALL IN MAIN LOOP
    MainPlayer.update(display, Camera.cameraX, Camera.cameraY)
    Camera.update(MainPlayer.x, MainPlayer.y)
    
    

    eventHandler()

    
    