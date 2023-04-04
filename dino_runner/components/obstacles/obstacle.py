import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(Sprite):
    def __init__(self, image, obstacle_type, name_obstacle=''):
        #self.image es una lista
        self.image = image
        #self.obstacle_type es un undice
        self.obstacle_type = obstacle_type
        self.rect = self.image[obstacle_type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.name_obstacle = name_obstacle
        self.index = 0

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        if self.name_obstacle == 'cactus':
            screen.blit(self.image[self.obstacle_type], (self.rect.x, self.rect.y))
        elif self.name_obstacle == 'bird':
            if self.index >= 9:
                self.index = 0
            screen.blit(self.image[self.index//5], self.rect)
            self.index += 1
