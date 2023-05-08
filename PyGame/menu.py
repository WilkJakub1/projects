import pygame


pygame.init()

class Menu:
    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen_rect

        self.font = pygame.font.SysFont(self.settings.font, self.settings.font_size)
        self.counter = 0
        self.counter_set = 3

    def draw_text(self, text, text_color, x, y):
        img = self.font.render(text, True, text_color)
        self.screen.blit(img, (x, y))

    def update(self):
        if self.counter == 0:
            self.draw_text("Resume", (100, 255, 255), 150, 150)
        else:
            self.draw_text("Resume", (255, 255, 255), 150, 150)
        if self.counter == 1:
            self.draw_text("Settings", (100, 255, 255), 150, 200)
        else:
            self.draw_text("Settings", (255, 255, 255), 150, 200)
        if self.counter == 2:
            self.draw_text("Quit", (100, 255, 255), 150, 250)
        else:
            self.draw_text("Quit", (255, 255, 255), 150, 250)
    
    
    def action(self, game):
        if self.counter == 0:
            game.pauza = False
        elif self.counter == 1:
            game.opcje = True
        elif self.counter == 2:
            game.exit_game()

    def opcje(self):
        self.draw_text("Opcja skina:", (255, 255, 255), 150, 100)
        x = 150
        y=150
        for number in range(0,4):
            if number == self.counter_set:
                color = (100, 255, 255)
            else:
                color = (255, 255, 255)
            self.draw_text(f"{number}", color, 150, y)
            y += 50
       
       