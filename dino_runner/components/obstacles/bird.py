from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, images):
        self.type = 0
        self.counter = 0
        super().__init__(images, self.type)
        self.list = [images[self.type], images[self.type + 1]]
        self.rect.y = 260

    def update(self, game_speed, obstacles):
        super().update(game_speed, obstacles)
        self.image = self.list[self.type]
        if self.counter <= 8:
            self.type = 0
            self.counter += 1
        elif self.counter < 16: 
            self.type = 1
            self.counter += 1
            if self.counter == 15:
                self.counter = 0


