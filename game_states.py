class GameState:
    def __init__(self,ai_game):
        self.setting=ai_game.setting
        self.reset_states()
        self.active=False
        self.high_score=0
    def reset_states(self):
        self.ships_left=self.setting.ship_limit      
        self.score=0 
        self.level=1