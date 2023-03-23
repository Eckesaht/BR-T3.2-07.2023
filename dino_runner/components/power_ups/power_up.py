import random

from dino_runner.utils.constants import SCREEN_WIDTH

class PowerUp:
    def __init__(self, image,type):
        self.image = image
        self.type = type 
        self.rect = self.image.get_rect()
        self.pos_x = 40
        self.pos_y = 50
        self.extra = 20
        self.x = self.pos_x * self.extra
        self.y = self.pos_x * self.extra
        self.rect.x = SCREEN_WIDTH + 50
        self.rect.y = random.randint(320,370)
        

        self.start_time = 0
        self.duration = random.randint(5,10)
        
    def update(self, game_speed, power_ups):
        self.extra += 3
        self.rect.x -=game_speed
    

        if self.rect.x < -self.rect.width:
            power_ups.pop()
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        