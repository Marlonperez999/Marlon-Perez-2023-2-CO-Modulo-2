import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH
class Obstacule(Sprite):
    def __init__(self,image,obstacule_type):
        # self.image es una lista
        self.image = image
        # self.obstacule_type es un indice
        self.obstacule_type = obstacule_type
        self.rect = self.image[self.obstacule_type].get_rect()
        self.rect.x = SCREEN_WIDTH
    def update(self,game_speed):
        self.rect.x -= game_speed

    def draw(self, screen):
        screen.blit(self.image[self.obstacule_type], (self.rect.x, self.rect.y))
