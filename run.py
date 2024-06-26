import pygame as pg
import os, configparser as cf
import player , animation
import camera, stat_monitor, _map

#INIT CONFIG FILE
config = cf.ConfigParser()
config.read('config.ini')


width = int(config['Display']['Width'])
height = int(config['Display']['Height'])


#DISPLAY
window = pg.display.set_mode((width, height), vsync=True)
display = pg.Surface((width//2.5, height//2.5))
clock = pg.time.Clock()
pg.init()

#CLASS OBJECTS
MainPlayer = player.Player_class(20,20)
#initialize camera
Camera = camera.Camera_class(MainPlayer.x , MainPlayer.y)
#initialize stat monitor
monitor = stat_monitor.Monitor()
#initialize MAP
Map = _map.Map()

def eventHandler():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            os._exit(0)

    
    #USING DISPLAY SURFACE TO CREATE DYNAMIC RESOLUTION FOR PIXEL PERFECT RES
    dynamicRes = pg.transform.scale(display, (width, height))
    window.blit(dynamicRes, (0,0))


    #MAIN SURFACE (FOR FONT AND GUI)
    monitor.update(clock, window)

    pg.display.flip()
    clock.tick()


#bg = pg.image.load('data/bck.png')
while True:
    display.fill((30,30,30))
    #window.fill(0)
    #display.blit(bg , (0 - Camera.cameraX,0 - Camera.cameraY))


    #CALL IN MAIN LOOP
    Map.load_map_image(display, Camera.cameraX, Camera.cameraY)
    #= 


    MainPlayer.update(display, Camera.cameraX, Camera.cameraY)
    Camera.update(MainPlayer.x, MainPlayer.y, display)
    Map.load_base_h(MainPlayer, display, Camera.cameraX, Camera.cameraY)
    
    #MOVE
    MainPlayer.x += MainPlayer.dx
    MainPlayer.y += MainPlayer.dy
    eventHandler()    