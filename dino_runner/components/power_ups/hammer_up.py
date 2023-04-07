import pygame
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER


class HammerUp(PowerUp):
    X_POS = 137
    Y_POS = 320

    def __init__(self):
        self.image = HAMMER
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def update(self, game_speed, power_ups):
        self.rect.x += game_speed
        if self.rect.x < self.rect.width:
            power_ups.pop()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
