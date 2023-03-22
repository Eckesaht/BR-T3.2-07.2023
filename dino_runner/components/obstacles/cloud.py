from dino_runner.utils.constants import SCREEN_WIDTH
import random

class Cloud():
    def __init__(self, images):
    
        self.image = images
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 300)
        self.rect.y = random.randint(20, 130)

    def draw(self, screen):
            screen.blit(self.image, (self.rect.x, self.rect.y))
  
    def update(self, game_speed, clouds):
        self.rect.x -= (game_speed - 20)

        if self.rect.x < -self.rect.width:
            clouds.clear()