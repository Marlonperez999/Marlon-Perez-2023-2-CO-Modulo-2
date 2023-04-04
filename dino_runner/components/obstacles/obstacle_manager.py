import pygame
import random
from dino_runner.components import obstacles
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD



class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            luck = random.randint(0, 2)
            if luck == 0:
                obstacle = Cactus(SMALL_CACTUS)
            elif luck == 1:
                obstacle = Cactus(LARGE_CACTUS)
            else:
                obstacle = Bird(BIRD)

            self.obstacles.append(obstacle)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

