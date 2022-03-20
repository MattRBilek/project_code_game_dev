import pygame as pg
import time
from copy import copy, deepcopy

from people.max_person import MyPerson
from people.new_class import NewPerson
from people.test_person import Example

GRAY = [225,225,225]

def collided(self, collider):
    if self.x < collider.x + collider.width and \
            self.x + self.width > collider.x and \
            self.y < collider.y + collider.height and \
            self.y + self.height > collider.y:
        return True
    return False


class Game:
    def __init__(self, fps=1): # constructor
        self.fps = fps
        self.width = 600
        self.height = 600
        self.people = [Example(50,50),MyPerson(50,100),NewPerson(74,74)]

    def game_initiating_window(self):
        if self.fps == 0:
            return
        self.screen = pg.display.set_mode((self.width, self.height), 0, 32)

        # updating the display
        pg.display.update()

    def draw(self):
        self.screen.fill(GRAY)
        for person in self.people:
            person.draw(self.screen)

    def run(self):

        self.game_initiating_window()
        running = True
        if not self.fps == 0:
            CLOCK = pg.time.Clock()
        while running:
            if not self.fps == 0:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        return
            for person1 in self.people:
                for person2 in self.people:
                    if person2 != person1 and collided(person2, person1):
                        person2.collided = True
                        person1.collided = True

            for person in self.people:
                person.update()

            if not self.fps == 0:
                self.draw()
                pg.display.update()
                CLOCK.tick(self.fps)
        if not self.fps == 0:
            pg.quit()
