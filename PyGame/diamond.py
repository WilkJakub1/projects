import pygame
import random


class Diamond(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.settings = game.settings
        self.screen = game.screen
        self.image = pygame.image.load("Images/diamond.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.top = random.randint(0, self.settings.screen_height - 30)
        self.rect.left = self.settings.screen_width + 500

    def update(self):
        self.rect.left -= self.settings.enemy_speed_x

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def check_collision(self, object):
        if pygame.Rect.colliderect(self.rect, object):
            return True
        else:
            return False
