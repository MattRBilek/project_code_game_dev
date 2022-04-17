# Does not currently work
import pygame as pg
from player import Player
from enemys.enemy import Enemy
from constants import *


class Dropper(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 50
        self.height = 50
        self.ground = None

    def draw(self, screen):
        pg.draw.rect(screen, [0, 40, 0], (self.x, self.y, self.width, self.height))

    def collide(self, world_object):
        if world_object.type is TYPES.FLOOR:
            self.ground = world_object

    def update(self, keys, player=None, enemies=None):
        if not self.on_screen:
            return

        if not self.grounded:
            self.y += 5
        elif self.ground is not None:
            # jump right x = self.ground.width + self.ground.x + self.width
            # jump left  x = self.ground.x - self.width
            if player.y > self.y + self.height + self.ground.height:
                if player.x < self.ground.x < player.x + player.width:
                    self.x = self.ground.x - self.width
                elif player.x < self.ground.x + self.ground.width < player.x + player.width:
                    self.x = self.ground.width + self.ground.x + self.width
