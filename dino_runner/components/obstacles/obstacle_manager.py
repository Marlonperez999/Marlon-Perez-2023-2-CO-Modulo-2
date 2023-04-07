import random
import pygame
from dino_runner.components import obstacles
from dino_runner.components.dinosaur import Dinosour
from dino_runner.components.obstacles.bird import Bird

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SHIELD_TYPE
from dino_runner.components.power_ups.hammer_up import HammerUp
from dino_runner.utils.constants import SMALL_CACTUS, SHIELD_TYPE, DEFAULT_TYPE, HAMMER_TYPE

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.hammer_quantity = []
        self.hammer = False
        self.havehammer = False        

    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle = self.generate_obstacle(random.randint(0, 2))
            self.obstacles.append(obstacle)

        if game.player.type == HAMMER_TYPE:
            self.havehammer = True
        else:
            self.havehammer = False

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.type != SHIELD_TYPE:
                    game.playing = False
                    game.death_count.update()
                    break
                else:
                    self.obstacles.remove(obstacle)
        
        for throw in self.hammer_quantity:
            throw.update(game.game_speed, self.hammer_quantity)
            if throw.rect.colliderect(obstacle.rect):
                if len(self.obstacles) > 0:
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        if len(self.hammer_quantity) > 0:
            for throw in self.hammer_quantity:
                throw.draw(screen)

    def generate_obstacle(self, obstacle_type):
        if obstacle_type == 0:
            cactus_type = 'SMALL'
            obstacle = Cactus(cactus_type)
        elif obstacle_type == 1:
            cactus_type = 'LARGE'
            obstacle = Cactus(cactus_type)
        else:
            obstacle = Bird()
        return obstacle

    def reset_obstacles(self):
        self.obstacles = []
        self.hammer_quantity  = []
        self.hammer = False
        self.havehammer = False

    def throw_hammer(self, user_input):
        if user_input[pygame.K_SPACE] and self.havehammer:
            power_up = HammerUp()
            self.hammer_quantity.append(power_up)
            self.havehammer = True
            