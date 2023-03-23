import pygame
import random

from dino_runner.components.music import Music
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.thunder_cloud import Thunder_Cloud
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, SMALL_CACTUS_Y_POS, LARGE_CACTUS_Y_POS, BIRD_Y_POS, DEATH_SOUND, THUNDER_CLOUD, THUNDER_CLOUD_Y_POS

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        #pygame.mixer.init()
        self.music = Music()

    def update(self, game):
        if len(self.obstacles) == 0:
            obst = random.randint(1,4)
            if obst == 1:
                obstacle = (Cactus(SMALL_CACTUS, SMALL_CACTUS_Y_POS))
                #obstacle.set_y_pos(SMALL_CACTUS_Y_POS)
            elif obst == 2:
                obstacle = Cactus(LARGE_CACTUS, LARGE_CACTUS_Y_POS)
            elif obst == 3:
                obstacle = Thunder_Cloud(THUNDER_CLOUD, THUNDER_CLOUD_Y_POS)
                #obstacle.set_y_pos(LARGE_CACTUS_Y_POS)
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
                        if game.player.has_hammer == True:
                            if isinstance(obstacle, Cactus):
                                self.obstacles.remove(obstacle)
                            else:
                                pygame.time.delay(500)
                                game.playing = False
                                game.death_count += 1
                                DEATH_SOUND.play()
                                self.music.play_death_music()
                                break
                        
                        elif game.player.has_sword == True:
                            if isinstance(obstacle, Bird):
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


