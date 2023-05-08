import pygame
import random
from settings import Settings
from dragon import Dragon
from Background import Background
from fireball import Fireball
from menu import Menu
from enemy import Enemy
from heart import Heart
from game_over import GameOver
from highest_score import HighestScore
from diamond import Diamond

pygame.init()


class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.playing = True

        self.dragon = Dragon(self)
        self.bg = Background(self)
        self.fireball = Fireball(self)
        self.menu = Menu(self)
        self.heart = Heart(self)
        self.game_over = GameOver(self)
        self.high_score = HighestScore(self)

        self.enemies = pygame.sprite.Group()
        self.diamonds = pygame.sprite.Group()

        if self.settings.easy_mode:
            for i in range(self.settings.easy_mode_enemies):
                self.enemy = Enemy(self, i*500)
                self.enemies.add(self.enemy)
        else:
            for i in range(self.settings.hard_mode_enemies):
                self.enemy = Enemy(self, i*500)
                self.enemies.add(self.enemy)
        
        self.font = pygame.font.SysFont(self.settings.font, self.settings.font_size)
        self.font1 = pygame.font.SysFont(self.settings.font, 30)

        self.pauza = False
        self.opcje = False

        self.intro = True
        self.intro_text = self.font.render("Welcome to the game", True, (0,0,0))

        self.outro = False
        self.outro_text = self.font.render("Are you sure you want to exit?", True, (0,0,0))

        self.press_esc = self.font1.render("Press ESC for menu", True, (0,0,0))

        with open('highest_score.txt', 'r') as f:
            self.settings.highest_score = int(f.readlines()[0])



    def run_game(self):
        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                if event.type == pygame.KEYDOWN:
                    self._keydown_action(event)

                if event.type == pygame.KEYUP:
                    self._keyup_action(event)

            if self.intro:
                self.screen.fill((0,0,0))
                self.bg.blit()
                self.screen.blit(self.intro_text, (250, 250))
                pygame.display.flip()
                continue

            if self.outro:
                self.screen.fill((0,0,0))
                self.bg.blit()
                self.screen.blit(self.outro_text, (200, 250))
                pygame.display.flip()
                continue
            
            self.screen.fill((0,0,0))
            self.points = self.font.render(f"{self.settings.points}", True, (0,0,0))
            self.highest_score = self.font.render(f"High score: {self.settings.highest_score}", True, (255, 255, 255))
            if self.opcje:
                self.menu.opcje()
            else:
                self.menu.update()
            if not self.pauza:
                if self.settings.hearts_left != 0:
                    self.bg.update()

                    
                    for enemy in self.enemies:
                        enemy.update()
                    self.fireball.update()
                    for object in self.enemies:
                        if self.fireball.check_collision(object.rect):
                            object.kill()
                        if self.dragon.check_collision(object.rect):
                            object.kill()
                    self.dragon.update()
                    for diamond in self.diamonds:
                        if diamond.check_collision(self.dragon.image_rect):
                            diamond.kill()
                            self.settings.hearts_left += 1
                        diamond.update()
                
                if not self.diamonds:
                    number = random.randint(0, 500)
                    if number == 19:
                        self.diamonds.add(Diamond(self))
                else:
                    for diamond in self.diamonds:
                        if diamond.rect.right < 0:
                            diamond.kill()
                self.bg.blit()
                self.enemies.draw(self.screen)
                self.fireball.blit(int(self.fireball.iteration/3))
                self.dragon.blit(int(self.dragon.iteration/12))
                self.diamonds.draw(self.screen)
                self.screen.blit(self.points, (self.settings.screen_width - 150, 430))
                self.screen.blit(self.press_esc, (10, 10))
                self.heart.blit()


                if self.settings.hearts_left == 0:
                    self.game_over.blit()

                    if self.settings.points > self.settings.highest_score:
                        self.settings.highest_score = self.settings.points
                        with open('highest_score.txt', 'w') as f:
                            f.write(str(self.settings.highest_score))
                        self.high_score.blit()

                    pygame.display.flip()
                    self.clock.tick(1)
                    self.settings.hearts_left = 3
                    self.pauza = True

                    for enemy in self.enemies:
                        enemy.kill()
                    if self.settings.easy_mode:
                        for i in range(self.settings.easy_mode_enemies):
                            self.enemy = Enemy(self, i*500)
                            self.enemies.add(self.enemy)
                    else:
                        for i in range(self.settings.hard_mode_enemies):
                            self.enemy = Enemy(self, i*500)
                            self.enemies.add(self.enemy)


                    self.settings.points = 0
                    self.dragon.image_rect.left = self.screen_rect.left
                    self.dragon.image_rect.top = int(self.settings.screen_height/2)
                    self.settings.enemy_speed_x = 8
                    self.settings.enemy_speed_y = 1
                    self.fireball.image_rect.right = -100
                    self.fireball.fired = False
            else:
                self.screen.blit(self.highest_score, (150, 430))

            pygame.display.flip()
            self.clock.tick(self.settings.fps)

    def _keydown_action(self, event):
        if event.key == pygame.K_RIGHT:
            self.dragon.moving_right = True

        if event.key == pygame.K_LEFT:
            self.dragon.moving_left = True

        if event.key == pygame.K_F1:
            self.intro = True

        if event.key == pygame.K_UP:
            self.dragon.moving_up = True
            if self.pauza:
                if self.menu.counter == 0:
                    self.menu.counter = 2
                else:
                    self.menu.counter -= 1
            if self.opcje:
                if self.menu.counter_set == 0:
                    self.menu.counter_set = 3
                else:
                    self.menu.counter_set -= 1

        if event.key == pygame.K_DOWN:
            if not self.pauza:
                self.dragon.moving_down = True
            if self.pauza:
                if self.menu.counter == 2:
                    self.menu.counter = 0
                else:
                    self.menu.counter += 1
            
            if self.opcje:
                if self.menu.counter_set == 3:
                    self.menu.counter_set = 0
                else:
                    self.menu.counter_set += 1

        if event.key == pygame.K_SPACE:
            if not self.fireball.fired:
                self.fireball.fire(self)

        if event.key == pygame.K_ESCAPE:
            print("pauza")
            if self.outro:
                self.outro = False
            else:
                if self.opcje:
                    self.opcje = False
                elif not self.pauza:
                    self.pauza = True
                elif self.pauza:
                    self.pauza = False


        if event.key == pygame.K_RETURN:
            self.intro = False
            if self.opcje:
                self.settings.dragon_skin = self.menu.counter_set
                self.dragon.change_skin()
                self.opcje = False
            elif self.outro:
                self.playing = False
            else:
                self.menu.action(self)

    def _keyup_action(self, event):
        if event.key == pygame.K_RIGHT:
            self.dragon.moving_right = False
        if event.key == pygame.K_LEFT:
            self.dragon.moving_left = False
        if event.key == pygame.K_UP:
            self.dragon.moving_up = False
        if event.key == pygame.K_DOWN:
            self.dragon.moving_down = False

    def exit_game(self):
        self.outro = True
            
if __name__ == '__main__':
    game = Game()
    game.run_game()
    pygame.quit()
                