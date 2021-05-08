class Settings:
    """Class for all settings in this game"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        # ustawienie dotyczące statku
        self.ship_speed = 1.5
        self.ship_limit=3
        # ustawienia dotyczące pocisku
        self.bullet_speed = 5
        self.bullet_width = 15
        self.bullet_height = 30
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 100
        self.alien_speed = 2.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

