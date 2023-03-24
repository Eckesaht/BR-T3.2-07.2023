import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.spin import Spin

from dino_runner.utils.constants import SPIN_TYPE

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(250, 300)
        self.choice = [Spin(), Shield()]
        

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and score == self.when_appears:
            self.power_ups.append(random.choice(self.choice))
            self.when_appears += random.randint(300, 350)
            
    def update(self, game):
        self.generate_power_up(game.score)
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            
            player = game.player
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.has_power_up = True
                player.type = power_up.type
                if power_up.type == SPIN_TYPE:
                    player.has_Spin = True
                else:
                    player.has_shield = True
                player.power_up_time_up = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)
                
    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
    def reset_power_ups(self):
        self.power_ups.clear()

            
    
    