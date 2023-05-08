import pygame


class HighestScore:
    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen

        self.font = pygame.font.SysFont(self.settings.font, self.settings.font_size)
        self.text = self.font.render("New high score!!!", True, (0,0,0))

    def blit(self):
        self.screen.blit(self.text, (300, 400))