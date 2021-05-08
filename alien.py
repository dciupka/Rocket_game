import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Alien class"""

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        # load alien and rect def

        self.image= pygame.image.load('images/ufo.bmp')
        self.rect= self.image.get_rect()

        #Alien in lef top corner
        self.rect.x =self.rect.width
        self.rect.y = self.rect.height

        #Przechowywanie dokładnego poziomego położenia obcego
        self.x = float(self.rect.x)


    def check_edges(self):
        screen_rect= self.screen.get_rect()
        if self.rect.right>= screen_rect.right or self.rect.left <=0:
            return True

    def update(self):
        "Move right alien"
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x