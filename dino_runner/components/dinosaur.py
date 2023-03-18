import pygame

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5




class Dinosaur:
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS

        self.step_index = 0
        self.jump_vel = JUMP_VEL

        # 0: Correndo
        # 1: No ar
        # 2: Agachado
        # 3: Descendo
        self.dino_status = 0

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1] #ternary operator 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index+=1        
        
        if self.step_index >= 10:
            self.step_index = 0
    

    def dive(self):
        self.jump_vel = JUMP_VEL

        if self.dino_status == 3:
            self.dino_rect.y += self.jump_vel*5
            self.jump_vel += 1

        if self.dino_rect.y > Y_POS:
            self.dino_status = 0
            self.dino_rect.y = Y_POS
            self.jump_vel = JUMP_VEL

    def jump(self):
        self.image = JUMPING
        
        if self.dino_status == 1: 
            self.dino_rect.y -= self.jump_vel*4
            self.jump_vel -= 0.8

        if self.dino_rect.y > Y_POS:
            self.dino_status = 0
            self.dino_rect.y = Y_POS
            self.jump_vel = JUMP_VEL
    
    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS + 30
        self.step_index+=1

        if self.step_index >= 10:
            self.step_index = 0
    
    def update(self, user_input):
        if user_input[pygame.K_UP] and self.dino_status != 3:
            self.dino_status = 1
        elif user_input[pygame.K_DOWN] and self.dino_status == 0:
            self.dino_status = 2
        elif user_input[pygame.K_DOWN] and self.dino_status == 1 and not user_input[pygame.K_UP]:
            self.dino_status = 3

        if self.dino_status == 0:
            self.run()
        elif self.dino_status == 1:
            self.jump()                
        elif self.dino_status == 2:
            if user_input[pygame.K_DOWN]:
                self.duck()
            else:
                self.run()
        elif self.dino_status == 3:
            self.dive()
    
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x,self.dino_rect.y))
    