import sys
import pygame
import time
from random import randint
from settings import Settings
from raindrop import Raindrop
from bucket import Bucket
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

class CatchingRaindrops:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Catiching Raindrops")
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.bucket = Bucket(self)
        self.raindrops = pygame.sprite.Group() 
        self.initial_time = int(time.time())
        self.play_button = Button(self, "Play")

    def run_game(self):
        while True:
            self.check_events()
            if self.stats.game_active:
                self.bucket.update()
                self.update_raindrops()
            self.update_screen()

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.bucket.blittme()
        for drop in self.raindrops.sprites():
            drop.blittme()
        self.sb.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

    def update_raindrops(self):
        self.raindrops.update()
        counter = int(time.time() - self.initial_time)
        if counter > self.settings.time_between_rows:
            self.new_raindrops()
            self.initial_time = int(time.time())
        self.check_raindrop_bottom()

    def new_raindrops(self):
        for i in range(self.settings.drops_per_row):
            new_drop = Raindrop(self)
            self.raindrops.add(new_drop)
    
    def check_events(self):
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                   self.check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                   self.check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.check_play_button(mouse_pos)

    def check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.bucket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.bucket.moving_left = False

    def check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.bucket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.bucket.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
    

    def check_raindrop_bottom(self):
        screen_rect = self.screen.get_rect()
        for raindrop in self.raindrops.sprites():
            if raindrop.rect.bottom >= screen_rect.bottom:
                collisions = pygame.sprite.spritecollideany(self.bucket, self.raindrops)
                if collisions:
                    self.stats.score += self.settings.raindrop_points
                    self.sb.prep_score()
                else:
                    self.raindrop_missed()
                self.raindrops.remove(raindrop)

    def raindrop_missed(self):
        if self.stats.drops_left > 0:
            self.stats.drops_left -= 1
            self.sb.prep_drops()
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked:
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_drops()

            self.raindrops.empty()

            self.bucket.center_bucket()

            pygame.mouse.set_visible(False)
            
if __name__ == '__main__':
    cr = CatchingRaindrops()
    cr.run_game()