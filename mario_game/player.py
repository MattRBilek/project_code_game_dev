import constants
import pygame as pg
import time

class Player:
    def __init__(self,x,y):
        self.up = 6
        self.down = 0
        self.x = x
        self.y = y
        self.width = constants.SCREEN_WIDTH/25 # TODO: make this scale with constancts.SCREEN_WIDTH / some number
        self.height = constants.SCREEN_HEIGHT/30 # TODO: make this scale with constancts.SCREEN_HEIGHT / some number
        self.color = [200, 100, 100]
        self.grounded = False # should we fall
        self.type = constants.TYPES.PLAYER
        self.y_velocity = 0

    def draw(self, screen):
        pg.draw.rect(screen,self.color,(self.x, self.y, self.width, self.height))

    def collide(self, world_object):
        pass # TODO: collided with object see type with type

    def update(self, keys):
        if keys[pg.K_SPACE] and self.grounded:    # jumping
            self.y_velocity = -20
            self.y += self.y_velocity

        if not self.grounded:
            self.y_velocity += 1
            self.y_velocity = min(self.y_velocity, 10)

            self.y += self.y_velocity
            # TODO: falling
        # TODO: anything else
