from dino_runner.components.obstacles.obstacle import Obstacle

class Lava(Obstacle):
    def __init__(self, images, rect_y):
        self.type = 0
        super().__init__(images, self.type)
        
        self.rect.y = rect_y

