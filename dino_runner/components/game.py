import pygame
import random

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_SIZE, FONT_TYPE, POINT_SOUND, CLOUD

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager


class Game:
    def __init__(self):
        pygame.init()
        self.cloud_img = CLOUD
        self.cloud_list = []
        pygame.mixer.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.half_width = SCREEN_WIDTH // 2
        self.half_height = SCREEN_HEIGHT // 2
        self.FONT = pygame.font.SysFont(FONT_TYPE, FONT_SIZE)
        self.score = 0
        self.pr = 0
        self.dodged_obstacles = [0, 0, 0]
        self.deaths = 0

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()

    def run(self):
        # Game loop: events - update - draw
        #self.playing = True
       
        while self.playing == False:
            self.show_menu()
            self.events()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.show_menu()
        self.deaths += 1
        
    def events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    pygame.QUIT()
                elif event.type == pygame.KEYDOWN and self.playing == False:
                    if event.key == pygame.K_c:
                        self.obstacle_manager.remove_obstacles()
                        self.playing = True
                        self.run()
                        break
                    elif event.key == pygame.K_r and self.playing == False:
                        self.obstacle_manager.remove_obstacles()
                        self.game_speed = 20
                        self.score = 0
                        self.playing = True
                        self.deaths = 0
                        self.run()
                        break
                    elif event.key == pygame.K_s and self.deaths == 0:
                        self.playing = True
                        self.run()

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.score += 1
        if self.score % 100 == 0:
            POINT_SOUND.play()
            self.game_speed += 5
        if self.score > self.pr:
            self.pr = self.score

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()

        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()

        pygame.display.update()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
        if len(self.cloud_list) < 5:
            cloud_x = SCREEN_WIDTH + random.randint(0, SCREEN_WIDTH)
            cloud_y = random.randint(0, SCREEN_HEIGHT // 2)
            cloud_vel = random.randint(1, 3)
            self.cloud_list.append((cloud_x, cloud_y, cloud_vel))


    def draw_score(self):
        show_score = self.FONT.render((f'Score: {self.score}'), True, (0, 0, 0))
        self.screen.blit(show_score, (SCREEN_WIDTH - 150, (SCREEN_HEIGHT + 10) - SCREEN_HEIGHT))

        show_score = self.FONT.render((f'Personal record: {self.pr}'), True, (0, 0, 0))
        self.screen.blit(show_score, (SCREEN_WIDTH - 1100, (SCREEN_HEIGHT + 10) - SCREEN_HEIGHT))

    def game_over(self):
        game_over_font = self.FONT.render("GAME OVER", True, (0, 0, 0))
        self.screen.blit(game_over_font, (self.half_width - game_over_font.get_width() / 2, self.half_height - game_over_font.get_height() - 50))
        pygame.display.update()

    def show_menu(self):
        
        if self.deaths == 0:
            start_font = self.FONT.render('Press (S) to start playing', True, (0, 0, 0))
            self.screen.fill((255, 255, 255))
            self.screen.blit(start_font, (self.half_width - start_font.get_width() + 150, self.half_height - start_font.get_height()))
            pygame.display.update()
            
        else:
            continue_font = self.FONT.render('Press (C) to continue playing', True, (0, 0, 0))
            reset_font = self.FONT.render('Press (R) to reset game progress', True, (0, 0, 0))
            self.screen.fill((255, 255, 255))
            self.screen.blit(continue_font, (self.half_width - continue_font.get_width() + 180, self.half_height - continue_font.get_height()))
            self.screen.blit(reset_font, (self.half_width - reset_font.get_width() + 200, self.half_height - reset_font.get_height() + 30))
            self.show_deaths()
            self.game_over()
            pygame.display.update()

    
    def show_deaths(self):
        show_deaths = self.FONT.render((f'Deaths: {self.deaths}'), True, (0, 0, 0))
        self.screen.blit(show_deaths, (SCREEN_WIDTH - 150, (SCREEN_HEIGHT + 10) - SCREEN_HEIGHT))

