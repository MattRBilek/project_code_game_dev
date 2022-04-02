import pygame as pg
from mario_game.enemys.enemy import Enemy
from mario_game.constants import *

class Jumper(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 20
        self.height = 20
        self.velocity = int(SCREEN_WIDTH / 100 / 10)
        self.ground = None
        self.y_velocity = 0

    def draw(self, screen):
        pg.draw.rect(screen, (100, 100, 0), (self.x, self.y, self.width, self.height))

    def collide(self, world_object):
        if world_object.type is TYPES.FLOOR:
            self.ground = world_object


    def update(self, keys, player=None, enemies=None):
        if not self.on_screen:
            return

        if self.grounded:
            self.y_velocity = -20
        elif not self.grounded:
            self.y_velocity += 1

        self.y += self.y_velocity
        self.x += self.velocity