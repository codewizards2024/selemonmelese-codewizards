import pygame.font
class ScoreBoard:
    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.setting=ai_game.setting
        self.states=ai_game.states
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)
        self.prep_score()  # Corrected line
        self.prep_high_score()
        self.prep_level()
    def prep_level(self):
        game_rank=str(self.states.level)    
        self.game_level=self.font.render(game_rank,True,self.text_color,self.setting.bg_color)
        self.level_rect=self.game_level.get_rect()
        self.level_rect.right=self.score_rect.right
        self.level_rect.top=self.score_rect.bottom +10
    def prep_high_score(self):
        rounded_score=round(self.states.high_score,-1)   
        score_str="{:,}".format(rounded_score) 
        self.high_score_image=self.font.render(score_str,True,self.text_color,self.setting.bg_color)
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.screen_rect.top
    def  prep_score(self):
        rounded_score=round(self.states.score,-1)
        score_str="{:,}".format(rounded_score)
        self.score_image=self.font.render(score_str,True,self.text_color,self.setting.bg_color) 
        self.score_rect=self.score_image.get_rect() 
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.game_level,self.level_rect)
    def check_high_score(self):
        if self.states.score>self.states.high_score:
            self.states.high_score=self.states.score    
            self.prep_high_score()


