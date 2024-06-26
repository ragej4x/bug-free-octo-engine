import configparser
import pygame as pg

config = configparser.ConfigParser()
config.read('config.ini')

class Monitor():
    def __init__(self) -> None:
        self.font = pg.font.Font('data/rainyhearts.ttf', 24)

        self.show_fps = bool(config['Stat_monitor']['Display_fps'])
        self.show_pos = bool(config['Stat_monitor']['Display_pos'])

    def update(self, clock, window):
        def display_fps():
            get_fps = str(int(clock.get_fps()))
            blit_fps = self.font.render(get_fps, True, (200,200,200))
            window.blit(blit_fps,(10 , 10))


        if self.show_fps == True:
            display_fps()