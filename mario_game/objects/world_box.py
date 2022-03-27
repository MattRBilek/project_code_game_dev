import constants


class WorldBox:
    def __init__(self):     # TODO: add is on screen
        self.x = -100
        self.y = -100
        self.width = constants.SCREEN_WIDTH + 200
        self.height = constants.SCREEN_HEIGHT + 200

    def draw(self, screen):
        pass
    def collide(self, world_object):
        pass