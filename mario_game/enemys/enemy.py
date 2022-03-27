import constants as constants


class Enemy:
    def __init__(self, x, y):  # TODO: add is on screen
        self.x = x
        self.y = y
        self.width = None
        self.height = None
        self.grounded = False  # should we fall
        self.type = constants.TYPES.ENEMY
        self.dead = False
        self.on_screen = False

    def draw(self, screen):
        pass

    def collide(self, world_object):
        pass

    def update(self, keys):
        pass
