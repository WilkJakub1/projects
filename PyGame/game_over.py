import pygame


class GameOver:
    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.font = pygame.font.SysFont(self.settings.font, self.settings.font_size)
        self.text = self.font.render("Game Over", True, (0,0,0))

    def blit(self):
        self.screen.blit(self.text, (325, 220))