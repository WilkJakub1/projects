import pygame


class Fireball:
    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen
        self.image = pygame.image.load("Images/fireball_sheet.png")
        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image, (384, 48))
        self.image_rect = pygame.Rect(-100, 100, 48, 48)

        self.fired = False
        self.collide = False

        self.iteration = 0

    def update(self):
        if self.fired and not self.collide:
            self.image_rect.right += self.settings.fireball_speed
            # if self.image_rect.right < self.settings.screen_width:
            #     self.fired = True
            # else:
            #     self.fired = False
            #     self.image_rect.x = -100

        self.iteration += 1
        if not self.collide:
            if self.iteration > 12:
                self.iteration = 0
        else:
            if self.iteration > 18:
                self.iteration = 0
                self.image_rect.right = -100
                self.collide = False
                self.fired = False



    def blit(self, img_num):
        self.screen.blit(self.image, self.image_rect, (48*img_num, 0, 48, 48))

    def fire(self, game):
        self.image_rect.top = game.dragon.image_rect.top + 30
        self.image_rect.right = game.dragon.image_rect.right + 5
        self.fired = True

    def check_collision(self, object):
        if self.image_rect.right >= self.settings.screen_width and not self.collide:
            self.collide = True
            self.iteration = 12

        elif pygame.Rect.colliderect(self.image_rect, object):
            self.collide = True
            self.iteration = 12
            self.settings.points += 1000

            return True
