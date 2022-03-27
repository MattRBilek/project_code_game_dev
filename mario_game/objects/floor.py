import constants
import pygame as pg


class Floor:
    def __init__(self, x, y, width=200, height=20):     # TODO: add is on screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = constants.TYPES.FLOOR

    def draw(self, screen):
        pg.draw.rect(screen, [255, 255, 255], (self.x, self.y, self.width, self.height))

    def collide(self, world_object):
        pass
