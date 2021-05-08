class GameStats:
    def __init__(self, game):
        self.settings = game.settings
        self.reset_stats()

    def reset_stats(self):
        """Dane statystyczne któr mogą się zmieniać w trakcie grty"""
        self.ships_left = self.settings.ship_limit
