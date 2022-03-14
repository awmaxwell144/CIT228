"""self.unscaled_image = pygame.image.load('Game_Project/images/raindrop.bmp')
        self.size = width, height = (100, 100)
        self.image = pygame.transform.scale(self.unscaled_image, self.size)"""
import pygame
from random import randint
from pygame.sprite import Sprite

class Raindrop(Sprite):
    def __init__(self, cr_game):
        super().__init__()
        self.screen = cr_game.screen
        self.settings = cr_game.settings

        self.unscaled_image = pygame.image.load('Game_Project/images/raindrop.bmp')
        self.imageSize = width, height = (100, 100) #only for the next line
        self.image = pygame.transform.scale(self.unscaled_image, self.imageSize)

        
        self.rect = self.image.get_rect()
        
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)

        self.x = randint(50, self.settings.screen_width - 50)
        self.rect.x = self.x

    
    def draw_raindrop(self):
        pygame.draw.rect(self.screen, self.rect)

    def blittme(self): #don't think I need
        self.screen.blit(self.image,self.rect)
        """

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
"""
    def update(self):
        self.y += (self.settings.raindrop_speed)
        self.rect.y = self.y
        