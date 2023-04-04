import random
from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,1)
        random_height = random.randint(220,305)
        super().__init__(image,self.type,'bird')
        self.rect.y = random_height
