#Does not currently work
import pygame as pg
from enemys.enemy import Enemy
import time
from constants import *
from enemys.bullet import Bullet


class Shooter(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 40
        self.height = 40
        self.ground = None
        self.clip = 0
        self.old_epoch = 0.0

    def draw(self, screen):  # TODO: add is on screen
        pg.draw.rect(screen, [60, 40, 80], (self.x, self.y, self.width, self.height))

    def collide(self, world_object):
        if world_object.type is TYPES.FLOOR:
            self.ground = world_object

    def update(self, keys, player=None, enemies=None):
        if not self.on_screen:
            self.old_epoch = time.time()
            return
        if not self.ground:
            self.y += 10

        if time.time() - self.old_epoch > 4: # four seconds have passed
            enemies.append(Bullet(self.x, self.y))
            self.clip += 1
            self.old_epoch = time.time()

