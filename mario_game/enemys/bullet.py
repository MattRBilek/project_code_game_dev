import pygame as pg
from enemys.enemy import Enemy
from constants import *


class Bullet(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 50
        self.height = 50
        self.velocity = int(SCREEN_WIDTH / 40 / 2)
        self.ground = None

    def draw(self, screen):  # TODO: add is on screen
        pg.draw.rect(screen, [66, 66, 66], (self.x, self.y, self.width, self.height))

    def collide(self, world_object):
        if world_object.type is TYPES.FLOOR:
            self.ground = world_object

    def update(self, keys, player=None, enemies=None):
        if not self.on_screen:
            return

        elif self.ground is None:
            self.x -= self.velocity