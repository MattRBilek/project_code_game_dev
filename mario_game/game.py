import pygame as pg
import time
import constants
from mario_game.enemys.left_mover import LeftMover
from mario_game.objects.floor import Floor
from mario_game.player import Player


class Game:
    def __init__(self, fps=60):
        self.fps = fps
        self.width = constants.SCREEN_WIDTH
        self.height = constants.SCREEN_HEIGHT
        self.player = Player(int(constants.SCREEN_WIDTH / 2), int(constants.SCREEN_HEIGHT / 2))
        self.enemies = [LeftMover(800, 100)]
        self.objects = [Floor(600, 400)]
        self.running = True
        self.screen = None

    def game_initiating_window(self):   # inits the windows
        if self.fps == 0:
            return
        self.screen = pg.display.set_mode((self.width, self.height), 0, 32)

        # updating the display
        pg.display.update()

    def draw(self):
        self.screen.fill(constants.GRAY)
        for world_object in self.objects:
            world_object.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)

        self.player.draw(self.screen)

    def run(self):  # main game loop
        self.game_initiating_window()

        if not self.fps == 0:
            CLOCK = pg.time.Clock()

        while self.running:
            if not self.fps == 0:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        return

            keys = pg.key.get_pressed()

            self.handle_inputs(keys)
            self.update(keys)

            if not self.fps == 0:
                self.draw()
                pg.display.update()
                CLOCK.tick(self.fps)
        if not self.fps == 0:
            pg.quit()

    def update(self, keys):
        for enemy in self.enemies:
            if constants.on_top_of(self.player, enemy):
                enemy.dead = True  # player on top of enemy
            elif constants.collided(self.player, enemy):
                self.running = False  # collided with player
            enemy.grounded = False
            for world_object in self.objects:
                if constants.on_top_of(enemy, world_object):
                    enemy.grounded = True
                    enemy.collide(world_object)

        self.player.grounded = False
        for world_object in self.objects:
            if constants.on_top_of(self.player, world_object):
                self.player.grounded = True
                self.player.collide(world_object)

        self.player.update(keys)
        for enemy in self.enemies:
            enemy.update(keys)

    def handle_inputs(self, keys):
        pass  # TODO: handle player inputs
