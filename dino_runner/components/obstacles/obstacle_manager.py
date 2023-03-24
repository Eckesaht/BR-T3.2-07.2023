import pygame
import random

from dino_runner.components.music import Music
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.thunder_cloud import Thunder_Cloud
from dino_runner.components.obstacles.lava import Lava
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, SMALL_CACTUS_Y_POS, LARGE_CACTUS_Y_POS, BIRD_Y_POS, DEATH_SOUND, THUNDER_CLOUD, THUNDER_CLOUD_Y_POS, LAVA, LAVA_Y_POS
class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.music = Music()

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obst = random.randint(1,5)
            if self.obst == 1:
                obstacle = Cactus(SMALL_CACTUS, SMALL_CACTUS_Y_POS)
            elif self.obst == 2:
                obstacle = Cactus(LARGE_CACTUS, LARGE_CACTUS_Y_POS)
            elif self.obst == 3:
                obstacle = Thunder_Cloud(THUNDER_CLOUD, THUNDER_CLOUD_Y_POS)
            elif self.obst == 4:
                obstacle = Lava(LAVA, LAVA_Y_POS)
            else:
                obstacle = Bird(BIRD, BIRD_Y_POS)
            
            self.obstacles.append(obstacle)
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    DEATH_SOUND.play()
                    self.music.play_death_music()
                    break

                else:
                    if game.player.has_power_up:
                        if game.player.has_spin == True:
                            if self.obst == 1 or self.obst == 2:
                                self.obstacles.remove(obstacle)
                            else:
                                pygame.time.delay(500)
                                game.playing = False
                                game.death_count += 1
                                DEATH_SOUND.play()
                                self.music.play_death_music()
                                break
                        
                        else:
                            self.obstacles.remove(obstacle)
                    
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            
    def reset_obstacles(self):
        self.obstacles.clear()


