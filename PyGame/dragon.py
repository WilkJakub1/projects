import pygame


pygame.init()

class Dragon:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.image = pygame.image.load('Images/flying_dragon1.png')
        self.image_rect = pygame.Rect(0, 100, 144, 128)
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        self.clock = pygame.time.Clock()
        self.counter = 0

        self.iteration = 0
    
    def update(self):
        if self.moving_up and self.image_rect.top >= 0:
            self.image_rect.y -= self.settings.y_speed
        if self.moving_down and self.image_rect.bottom <= self.settings.screen_height:
            self.image_rect.y += self.settings.y_speed
        if self.moving_right and self.image_rect.right <= self.settings.screen_width:
            self.image_rect.x += self.settings.x_speed
        if self.moving_left and self.image_rect.left >= 0:
            self.image_rect.x -= self.settings.x_speed
        if self.image_rect.bottom < self.settings.screen_height:
            self.image_rect.bottom += 3

        if self.image_rect.bottom > self.settings.screen_height - 50 and self.counter == 6:
            self.settings.points -= 40
            self.counter = 0
        elif self.image_rect.bottom > self.settings.screen_height - 50:
            self.counter += 1

        self.iteration += 1
        if self.iteration > 35:
            self.iteration = 0

    
    def blit(self, img_num):
        self.screen.blit(self.image, self.image_rect, (144*img_num, 128, 144, 128))

    def change_skin(self):
        for i in range(4):
            if i == self.settings.dragon_skin:
                self.image = pygame.image.load(f"Images/flying_dragon{i+1}.png")

    def check_collision(self, object):
        if pygame.Rect.colliderect(self.image_rect, object):
            self.settings.hearts_left -= 1
            return True
