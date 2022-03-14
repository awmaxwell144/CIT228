import pygame
from pygame.sprite import Sprite

class Bucket(Sprite):
    def __init__(self, cr_game):
        super().__init__()
        self.screen = cr_game.screen
        self.settings = cr_game.settings
        self.screen_rect = cr_game.screen.get_rect()

        self.unscaled_image = pygame.image.load('Game_Project/images/red_bucket.bmp')
        self.size = width, height = (100, 100)
        self.image = pygame.transform.scale(self.unscaled_image, self.size)
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.bucket_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.bucket_speed
    
    def blittme(self):
        self.screen.blit(self.image, self.rect)

    def center_bucket(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)