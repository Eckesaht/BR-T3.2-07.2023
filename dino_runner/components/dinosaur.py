import pygame

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE,SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, DUCKING_HAMMER, JUMPING_HAMMER, RUNNING_HAMMER, HAMMER_TYPE, JUMPING_SOUND, SCREEN_WIDTH #SWORD_TYPE, DUCKING_SWORD, RUNNING_SWORD, JUMPING_SWORD,

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE:DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE:JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE:RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}

X_POS = 80
Y_POS = 520
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
        self.has_hammer = False
        self.has_sword = False
        self.has_shield = False

    def run(self):
        self.image = RUN_IMG[self.type][self.run_index]
        self.counter_run += 1
        self.dino_rect.y = Y_POS
        if self.counter_run >= 5:
            self.run_index+=1
            self.counter_run = 0 
            if self.run_index >= 8:
                self.run_index = 0
            

    def jump(self):
        self.image = JUMP_IMG[self.type][self.jump_index]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel*4
            self.jump_vel -= 0.8
            self.counter_jump += 1
            if self.counter_jump % 2 == 0 and self.jump_index < 10:
                self.jump_index += 1
                self.counter_jump = 0

        if self.jump_vel < -JUMP_VEL:
            self.dino_jump = False
            self.dino_rect.y = Y_POS
            self.jump_vel = JUMP_VEL
            self.counter_jump += 1

        
        if self.jump_index == 10:
            self.jump_index = 0
            
    
    def duck(self):
        self.image = DUCK_IMG[self.type][0] 
        
        self.dino_rect.y = Y_POS_DUCK
        self.step_index+=1        
        
        self.dino_duck = False        
    

    # Resolver bug - atravessando as bordas do jogo

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
        
        # user_input[pygame.K_DOWN] and self.dino_jump:
            #self.jump_vel += self.jump_vel*5

        if user_input[pygame.K_RIGHT]:
            if self.dino_rect.x < SCREEN_WIDTH - 90:
                self.dino_rect.x +=10
            else:
                self.dino_rect.x -= 10
            
        elif user_input[pygame.K_LEFT]:
            
            if self.dino_rect.x <=  0:
                self.dino_rect.x += 10
            else:
                self.dino_rect.x -= 10
            
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
    