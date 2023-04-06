import pygame
from dino_runner.utils.constants import HAMMER


class HammerUp():
    X_POS = 137
    Y_POS = 320

    def __init__(self):
        self.image = HAMMER
        self.hammer = self.image.get_rect()
        self.hammer.x = self.X_POS
        self.hammer.y = self.Y_POS

    def update(self):
        pass

    def draw(self, screen):
        for _ in range(137, 1100):
            screen.blit(self.image, (self.hammer.x, self.hammer.y))
            pygame.display.update()
            self.hammer.x += 0.8
