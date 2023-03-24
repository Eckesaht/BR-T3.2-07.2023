from dino_runner.components.obstacles.obstacle import Obstacle

class Thunder(Obstacle):
    def __init__(self, image, x, y):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.x = x
        self.rect.y = y
        

             


        
    
    
        
