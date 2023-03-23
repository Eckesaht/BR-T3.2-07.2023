from dino_runner.utils.constants import MUSIC_MENU, MUSIC_DEATH_MENU, MUSIC_PLAYING
import pygame
import random

class Music:
    def __init__(self):
        pygame.mixer.init()
        self.mixer = pygame.mixer.music
    def play_menu_music(self):
        self.mixer.load(MUSIC_MENU[self.randomizer(0, 3)])
        self.mixer.play()

    def play_death_music(self):
        self.mixer.load(MUSIC_DEATH_MENU[self.randomizer(0, 2)])
        self.mixer.play()

    def play_playing_music(self):
        self.mixer.load(MUSIC_PLAYING[self.randomizer(0, 3)])
        self.mixer.play()

    def randomizer(self, min, max):
        return random.randint(min, max)