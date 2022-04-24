import constants
import pygame as pg


class XObject:
    def __init__(self, x, y, width=50, height=50):     # TODO: add is on screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = constants.TYPES.OBJECT

    def draw(self, screen):
        pg.draw.rect(screen, [100, 0, 0], (self.x, self.y, self.width, self.height))

    def collide(self, world_object):
        if self.y > world_object.y + world_object.height - 20:
            return 0
        if self.x - world_object.x + self.width/2 - world_object.width/2 > 0:
            return self.x - world_object.width - world_object.x
        return self.x + self.width - world_object.x