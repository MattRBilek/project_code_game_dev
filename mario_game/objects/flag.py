from mario_game import constants
import pygame as pg


class Flag:
    def __init__(self, x, y, width=100, height=50):     # TODO: add is on screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = constants.TYPES.FLAG



    def draw(self, screen):
        pg.draw.rect(screen, [0, 255, 255], (self.x, self.y, self.width, self.height))

    def collide(self, world_object):
        pass