import sys  
import pygame  
from ex1 import Setting
from ship import Ship

class AlienInvasion:
    def __init__(self):  
        pygame.init()  
        self.setting = Setting()
        self.screen = pygame.display.set_mode((self.setting.width, self.setting.height))
        pygame.display.set_caption(self.setting.caption)  
        self.bg_color = (self.setting.bg_color)
        self.ship = Ship(self)  # Create an instance of Ship

    def run_game(self): 
        while True: 
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:  
                    sys.exit()  
            self.screen.fill(self.setting.bg_color)  
            self.ship.blitme()  # Draw the ship on the screen
            pygame.display.flip()  

if __name__ == "__main__":
    ai = AlienInvasion() 
    ai.run_game()


