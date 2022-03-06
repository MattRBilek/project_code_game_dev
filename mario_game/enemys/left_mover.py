import pygame as pg
from mario_game.enemys.enemy import Enemy


class LeftMover(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 50
        self.height = 50

    def draw(self, screen):     # TODO: add is on screen
        pg.draw.rect(screen, [255, 0, 255], (self.x, self.y, self.width, self.height))

    def collide(self, world_object):
        pass

    def update(self, keys):
        if not self.grounded:
            self.y += 3
        self.x -= 1
