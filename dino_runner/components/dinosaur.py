import pygame

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE,SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, DUCKING_SPIN, JUMPING_SPIN, RUNNING_SPIN, SPIN_TYPE, JUMPING_SOUND, SCREEN_WIDTH 

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE:DUCKING_SHIELD, SPIN_TYPE: DUCKING_SPIN}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE:JUMPING_SHIELD, SPIN_TYPE: JUMPING_SPIN}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE:RUNNING_SHIELD, SPIN_TYPE: RUNNING_SPIN}

X_POS = 80
Y_POS = 518
Y_POS_DUCK = 535
JUMP_VEL = 8.5

class Dinosaur:
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        pygame.mixer.init()
        
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.step_index = 0
        self.run_index = 0
        self.jump_vel = JUMP_VEL
        self.jump_index = 0
        self.counter_run = 0
        self.counter_jump = 0
        self.has_power_up = False
        self.has_spin = False
        self.has_sword = False
        self.has_shield = False

    def run(self):
        self.image = RUN_IMG[self.type][self.run_index]
        self.counter_run += 1
        self.dino_rect.y = Y_POS
        if self.counter_run >= 5:
            self.run_index+=1
            self.counter_run = 0 
            if self.run_index == 7:
                self.run_index = 0
            

    def jump(self):
        self.image = JUMP_IMG[self.type][self.jump_index]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel*4
            self.jump_vel -= 0.8
            self.counter_jump += 1
            if self.counter_jump % 2 == 0 and self.jump_index < 7:
                self.jump_index += 1
                self.counter_jump = 0

        if self.jump_vel < -JUMP_VEL:
            self.dino_jump = False
            self.dino_rect.y = Y_POS
            self.jump_vel = JUMP_VEL
            self.counter_jump += 1

        
        if self.jump_index == 6:
            self.jump_index = 0
            
    
    def duck(self):
        self.image = DUCK_IMG[self.type][0] 
        if self.type == DEFAULT_TYPE:
            self.dino_rect.y = Y_POS_DUCK
            self.step_index+=1        
        
        self.dino_duck = False        
    

    def update(self, user_input):
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            JUMPING_SOUND.play()                
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
        elif not self.dino_jump and not self.dino_duck:
            self.dino_run = True

        if user_input[pygame.K_RIGHT]:
            if self.dino_rect.x < SCREEN_WIDTH - 90:
                self.dino_rect.x +=15
            else:
                self.dino_rect.x -= 15
            
        elif user_input[pygame.K_LEFT]:
            
            if self.dino_rect.x <=  0:
                self.dino_rect.x += 15
            else:
                self.dino_rect.x -= 15
            
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
            
        if self.step_index >= 10:
            self.step_index = 0
            
    
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x,self.dino_rect.y))
    