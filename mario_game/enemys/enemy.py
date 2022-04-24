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
        self.name = "base"


    ### pass in dictionary that holds data
    def load_from_json(self, dict):
        pass ### use dict to extract data

    ### store data to string and return
    def strore_to_json(self):
        return "{'type' : "+self.name+", 'x'"+self.x+",'y':"+self.y+"}"

    def draw(self, screen):
        pass

    def collide(self, world_object):
        pass

    def update(self, keys, player=None, enemies=None):
        pass
