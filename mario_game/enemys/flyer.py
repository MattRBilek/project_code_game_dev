import pygame as pg
from enemys.enemy import Enemy
from constants import *


class Flyer(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.origin = x
        self.width = 60
        self.height = 20
        self.velocity = int(SCREEN_WIDTH / 50 / 5)

    def draw(self, screen):
        pg.draw.rect(screen, [255, 255, 255], (self.x, self.y, self.width, self.height))

    def update(self, keys, player=None, enemies=None):
        if not self.on_screen:
            return
        if self.x + self.width > self.origin + 100:
            self.velocity *= -1
        elif self.x < self.origin - 100:
            self.velocity *= -1

        self.x += self.velocity
