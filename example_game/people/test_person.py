import pygame as pg
class Example:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25
        self.collided = False

    def draw(self, screen):
        colour = [255,0,0]
        pg.draw.rect(screen,colour,(self.x, self.y, self.width, self.height))

    def update(self):
        pass