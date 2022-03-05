import pygame as pg
class Example:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25
        self.collided = False
        self.colour = [255,0,0]

    def draw(self, screen):
        pg.draw.rect(screen,self.colour,(self.x, self.y, self.width, self.height))

    def update(self):
        if self.collided:
            self.colour = [255,0,255]
        else:
            self.colour = [255, 0, 0]