import sys
import pygame
from time import sleep
from setting import Setting
from ship import Ship
from scoreboard import ScoreBoard
from button import Button
from bullet import Bullet
from alien import Alien
from game_states import GameState

class AlienInvasion:
    count = 0
    def __init__(self):
        pygame.init()
        self.setting = Setting()
        self.states = GameState(self)  # Ensure this is instantiated before accessing it

        if self.setting.fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.setting.width = self.screen.get_rect().width
            self.setting.height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption(self.setting.caption)
        self.bg_color = self.setting.bg_color
        self.ship = Ship(self)
        self.sb = ScoreBoard(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self, "play")

    def run_game(self):
        while self.count <= self.setting.bullets_allowed: 
            self._check_events()
            if self.states.active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT: 
                sys.exit()   
            elif event.type==pygame.KEYDOWN:
               self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)    
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pose=pygame.mouse.get_pos()
                self._check_play_button(mouse_pose)
    def _check_play_button(self,mouse_pose):
        button_click=self.play_button.rect.collidepoint(mouse_pose)
        if button_click and not self.states.active:
            self.setting._intialize_dynamic_setting()
            self.states.reset_states()
            self.states.active=True   
            self.sb.prep_score()
            self.sb.prep_level()
            self.aliens.empty() 
            self.bullets.empty()
            self._create_fleet()
            self.ship.center()
            pygame.mouse.set_visible(False)
    def _check_keydown_events(self,event):
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=True
        elif event.key==pygame.K_q:
            sys.exit()    
        elif event.key==pygame.K_r:
            self._reset_game()
        elif event.key==pygame.K_SPACE:
                self._fire_bullet()    
    def _check_keyup_events(self,event):
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=False    

            
    # def _fire_bullet(self):
    #     if len(self.bullets) < self.setting.bullets_allowed:
    #         new_bullet = Bullet(self)
    #         self.bullets.add(new_bullet)   
    def _relod_game(self):
        self.count=0
        self.bullets.empty()
        self.aliens.empty()
        self._create_fleet()
        self.ship.center()

    def _fire_bullet(self):
       
        if len(self.bullets) < self.setting.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)  
            self.count = self.count + 1
        if self.count>self.setting.bullets_allowed:
            print("the game is over press r to restart again!!")    
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)    
        self._check_bullet_alien_collision()
 
    def _check_bullet_alien_collision(self):
        collision=pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)  
        if collision:
            for alien in collision.values():
                self.states.score+=self.setting.alien_point*len(alien)
            self.sb.prep_score()  
            self.sb.check_high_score()
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.setting.increese_speed()
            self.states.level+=1
            self.sb.prep_level()
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        # Check for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()    

    def _ship_hit(self):
        # Handle the ship being hit by an alien
        if self.states.ships_left>0:                 
          self.states.ships_left-=1
        # get rid of any remaining aliens and bulletes
          self.aliens.empty()
          self.bullets.empty()
          self._create_fleet()
          self.ship.center()
          sleep(0.5)
        else:
            print("You have lost")  # Print the message
            self.states.active=False  
            pygame.mouse.set_visible(True)
              # Quit the game after three hits
    def _check_aliens_bottom(self):
        self.screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen_rect.bottom:
                self._ship_hit()
                break
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1
                    
    def _create_fleet(self):
        alien = Alien(self)
        
        alien_width, alien_height = alien.rect.size
        available_space_x = self.setting.width - 2 * alien_width
        number_aliens_x = available_space_x // (2 * alien_width)
        ship_height = self.ship.rect.height
        available_space_y = self.setting.height - 3 * alien_height - ship_height
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)
    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)    
        self.sb.show_score()   
        if not self.states.active:
            self.play_button.draw_button()       
        pygame.display.flip()                

if __name__=="__main__":
    ai =AlienInvasion()
    ai.run_game()


