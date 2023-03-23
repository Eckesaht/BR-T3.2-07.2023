from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import  SCREEN_WIDTH
import random

class Thunder_Cloud(Obstacle):
    def __init__(self,image, y):
        super().__init__(image, 0)
        #self.cloud = self.image[0]
        self.rect.y = y
        self.rect.x = SCREEN_WIDTH
        self.stop_range = random.randint(50, 350)

        if self.rect.x >= self.stop_range:
            self.moving = True
        else:
            self.moving = False

    
    def update(self,game_speed, obstacles):

        if self.moving:
            self.rect.x -= game_speed - 10
        else:
            self.rect.x = self.stop_range
    
        super().update(game_speed, obstacles)
