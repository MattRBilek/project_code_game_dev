import pygame as pg
from player import Player
from enemys.enemy import Enemy
from constants import *


class Charger(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 50
        self.height = 30
        self.ground = None
        self.charge = False
        self.velocity = int(SCREEN_WIDTH / 40 / 4)

    def draw(self, screen):
        pg.draw.rect(screen, [90, 200, 90], (self.x, self.y, self.width, self.height))

    def collide(self, world_object):
        if world_object.type is TYPES.FLOOR:
            self.ground = world_object

    def update(self, keys, player=None, enemies=None):
        if not self.on_screen:
            return
        if not self.grounded:
            self.y += 10
        if self.grounded is not None and self.y + self.height == player.y + player.height:
            if player.x + 300 > self.x > player.x - 300:
                self.charge = True
        if self.charge:
            if player.x > self.x:
                self.x += self.velocity
            elif player.x < self.x:
                self.x -= self.velocity