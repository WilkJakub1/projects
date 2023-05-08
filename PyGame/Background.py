import pygame

pygame.init()

class Background:
    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen
        self.bg1 = pygame.image.load("Images/sky(1).png")
        self.bg1_rect = self.bg1.get_rect()
        self.bg2_rect = self.bg1.get_rect()
        self.bg2_rect.left = 1024
        self.bg1_rect.bottom = self.settings.screen_height
        self.bg2_rect.bottom = self.settings.screen_height
    
    def update(self):
        self.bg1_rect.left -= self.settings.bg_speed
        self.bg2_rect.left -= self.settings.bg_speed
        if self.bg1_rect.right < 0:
            self.bg1_rect.left = self.bg2_rect.right
        elif self.bg2_rect.right < 0:
            self.bg2_rect.left = self.bg1_rect.right


    def blit(self):     
        self.screen.blit(self.bg1, self.bg1_rect)
        self.screen.blit(self.bg1, self.bg2_rect)