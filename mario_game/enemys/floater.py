import pygame as pg
from player import Player
from enemys.enemy import Enemy
from constants import *


class Floater(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.origin = y
        self.width = 50
        self.height = 50
        self.ground = None
        self.fall = False

    def draw(self, screen):
        pg.draw.rect(screen, [0, 40, 0], (self.x, self.y, self.width, self.height))

    def collide(self, world_object):
        if world_object.type is TYPES.FLOOR:
            self.fall = False
            self.ground = world_object

    def update(self, keys, player=None, enemies=None):
        if not self.on_screen:
            return
        
        if self.origin is self.y:
            self.ground = None

        if self.fall:
            self.y+=10

        elif self.ground is None:
            if player.y > self.y + self.height:
                if player.x < self.x < player.x + player.width or player.x < self.x + self.width < player.x + player.width:
                    self.fall = True
        if not self.fall and self.y is not self.origin:
            self.y -= 2