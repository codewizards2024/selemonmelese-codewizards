import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.image = pygame.image.load("C:/users/hp/pictures/alien.bmp")
        self.image = pygame.transform.scale(self.image, (50, 50))  # Resize the image
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def check_edges(self):
        self.screen_rect = self.screen.get_rect()
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.setting.alien_speed * self.setting.fleet_direction)
        self.rect.x = self.x


