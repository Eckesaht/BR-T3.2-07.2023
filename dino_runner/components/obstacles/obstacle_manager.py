import pygame, random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        self.choice = random.randint(0, 2)
        if self.choice == 0 and len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
        
        elif self.choice == 1 and len(self.obstacles) == 0:
            self.obstacles.append(Bird(BIRD))
 
        elif self.choice == 2 and len(self.obstacles) == 0:
            self.obstacles.append(Cactus(LARGE_CACTUS))


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break                
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)



