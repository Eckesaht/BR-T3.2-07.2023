import pygame, random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cloud import Cloud
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, DEATH_SOUND, CLOUD


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.clouds = []
        pygame.mixer.init()

    def update(self, game):
        self.choice = random.randint(0, 2)
        if self.choice == 0 and len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
        
        elif self.choice == 1 and len(self.obstacles) == 0:
            self.obstacles.append(Bird(BIRD))
 
        elif self.choice == 2 and len(self.obstacles) == 0:
            self.obstacles.append(Cactus(LARGE_CACTUS))


        if len(self.clouds) == 0:
            for x in range(random.randint(5, 10)):
                self.clouds.append(Cloud(CLOUD))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                DEATH_SOUND.play()
                pygame.time.delay(500)
                game.playing = False
                break
        
        for cloud in self.clouds:
            cloud.update(game.game_speed, self.clouds)
        
        
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

        for cloud in self.clouds:
            cloud.draw(screen)
    def remove_obstacles(self):
        self.obstacles.clear()


