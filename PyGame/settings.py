class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 500
        self.fps = 60
        self.x_speed = 6
        self.y_speed = 6
        self.bg_speed = 2

        self.font = "arialblack"
        self.font_size = 40
        self.points = 0

        self.fireball_speed = 5

        self.dragon_skin = 0

        self.easy_mode = False
        self.hard_mode = False

        self.enemy_speed_x = 8
        self.enemy_speed_y = 1

        self.easy_mode_enemies = 100
        self.hard_mode_enemies = 300

        self.hearts_left = 3

        self.highest_score = 0
