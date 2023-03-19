import random

from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self,images):
        super().__init__(images, random.randint(0,1))
        self.images = images
        self.flying_index = 0

    
    def update(self,game_speed, obstacles):
        #changing the images
        self.image = self.images[self.flying_index //5] 
        
        self.flying_index += 1
        
        if self.flying_index >=10:
            self.flying_index = 0
        
        super().update(game_speed, obstacles)
    
        