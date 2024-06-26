import configparser
import pygame as pg

config = configparser.ConfigParser()
config.read('config.ini')

class Monitor():
    def __init__(self) -> None:
        self.font = pg.font.Font()

    def update(self):
        pass