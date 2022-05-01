import pygame as pg
from enemys.enemy import Enemy
from constants import *


class Bullet(Enemy):
    def __init__(self, x, y, velocity=int(SCREEN_WIDTH / 40 / 2)):
        super().__init__(x, y)
        self.width = 10
        self.height = 5
        self.velocity = velocity
        self.ground = None
        self.on_screen = True

    def draw(self, screen):  # TODO: add is on screen
        if not self.on_screen:
            return
        pg.draw.rect(screen, [66, 66, 66], (self.x, self.y, self.width, self.height))

    def collide(self, world_object):
        if world_object.type is TYPES.FLOOR:
            self.ground = world_object

    def update(self, keys, player=None, enemies=None):
        if not self.on_screen:
            self.dead = True
            return

        self.x -= self.velocity
