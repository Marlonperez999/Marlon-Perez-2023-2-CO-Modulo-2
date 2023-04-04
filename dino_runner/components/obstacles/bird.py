import random
from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,1)        
        super().__init__(image,self.type,'bird')
        self.rect.y = 0
        self.bird_height()

    def bird_height(self):
        random_height = random.randint(0,2)
        if random_height == 0:
            self.rect.y = 305
        elif random_height == 1:
            self.rect.y = 240
        else:
            self.rect.y=220