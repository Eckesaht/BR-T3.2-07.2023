import pygame

from dino_runner.utils.constants import BG, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, POINT_SOUND, FONT, FONT_COLOR, HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.music import Music

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = -15
        self.death_count = 0
        self.score = 0
        self.highest_score = 0
        self.max_lives = 3
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.player = Dinosaur()
        self.music = Music()

    def execute(self):
        
        self.executing = True
        self.music.play_menu_music()
        while self.executing:
            if not self.playing:
                self.show_menu()
        
        pygame.display.quit()
        pygame.quit()
    

    def run(self):
        self.playing = True
        self.music.play_playing_music()
        while self.playing:
            self.events()
            self.update()
            self.draw()
    
    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
         
        self.game_speed = 20
        self.score = 0
        self.death_count = 0

    def continue_game(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)       
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        self.update_score()
        
    def update_score(self):
        self.score+=1
        if self.score > self.highest_score:
            self.highest_score = self.score
        if self.score%100 == 0:
            self.game_speed+=5
            POINT_SOUND.play()
        
        
    def draw(self):
        self.clock.tick(FPS)
        self.fill_screen()
        self.draw_background()

        self.player.draw(self.screen)
        self.draw_score()
        self.draw_deaths()
        self.draw_power_up_time()
        
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        
        pygame.display.flip()

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks())/1000, 2)
            
            if time_to_show >=0:
                self.draw_text(f'Power Up: {time_to_show}', 530, 100, FONT_COLOR['RED'])
            else:
                self.player.has_power_up = False
                self.player.has_spin = False
                self.player.has_shield = False
                self.player.type = DEFAULT_TYPE
                
    def draw_score(self):
        self.draw_text(f'Score: {self.score}', 1000, 50, FONT_COLOR['YELLOW'])
        self.draw_text(f'Highest Score: {self.highest_score}', 125, 60, FONT_COLOR['AQUA'])


    def draw_background(self):
        image_width = BG.get_width()
        self.x_pos_bg -= 1
        if self.x_pos_bg <= -image_width:
            self.x_pos_bg = 0
        self.screen.blit(BG, (self.x_pos_bg, 0))
        self.screen.blit(BG, (self.x_pos_bg + image_width, 0))

        
    def fill_screen(self):
        self.screen.fill(FONT_COLOR['WHITE'])
        

    def draw_text(self, message, x, y, color):
        self.text = FONT.render(message, True, color)
        text_rect = self.text.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(self.text, text_rect)

    def show_menu(self):
        self.fill_screen()
        if self.death_count == 0:
            self.draw_text("Press (S) to start playing", HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, FONT_COLOR['BLACK'])

        else:
            self.draw_text("Press (C) to continue playing", HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, FONT_COLOR['BLACK'])

            self.draw_text("Press (R) to restart the game", HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT + 30, FONT_COLOR['BLACK'])

            self.draw_text("Press (X) to check for this run stats", HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT + 60, FONT_COLOR['BLACK'])
        
        pygame.display.update()
        self.handle_events_on_menu()
    
    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_s] and self.death_count == 0:
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_r]:
                    self.player = Dinosaur()
                    self.reset_game()
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_c]:
                    self.continue_game()
                    self.run()
        
    def draw_deaths(self):
        self.draw_text(f'Deaths: {self.death_count}', 1000, 80, FONT_COLOR['GREEN'])


            
