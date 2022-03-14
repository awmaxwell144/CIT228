import pygame.font
from pygame.sprite import Group
from raindrop import Raindrop

class Scoreboard:
    def __init__(self,cr_game):
        self.cr_game = cr_game
        self.screen = cr_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = cr_game.settings
        self.stats = cr_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_drops()

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.drops.draw(self.screen)

    def prep_drops(self):
        self.drops = Group()
        for drop_number in range(self.stats.drops_left):
            drop = Raindrop(self.cr_game)
            drop.rect.x = 10 + drop_number * drop.rect.width
            drop.rect.y = 10
            self.drops.add(drop)



