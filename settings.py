class Settings:
    """Class for all settings in this game"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        # ustawienie dotyczące statku
        self.ship_speed = 1.5
        # ustawienia dotyczące pocisku
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
