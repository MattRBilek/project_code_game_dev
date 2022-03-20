import pygame as pg
import pygame.draw


class NewPerson:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25
        self.collided = False

    def draw(self, screen):
        pygame.draw.rect(screen, [0, 0, 255], (self.x, self.y, self.width, self.height))

    def move_up(self, distance):
        self.y -= distance

    def update(self):
        self.move_up(0 if not self.collided else 0)
        self.collided = False
