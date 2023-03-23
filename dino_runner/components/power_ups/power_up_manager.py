import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
#from dino_runner.components.power_ups.sword import Sword
from dino_runner.utils.constants import HAMMER_TYPE #SWORD_TYPE

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.choice = [Shield(), Hammer()]

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200,300)
            self.power_ups.append(random.choice(self.choice))
            
    def update(self, game):
        self.generate_power_up(game.score)
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            
            player = game.player
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()#
                #player.shield = True
                player.has_power_up = True
                player.type = power_up.type
                if power_up.type == HAMMER_TYPE:
                    player.has_hammer = True
                #elif power_up.type == SWORD_TYPE:
                    #player.has_sword = True
                else:
                    player.has_shield = True
                player.power_up_time_up = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)
    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
    def reset_power_ups(self):
        self.power_ups.clear()
        self.when_appears = random.randint(200,300)
            
    
    