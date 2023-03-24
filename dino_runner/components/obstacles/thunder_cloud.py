from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.thunder import Thunder
from dino_runner.utils.constants import SCREEN_WIDTH, THUNDER, THUNDER_POS_X, THUNDER_POS_Y
import random

class Thunder_Cloud(Obstacle):
    def __init__(self,image, y):
        super().__init__(image, 0)
        self.moving = True
        self.rect.y = y
        self.rect.x = SCREEN_WIDTH
        self.stop_range = random.randint(THUNDER_POS_X, THUNDER_POS_Y)

    def update(self, game_speed, obstacles):
        if self.rect.x > self.stop_range:
            self.moving = True
        else:
            self.moving = False

        if self.moving:
            self.rect.x -= game_speed - 5
        else:
            self.rect.x = self.stop_range
            
            if len(obstacles) == 1:
                obstacles.append(Thunder(THUNDER, self.stop_range + 15, self.rect.y + 15))
            else:
                obstacles.clear()
                


       





        
    
    
        
