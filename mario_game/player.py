import constants
import pygame as pg

class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 50 # TODO: make this scale with constancts.SCREEN_WIDTH / some number
        self.height = 50 # TODO: make this scale with constancts.SCREEN_HEIGHT / some number
        self.grounded = False # should we fall
        self.going_up = False # keep track of if u are jumping or not
        self.type = constants.TYPES.PLAYER

    def draw(self, screen):
        pass # TODO: draw picture of player

    def collide(self, world_object):
        pass # TODO: collided with object see type with type

    def update(self, keys):
        if keys[pg.K_SPACE]:
            pass # TODO: something while pressing space

        if self.grounded and not self.going_up:
            pass # TODO: falling

        # TODO: anything else
