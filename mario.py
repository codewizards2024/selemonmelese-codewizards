import pygame
from setting import Setting
class Mario:
    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.setting=Setting()
        self.image=pygame.image.load("c:/users/hp/pictures/mario.bmp")
        self.rect=self.image.get_rect()
        self.bg_color=(self.setting.bg_color)
        self.rect.center=self.screen_rect.center
    def blitme(self):
        self.screen.blit(self.image,self.rect)
            