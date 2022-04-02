import pygame as pg
from enemys.enemy import Enemy
from constants import *


class Mover(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 50
        self.height = 50
        self.velocity = int(SCREEN_WIDTH / 60 / 6)
        self.ground = None

    def draw(self, screen):  # TODO: add is on screen
        pg.draw.rect(screen, [0, 255, 0], (self.x, self.y, self.width, self.height))

    def collide(self, world_object):
        if world_object.type is TYPES.FLOOR:
            self.ground = world_object

    def update(self, keys, player=None, enemies=None):
        if not self.on_screen:
            return

        if not self.grounded:
            self.y += 3
        elif self.ground is not None:
            if self.x + self.width > self.ground.width + self.ground.x:
                self.velocity *= -1
            elif self.x < self.ground.x:
                self.velocity *= -1

            self.x += self.velocity
