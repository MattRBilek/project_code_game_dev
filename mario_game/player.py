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
        self.colour = [200, 100, 100]
        self.grounded = False # should we fall
        self.going_up = False # keep track of if u are jumping or not
        self.type = constants.TYPES.PLAYER

    def draw(self, screen):
        pg.draw.rect(screen,self.colour,(self.x, self.y, self.width, self.height))
        pass # TODO: draw picture of player

    def collide(self, world_object):
        pass # TODO: collided with object see type with type

    def update(self, keys):
        if keys[pg.K_SPACE] and self.collide:
            self.going_up = True
            self.y -= 5
            self.going_up = False
            self.up = 6
            # TODO: something while pressing space

        if not self.grounded and not self.going_up:
            self.y += 3
            # TODO: falling
        # TODO: anything else
