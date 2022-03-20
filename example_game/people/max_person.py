import pygame as pg


class MyPerson:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 15
        self.collided = False;
        self.colour = [100, 100, 100];

    def draw(self, screen):
        pg.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))

    def update(self):
        if self.collided:
            self.colour = [30, 255, 100]
        else:
            self.colour = [255, 0, 0]