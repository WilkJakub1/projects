import pygame


class Heart:
    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("Images/heart.png")
        self.rect = self.image.get_rect()
        self.rect.top = 50
        self.rect.right = self.screen_rect.right 

    def blit(self):
        for i in range(self.settings.hearts_left):
            self.screen.blit(self.image, (self.screen_rect.right - 50 *(i+1), 10))