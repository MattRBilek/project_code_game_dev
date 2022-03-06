from mario_game import constants

class Enemy:
    def __init__(self,x,y):     # TODO: add is on screen
        self.x = x
        self.y = y
        self.width = None
        self.height = None
        self.grounded = False # should we fall
        self.going_up = False # keep track of if u are jumping or not
        self.type = constants.TYPES.ENEMY

    def draw(self, screen):
        pass

    def collide(self, world_object):
        pass

    def update(self, keys):
        pass