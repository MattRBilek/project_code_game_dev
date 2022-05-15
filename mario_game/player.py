import constants
import pygame as pg
import time

image_width = 200
image_height = 200


class Player:
    def __init__(self,x,y):
        self.up = 6
        self.down = 0
        self.x = x
        self.y = y
        self.width = 200 #constants.SCREEN_WIDTH/25 # TODO: make this scale with constancts.SCREEN_WIDTH / some number
        self.height = 200 #constants.SCREEN_HEIGHT/30 # TODO: make this scale with constancts.SCREEN_HEIGHT / some number
        self.color = [200, 100, 100]
        self.grounded = False # should we fall
        self.type = constants.TYPES.PLAYER
        self.y_velocity = 0
        self.left = False
        self.right = False
        self.image = pg.image.load("Spritesheet.png")
        self.image = pg.transform.scale(self.image, (800, 800))
        self.moveing_left = True
        self.image_x = 0
    def draw(self, screen):
        screen.blit(self.image, (self.x,self.y), ((int(self.image_x) % 4) * image_width,
                                                  (2 + (not self.moveing_left)) * image_height,image_width,image_height))

    def collide(self, world_object):
        pass # TODO: collided with object see type with type

    def update(self, keys):
        if keys[pg.K_SPACE] and self.grounded:    # jumping
            self.y_velocity = -20
            self.y += self.y_velocity

        if keys[pg.K_d]:
            self.moveing_left = False
            self.image_x += .05
        elif keys[pg.K_a]:
            self.moveing_left = True
            self.image_x += .05

        if not self.grounded:
            self.y_velocity += 1
            self.y_velocity = min(self.y_velocity, 10)

            self.y += self.y_velocity
            # TODO: falling
        # TODO: anything else
