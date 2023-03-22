import random

from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self,images):
        super().__init__(images, random.randint(0,1))
        self.images = images
        self.flying_index = 0
        
        self.touched_ground = False
        #this will decide if the bird would be in zig-zig or not
        self.moving = random.randint(1,2) % 2 == 0 and True or False

    
    def update(self,game_speed, obstacles):
        #changing the images
        self.image = self.images[self.flying_index //5] 
        
        self.flying_index += 1
                
        if self.moving:
            if not self.touched_ground:
                self.rect.y +=10
                if self.rect.y > 350:
                    self.touched_ground = True
            else:
                self.rect.y -=10
                if self.rect.y < 200:
                    self.touched_ground = False
        
        if self.flying_index >=10:
            self.flying_index = 0
        
        super().update(game_speed, obstacles)
    
        