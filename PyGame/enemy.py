import pygame
import random


pygame.init()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x_position):
        super().__init__()
        self.settings = game.settings
        self.screen = game.screen 
        self.enemy_type = random.randint(0, 1)
        self.image = pygame.image.load(f"Images/enemy{self.enemy_type}.png")
        if self.enemy_type == 0:
            self.dims = 80
            self.rect = pygame.Rect(0, 0, 80, 80)
            self.image = pygame.transform.scale(self.image, (80, 80))
        else:
            self.rect = pygame.Rect(0, 0, 64, 64)
            self.dims = 64

        self.rect.left = self.screen.get_rect().right + x_position + 200
        self.rect.bottom = random.randint(160, self.settings.screen_height)

    def update(self):
        self.rect.left -= self.settings.enemy_speed_x
        if self.settings.hard_mode:
            self.rect.top -= self.settings.enemy_speed_y

            self.settings.enemy_speed_y += 0.00001        

        self.settings.enemy_speed_x += 0.00001
        # self.blit()

    def blit(self):
        self.screen.blit(self.image, self.rect, (self.enemy_type*7*52, 0, self.dims, self.dims))
        