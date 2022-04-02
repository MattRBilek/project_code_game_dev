import enum

GRAY = [225, 225, 225]
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600


class TYPES(enum.IntEnum):
    PLAYER = 0
    ENEMY = 1
    OBJECT = 2
    FLOOR = 3
    FLAG = 4


# returns true if object1 has collided with collider
def collided(object1, collider):
    if object1.x < collider.x + collider.width and \
            object1.x + object1.width > collider.x and \
            object1.y < collider.y + collider.height and \
            object1.y + object1.height > collider.y:
        return True
    return False


# returns true if object1 is on top of the collider with a slight buffer
def on_top_of(object1, collider):
    if object1.x < collider.x + collider.width and \
            object1.x + object1.width > collider.x and \
            object1.y + object1.height > collider.y > object1.y:
        return True
    return False
