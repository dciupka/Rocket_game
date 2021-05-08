import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Alien class"""

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen

        # load alien and rect def

        self.image= pygame.image.load('images/ufo.bmp')
        self.rect= self.image.get_rect()

        #Alien in lef top corner
        self.rect.x =self.rect.width
        self.rect.y = self.rect.height

        #Przechowywanie dokładnego poziomego położenia obcego
        self.x = float(self.rect.x)
