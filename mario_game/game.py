import pygame as pg
import constants
import time
from enemys.dropper import Dropper
from enemys.bullet import Bullet
from enemys.floater import Floater
from enemys.shooter import Shooter
# from enemys.charger import Charger
# from enemys.jumper import Jumper
# from enemys.flyer import Flyer
# from enemys.mover import Mover
# from mario_game.objects.flag import Flag
from objects.floor import Floor
from objects.object import XObject
from objects.world_box import WorldBox
from player import Player


class Game:
    def __init__(self, fps=60):
        self.fps = fps
        self.width = constants.SCREEN_WIDTH
        self.height = constants.SCREEN_HEIGHT
        self.player = Player(int(constants.SCREEN_WIDTH / 2), int(constants.SCREEN_HEIGHT / 2))
        self.enemies = [Dropper(950, 0), Floater(800, 20), Shooter(1000, 200)]
        self.timer = time.time()
        self.objects = [Floor(900, 100), Floor(600, 400, width=1000), XObject(700, 340)]
        self.world_box = WorldBox()
        self.running = True
        self.screen = None

    def new_game_from_json(self, fps, file_name):
        self.fps = fps
        self.width = constants.SCREEN_WIDTH
        self.height = constants.SCREEN_HEIGHT

        self.timer = time.time()

        self.world_box = WorldBox()
        self.running = True
        self.screen = None

        json_data = {}  # load json from filename

        self.objects = []  # update this with json data
        self.enemies = []
        self.player = Player(int(constants.SCREEN_WIDTH / 2), int(constants.SCREEN_HEIGHT / 2))

        for enemy in json_data["enemies"]: # DO ENEMIES
            if enemy["type"] == "dropper":
                self.enemies.append(Dropper(enemy["x"], enemy["y"]))

        for object in json_data["objects"]: # DO OBJECTS
            pass

        player_data = json_data["player"] # DO PLAYER


    def game_initiating_window(self):  # inits the windows
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

        self.player.update(keys)
        for enemy in self.enemies:
            enemy.update(keys, self.player, self.enemies)

        for enemy in self.enemies:
            enemy.on_screen = False
            if constants.on_top_of(self.player, enemy):
                enemy.dead = True  # player on top of enemy

            elif constants.collided(self.player, enemy):
                self.running = False  # collided with player
            if constants.collided(self.world_box, enemy):
                enemy.on_screen = True

            enemy.grounded = False
            for world_object in self.objects:
                if constants.on_top_of(enemy, world_object) and world_object.type != constants.TYPES.FLAG:
                    enemy.grounded = True
                    enemy.y = world_object.y - enemy.height + 2
                if constants.TYPES.OBJECT == world_object.type and constants.collided(enemy, world_object):
                    move = world_object.collide(enemy)
                    enemy.x += move

        for enemy in self.enemies:
            if enemy.dead:
                self.enemies.remove(enemy)

        self.player.grounded = False
        for world_object in self.objects:
            if constants.on_top_of(self.player, world_object):
                if world_object.type != constants.TYPES.FLAG:
                    self.player.y = world_object.y - self.player.height + 2
                    self.player.grounded = True
                    self.player.collide(world_object)
            if constants.collided(self.player, world_object):
                if world_object.type == constants.TYPES.FLAG:
                    self.running = False
                elif world_object.type == constants.TYPES.OBJECT:
                    move = world_object.collide(self.player)
                    self.update_all_with_x(-move)

        if self.player.y > constants.SCREEN_HEIGHT:
            self.running = False

    def update_all_with_x(self, x):
        for enemy in self.enemies:
            enemy.x += x
        for world_object in self.objects:
            world_object.x += x

    def handle_inputs(self, keys):
        update_speed = constants.SCREEN_WIDTH / self.fps / 5
        if keys[pg.K_d]:
            self.update_all_with_x(-update_speed)
        if keys[pg.K_a]:
            self.update_all_with_x(update_speed)
