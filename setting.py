import pygame
class Setting:
    def __init__(self):
        # settings to intialize the game
        # screen setting 
        self.fullscreen=True
        self.bg_color=(230,230,230)
        self.caption="Alien Invasion"
        self.fleet_drop_speed=10
        self.ship_limit=3
        self.bullet_width=6
        self.bullet_height=15
        self.bullet_color=(60,0,0)
        self.bullets_allowed=50
        self.speedup_scale=1.1
        self.score_scale=1.5
        self.alien_point=50
        self._intialize_dynamic_setting()
    def _intialize_dynamic_setting(self):
        self.bullet_speed=2
        self.alien_speed=0.5
        self.fleet_direction=1 
        self.ship_speed=1
    def increese_speed(self):
        self.bullet_speed*=self.speedup_scale    
        self.alien_speed*=self.speedup_scale
        self.ship_speed*=self.speedup_scale
        self.alien_point=(self.alien_point*self.score_scale)
