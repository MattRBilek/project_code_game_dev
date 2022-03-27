# Does not currently work
import pygame as pg
from player import Player
from enemys.enemy import Enemy
from constants import *


class Dropper(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.origin = y
        self.player = Player
        self.width = 50
        self.height = 20
        self.drop = False  # Should this enemy drop
        self.ground = False
        self.y_velocity = 0

    def draw(self, screen):
        pg.draw.rect(screen, [0, 40, 0], (self.x, self.y, self.width, self.height))

    def collide(self, world_object):
        if world_object.type is TYPES.FLOOR:
            self.ground = world_object

    def update(self, keys):
        if not self.grounded and self.player == self.x:
            self.y_velocity = 20

        if self.grounded and not self.y == self.origin:
            self.y_velocity = -10

        if self.y == self.origin:
            self.y_velocity = 0

        self.y += self.y_velocity

